#!/usr/bin/env bash
# Zeitlos remake pipeline.
#   chunk    <source.mp4> <outdir>             -> c01.mp4 .. c12.mp4 (silent, 30 fps, exact frame counts)
#   assemble <source.mp4> <editdir> <out.mp4>  -> joins e01.mp4 .. e12.mp4 (Higgsfield edits) at 720p
#                                                 and lays the original German audio back on top
# Runs anywhere ffmpeg/ffprobe/python3 exist (locally or in the Higgsfield sandbox).
set -euo pipefail

# Chunk boundaries in seconds; each chunk is 4-30 s (Ad Multiplier limit) and starts on a shot cut.
BOUNDS=(0 20 40 58 85 109 133 145 169 193 217 241 252.5)
FPS=30
W=1266; H=720   # 720p at the source's 816x464 aspect

frames() { python3 -c "print(round(($2-$1)*$FPS))"; }

chunk() {
  local src=$1 out=$2; mkdir -p "$out"
  for i in $(seq 0 11); do
    local a=${BOUNDS[$i]} b=${BOUNDS[$((i+1))]} n; n=$(printf "%02d" $((i+1)))
    ffmpeg -nostdin -v error -y -i "$src" \
      -vf "trim=start=$a:end=$b,setpts=PTS-STARTPTS,fps=$FPS" -frames:v "$(frames "$a" "$b")" -an \
      -c:v libx264 -preset slow -crf 14 -pix_fmt yuv420p -movflags +faststart "$out/c$n.mp4"
    echo "c$n  $a-$b s  $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out/c$n.mp4") s"
  done
}

assemble() {
  local src=$1 edits=$2 out=$3 tmp; tmp=$(mktemp -d)
  : > "$tmp/list.txt"
  for i in $(seq 0 11); do
    local a=${BOUNDS[$i]} b=${BOUNDS[$((i+1))]} n; n=$(printf "%02d" $((i+1)))
    local f="$edits/e$n.mp4" want; want=$(frames "$a" "$b")
    [ -f "$f" ] || { echo "missing $f" >&2; exit 1; }
    # Fail rather than freeze-frame if an edit came back short.
    local got; got=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
    python3 -c "import sys; sys.exit(0 if $got >= ($b-$a) - 0.1 else 1)" || { echo "e$n too short: $got s" >&2; exit 1; }
    ffmpeg -nostdin -v error -y -i "$f" -map 0:v:0 -an \
      -vf "fps=$FPS,scale=$W:$H:flags=lanczos,setsar=1" -frames:v "$want" \
      -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p "$tmp/n$n.mp4"
    echo "file '$tmp/n$n.mp4'" >> "$tmp/list.txt"
  done
  ffmpeg -nostdin -v error -y -f concat -safe 0 -i "$tmp/list.txt" -c copy "$tmp/video.mp4"
  ffmpeg -nostdin -v error -y -i "$tmp/video.mp4" -i "$src" -map 0:v:0 -map 1:a:0 \
    -c:v copy -c:a aac -b:a 192k -af "apad" -t "${BOUNDS[12]}" -movflags +faststart "$out"
  rm -rf "$tmp"
  ffprobe -v error -show_entries stream=codec_type,width,height,duration -of compact "$out"
}

case "${1:-}" in
  chunk) chunk "$2" "$3" ;;
  assemble) assemble "$2" "$3" "$4" ;;
  *) echo "usage: $0 chunk <source.mp4> <outdir> | assemble <source.mp4> <editdir> <out.mp4>" >&2; exit 2 ;;
esac
