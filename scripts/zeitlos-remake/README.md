# Seniorenresidenz „Zeitlos" — Higgsfield fix-up (720p)

Fixes the 4:12 German tour video (CapCut AI original, 816×464). Only shots where a host is out of
uniform are re-rendered; every other shot, the script, the voices and the timing stay as they are.
Each fixed host gets the face from their reference photo and the light-blue scrubs already worn in
the kept shots.

## Shot audit

| Time | Host photo | In the original | Action |
|---|---|---|---|
| 0:00–0:40 | photo 3 | light-blue scrubs | keep |
| 0:40–1:25 | photo 5 | bright-blue sweater | **fix** (f01, f02) |
| 1:25–2:25 | photo 2 | navy scrubs, Nike logo bleed at 2:23 | **fix** (f03–f05) |
| 2:25–2:37 | photo 4 | teal scrubs, training shop | **fix** (f06) |
| 2:37–2:49 | photo 4 | light-blue scrubs, bus stop | keep |
| 2:49–3:01 | photo 4 | teal scrubs, yoga + pool | **fix** (f07) |
| 3:01–3:13 | photo 4 | light-blue scrubs, dog + dining | keep |
| 3:13–3:37 | photo 1 | turquoise scrubs, baking + crafts | **fix** (f08) |
| 3:37–3:49 | photo 1 | light-blue scrubs, schedule board | keep |
| 3:49–4:01 | photo 1 | red blouse + leather jacket | **fix** (f09) |
| 4:01–4:12 | group, L→R 4, 1, 3, 5, 2 | photos 4, 5, 2 out of uniform | **fix** 1st, 4th, 5th (f10) |

**Uniform:** medium light-blue (cornflower) short-sleeve V-neck scrub top with seam piping and a pen
in the chest pocket, matching scrub trousers, white clip-on photo ID badge. No stethoscope, jacket,
sweater or logos. `pipeline.py uniform` crops it from 3:44 and 3:10 of the original (below the chin)
and that image is passed as the last `@Image` of every edit.

## Method

Higgsfield **Ad Multiplier** (`model: ad_multiplier`, Seedance 2.5, `mode: video_edit`) replaces the
presenter in each clip while keeping motion, lip movements, camera and timing. Clips start and end on
shot cuts and stay within its 4–30 s limit. Prompts are in `prompts.json` (from `build_prompts.py`):

```json
{"model": "ad_multiplier", "mode": "video_edit", "resolution": "720p", "aspect_ratio": "auto",
 "generate_audio": false, "duration": <ceil(clip seconds)>, "prompt": "<prompts.json[fNN].prompt>",
 "medias": [{"role": "video", "value": "<fNN clip>"}, {"role": "image", "value": "<host photo>"}, ...,
            {"role": "image", "value": "<uniform_ref>"}]}
```

```bash
python3 pipeline.py chunk   original.mp4 clips/             # f01..f10
python3 pipeline.py uniform original.mp4 uniform_ref.png
python3 pipeline.py splice  original.mp4 edits/ final.mp4   # e01..e10 from Higgsfield -> full video
```

`splice` rebuilds the full 252.5 s at 1266×720 / 30 fps from the kept shots plus the edits and puts the
original German audio back, so narration and lip-sync line up with the source.

## Quality check

Inspect frames from every edit against its reference photo: face match, the same scrub shade as the
kept shots, no stethoscope or logo, and residents/props unchanged. Retry a failed clip once.

## Cost

177 billed seconds (10 clips). Seedance 2.5 at 720p preflights at 7 credits/s, so about **1,240
credits**, against 1,464 available. The exact Ad Multiplier price is confirmed with `get_cost` on the
first clip before anything is spent.

`transcript_de.txt` is a machine transcript (Whisper small) of the original narration, for reference.
