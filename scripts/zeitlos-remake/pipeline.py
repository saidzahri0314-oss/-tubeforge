"""Zeitlos remake pipeline (needs ffmpeg/ffprobe; runs locally or in the Higgsfield sandbox).

  python3 pipeline.py chunk   <source.mp4> <outdir>              -> f01.mp4 .. f10.mp4, the clips to fix
  python3 pipeline.py uniform <source.mp4> <out.png>             -> uniform reference crop (no face)
  python3 pipeline.py splice  <source.mp4> <editdir> <out.mp4>   -> full 720p video: kept shots from the
                                                                    source + e01..e10 edits, original audio

Clip ranges come from prompts.json, so build_prompts.py stays the single source of truth.
"""
import json, math, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS = json.load(open(os.path.join(HERE, "prompts.json")))
FPS = 30
W, H = 1266, 720  # 720p at the source's 816x464 aspect


def ff(*args):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *args], check=True)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         check=True, capture_output=True, text=True).stdout
    return float(out)


def frames(a, b):
    return round((b - a) * FPS)


def cut(src, a, b, out, scale=None):
    vf = f"trim=start={a}:end={b},setpts=PTS-STARTPTS,fps={FPS}"
    if scale:
        vf += f",scale={scale}:flags=lanczos,setsar=1"
    ff("-i", src, "-vf", vf, "-frames:v", str(frames(a, b)), "-an",
       "-c:v", "libx264", "-preset", "slow", "-crf", "14" if not scale else "16", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out)


def chunk(src, outdir):
    os.makedirs(outdir, exist_ok=True)
    for k, c in CLIPS.items():
        out = os.path.join(outdir, f"{k}.mp4")
        cut(src, c["start"], c["end"], out)
        print(k, c["start"], c["end"], f"{duration(out):.3f}s", f"bill {math.ceil(c['duration'])}s")


def uniform(src, out):
    # Light-blue scrubs already worn at 3:44 (top, badge, pen) and 3:10 (top + trousers), cropped below the chin.
    with tempfile.TemporaryDirectory() as t:
        ff("-ss", "224", "-i", src, "-frames:v", "1", "-vf", "crop=400:190:40:274,scale=-1:500:flags=lanczos", f"{t}/a.png")
        ff("-ss", "190", "-i", src, "-frames:v", "1", "-vf", "crop=230:250:120:214,scale=-1:500:flags=lanczos", f"{t}/b.png")
        ff("-i", f"{t}/a.png", "-i", f"{t}/b.png", "-filter_complex", "[0][1]hstack", out)
    print(out)


def splice(src, editdir, out):
    end = duration(src)
    fixes = sorted(((c["start"], c["end"], k) for k, c in CLIPS.items()))
    timeline, t = [], 0.0
    for a, b, k in fixes:
        if a > t:
            timeline.append((t, a, None))
        timeline.append((a, b, k))
        t = b
    if t < end - 1 / FPS:
        timeline.append((t, end, None))
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, (a, b, k) in enumerate(timeline):
            part = os.path.join(tmp, f"p{i:02d}.mp4")
            if k is None:
                cut(src, a, b, part, scale=f"{W}:{H}")
            else:
                edit = os.path.join(editdir, k.replace("f", "e", 1) + ".mp4")
                got = duration(edit)
                # Fail rather than freeze-frame if an edit came back short.
                if got < (b - a) - 0.1:
                    sys.exit(f"{edit} is {got:.2f}s, needs {b - a:.2f}s")
                ff("-i", edit, "-map", "0:v:0", "-an", "-vf", f"fps={FPS},scale={W}:{H}:flags=lanczos,setsar=1",
                   "-frames:v", str(frames(a, b)), "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", part)
            parts.append(part)
            print(f"{a:7.2f}-{b:7.2f}  {'edit ' + k if k else 'keep'}")
        lst = os.path.join(tmp, "list.txt")
        open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
        ff("-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", f"{tmp}/video.mp4")
        ff("-i", f"{tmp}/video.mp4", "-i", src, "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
           "-c:a", "aac", "-b:a", "192k", "-af", "apad", "-t", f"{sum(frames(a, b) for a, b, _ in timeline) / FPS}",
           "-movflags", "+faststart", out)
    print(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,duration", "-of", "compact", out],
                         capture_output=True, text=True).stdout)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "chunk" and len(sys.argv) == 4:
        chunk(sys.argv[2], sys.argv[3])
    elif cmd == "uniform" and len(sys.argv) == 4:
        uniform(sys.argv[2], sys.argv[3])
    elif cmd == "splice" and len(sys.argv) == 5:
        splice(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit(__doc__)
