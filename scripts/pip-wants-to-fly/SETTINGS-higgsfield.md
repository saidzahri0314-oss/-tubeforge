# HIGGSFIELD SETTINGS — Pip Wants to Fly

Checked against Higgsfield's live model catalog on 2026-10-02: model names, aspect ratios, parameters, and credit prices quoted for your account. Menus and prices change, so re-check costs before a big batch.

## 1. Frame & format

| Setting | Use | Why |
|---|---|---|
| Aspect ratio | **9:16** vertical | Shorts, TikTok and Reels are vertical; Kling 3.0, Seedance 2.0, MiniMax H3, Cinema Studio and Nano Banana Pro all generate 9:16 natively |
| Delivery size | **1080×1920** | Standard Shorts upload |
| Keyframes | Nano Banana Pro · **2K** · 9:16 | A start frame sharper than the video gives the animation detail to keep |
| Clips | Kling 3.0 · **Pro** mode | Kling's higher-quality tier on Higgsfield; a 4K mode exists if you need it |
| Generated length | **5 s** per shot, keep 2–3 s | Gives you handles to trim; drift and freezes live in the first fraction of a second and the tail |
| Frame rate | the clips' native rate (check one clip; usually 24 fps) | Mixing rates or forcing 30/60 fps in the edit causes judder |
| Safe zone | Pip's face and the main action in the middle ~60% of the frame height; bottom fifth plain; right edge clear | Shorts' title, captions and buttons sit there |

- **Set 9:16 on every video generation.** Don't count on the clip inheriting it from the start frame; Higgsfield's own kids-video pipeline sets the ratio explicitly on every call.
- **Don't crop 16:9 down to 9:16.** You lose resolution and the composition falls apart.
- **Need 16:9 as well** (a compilation episode, YouTube on a TV)? Make a separate 16:9 pass of the keyframes and re-animate, or test Higgsfield's Reframe tool on one clip before trusting it with all 13.

## 2. Models & credits

| Job | Model | Settings | Credits (quoted 2026-10-02) | Why this one |
|---|---|---|---|---|
| Character sheets, plates, keyframes, end-frame edits | **Nano Banana Pro** | 2K · 9:16 (sheets 16:9 or 2:3, prop 1:1) | 2 per image | Works with Elements, holds a character steady, and handles "edit this image" end frames |
| Animate every shot | **Kling 3.0** | Pro · 5 s · 9:16 · sound off | 8.75 per clip (12.5 with sound) | Expressive cartoon motion, start + end frames, and the cheapest high-quality option priced here |
| Fallback when Pip drifts | **Seedance 2.0** | std · 720p · 5 s · genre Comedy · start frame + turnaround sheet as image reference | 22.5 per clip (45 at 1080p) | Holds identity from reference images best |
| Optional designed camera on one shot | **Cinematic Studio Video 3.5** | 1080p · 5 s · camera style Dreamy Flow | 50 per clip | Named camera styles; too pricey for more than one shot |
| Fast route (3 clips instead of 13) | **MiniMax H3** | 2K · 10 s · up to 7 reference images | 20 per 10 s block | The model Higgsfield's own kids-video workflow uses for 10 s, four-cut scenes |

**Budget, shot-by-shot route**

| Item | Count | Credits |
|---|---|---|
| Assets (Pip ×3, two plates, balloons) | 6 images × 2 | 12 |
| Keyframes (13 start + end frames for shots 05 and 12) | 15 images × 2 | 30 |
| Clips (Kling 3.0 Pro, 5 s, sound off) | 13 × 8.75 | 113.75 |
| **Clean first pass** | | **≈156** |
| Native sound on the four "optional" shots | 4 × 3.75 | +15 |
| **Plan for, with retakes** | | **~300** |

Fast route: 12 for assets + 3 × 20 for the blocks ≈ **72 credits** first pass, ~130 with a retake of each block.

## 3. Motion strength

Higgsfield has no universal "motion strength" slider. Kling 3.0, Seedance and MiniMax H3 expose no intensity parameter at all; they take motion intensity from the prompt, the camera move and the start/end frames. The closest thing is on **Cinema Studio Video 2**: **Speed Ramp** (Linear / Slow-mo / Speed-up / Impact) and **Prompt Adherence** (cfg, 0–1, default 0.5). Cinematic Studio Video 3.5 adds named camera styles (section 4).

So motion strength is set with five levers:

1. **Verbs and adverbs**: "gentle, floaty" vs "bouncy, springy" vs "fast, zippy".
2. **How many things move**: one action per shot. Every extra moving thing raises the effective strength.
3. **The camera move**: a static camera reads calmer than any move.
4. **Start + end frames**: they pin where the motion has to land (shots 05, 12, 13).
5. **How much you keep**: a shorter keep hides drift. Fast shots keep 2 s unless an end frame pins the landing (shot 05 keeps 3 s).

| Level | Shots | Prompt words | Subject | Camera | Keep | If a model page shows a motion slider |
|---|---|---|---|---|---|---|
| **Low** | 02, 09 | gentle, slow, floaty, calm | one small action | static, slow push-in or tilt | 2 s | ~30–40% |
| **Medium** (default) | 01, 03, 06, 07, 11, 13 | bouncy, springy, playful, squash-and-stretch | one clear action | one smooth move | 2–3 s | ~50% |
| **High** | 04, 05, 08, 10, 12 | fast, zippy, energetic, exaggerated | one big action that settles | static, or one move that follows Pip | 2 s (3 s with an end frame) | 60–70%, never max |

Rules that keep the quality up:

- **High motion only on medium and wide shots.** Close-ups stay Low or Medium; big motion on a face is where beaks and eyes melt. That's why shot 07's sneeze is one jolt in a static close-up.
- **Never pair fast subject motion with a fast camera** unless the camera follows the subject. Shot 04's fast backward track keeps Pip centered, so his motion on screen stays moderate.
- **End every action on a settled pose.** It stops end-of-clip drift and gives clean cut points.
- **If you run a shot on Cinema Studio Video 2:** Prompt Adherence 0.6 for scripted gags and 0.5 for floaty shots; Speed Ramp Linear, except Slow-mo for the leap (12) and Impact for the splash (08).

## 4. Camera control

- **One camera behavior per shot.** Two moves in one clip (a push-in plus an orbit) is the fastest way to get mush; Higgsfield's own prompt guidance says the same. Every motion prompt here puts the move on its own `CAMERA:` line and ends it with "nothing else".
- **Gags and big beats are locked off:** shots 03, 05, 07, 08, 10, 12 and 13 use a static camera. A gag reads best when the frame holds still, and a still frame lets fast action read cleanly.
- **Moves are smooth and slow-to-medium:** push-in, tilt, crane, tracking. No handheld shake, dutch angles, crash zooms or fast orbits; they warp the character and feel chaotic to small viewers.
- **For exact control, use start + end frames.** Make the end keyframe by editing the start keyframe (attach it as the base image and change only Pip), so the background is identical and the model only has to animate the change between them. Shots 05, 12 and 13 work this way.
- **There are no one-click dolly or crane presets to lean on.** Higgsfield's preset galleries (searched 2026-10-02) carry effect templates such as Earth Zoom, not plain camera moves, so the moves are written into the prompts.

| # | Camera | # | Camera |
|---|---|---|---|
| 01 | slow push-in | 08 | static, top-down |
| 02 | slow tilt up | 09 | slow push-in |
| 03 | static | 10 | static (Pip passes the lens) |
| 04 | fast tracking backward at snow level | 11 | lateral tracking, left to right |
| 05 | static wide (start + end frame) | 12 | static low angle (start + end frame) |
| 06 | crane up | 13 | static eye level (end frame = shot 01) |
| 07 | static | | |

**Cinematic Studio Video 3.5 camera styles**, if you want one shot with a more designed camera (≈50 credits per 5 s, against 8.75 on Kling): Classic Static, Silent Machine, One Take, Epic Scale, Intimate Observer, Impossible Camera, Documentary Snap, Raw Chaos, Dreamy Flow. Going by the names (test one generation first), Dreamy Flow fits shot 11, Classic Static fits the gags and Epic Scale fits the leap. Skip Raw Chaos and Documentary Snap, which suggest shaky handheld. For its color grade, Naturalistic Clean keeps the candy colors; the teal-orange, bleach-bypass and cold-steel grades fight them.

## 5. Per-shot settings

All Kling 3.0 · Pro · 5 s · 9:16. "Optional" sound means: switch native sound on (12.5 instead of 8.75 credits) only if you aren't doing your own SFX pass. Those prompts already carry an `AUDIO` line.

| # | Keep | Frames | Camera | Motion | Native sound |
|---|---|---|---|---|---|
| 01 | 2.5 s | start | slow push-in | Medium | off |
| 02 | 2.0 s | start | slow tilt up | Low | off |
| 03 | 2.5 s | start | static | Medium → High on the drop | optional |
| 04 | 2.0 s | start | fast tracking backward | High | off |
| 05 | 3.0 s | start + end | static wide | High → settles | optional |
| 06 | 3.0 s | start | crane up | Medium | off |
| 07 | 2.0 s | start | static | Medium (one jolt) | off |
| 08 | 2.0 s | start | static top-down | High | optional |
| 09 | 2.0 s | start | slow push-in | Low | off |
| 10 | 2.0 s | start | static | High | off |
| 11 | 2.5 s | start | lateral tracking | Medium–High | off |
| 12 | 2.0 s | start + end | static low angle | High, in slow motion | optional |
| 13 | the last 2.5 s | start + end (= shot 01 keyframe) | static eye level | Low → Medium | off |

## 6. Prompt rules that matter on Higgsfield

1. **Don't name studios or franchises** ("Pixar", "Disney", "DreamWorks"). Describe the look instead; the style lock already does.
2. **Keep "child", "kid" and "childlike" out of prompts.** Higgsfield's own kids-video pipeline bans those words because they trip false content flags. These prompts also avoid "baby" to be safe, and use "little", "small" and "preschool" instead.
3. **Paste the locks unchanged.** The same style, lighting and negative text in every prompt is the consistency mechanism.
4. **One action and one camera move per shot.** Write the action as choreography, one verb after another ("tips forward, dives, wiggles").
5. **Negatives go on the last line** (`NEGATIVE: …`). These models have no separate negative field; if a model page shows one, move the list there.
6. **No words in the picture.** Generated lettering comes out as gibberish; titles and captions go in the edit.
7. **Pip never talks on screen.** The VO and his little sounds go in the edit, so there is no lip-sync to break.

## 7. QC: before you animate, and again before you edit

- [ ] Pip is on model: two flippers, three-feather tuft, cream heart-shaped face patch, orange beak and feet, cherry-red scarf with **one** white stripe.
- [ ] Five balloons, the same five colors, strings in his flipper — never around his neck.
- [ ] The sun comes from the upper left in every outdoor shot; Pip's progress moves left → right.
- [ ] No letters or numbers anywhere, no extra limbs, no face melt in the fast shots.
- [ ] Every clip moves from its first frame (trim if it doesn't).
- [ ] Shot 13's last frame is shot 01's first frame.
- [ ] Nothing scary: bright water, happy faces, no flashing.

## 8. Troubleshooting

| Problem | Fix |
|---|---|
| Pip drifts off model | Fix the keyframe, not the clip: re-attach @Pip, shorten the SUBJECT line, regenerate. If he still drifts once moving, run that shot on Seedance 2.0 with the start frame plus the turnaround sheet as an image reference (genre Comedy). |
| A generation is flagged or blocked for no clear reason | Retry it unchanged a couple of times; these flags are often random. If it keeps failing, reword (drop any child/kid/baby words), widen a tight face close-up, calm the pose. That's Higgsfield's own retry order. |
| Face or flippers melt in fast action | Drop to Medium wording, keep 2 s or less, lock the camera, or add an end frame. |
| The camera makes two moves or wanders | One `CAMERA` verb plus "nothing else"; for an exact path, use start + end frames. |
| The clip opens on a frozen frame | Trim the first frames; regenerate if the move starts late. |
| Gibberish letters appear | Don't describe signs or labels; keep "text, letters, numbers" in the negative; add titles in the edit. |
| The balloons change number or color | Attach @Balloon-Bunch and keep the five colors named in the prompt. |
| The loop visibly jumps | Shot 13's end frame must be the exact shot 01 keyframe image, and the cut must fall on shot 13's last frame. |

## 9. Edit & export

- Timeline 1080×1920 at the clips' native frame rate. Lay each shot in at its keep-length from the beat sheet in [`STORY.md`](STORY.md).
- 120 BPM music, so every cut lands on a beat (every shot length is a multiple of 0.5 s).
- Mix: VO on top, music ducked under it, one SFX per motion; aim for about −14 LUFS integrated, the level YouTube plays back at.
- Export H.264 MP4 at a high bitrate with AAC audio.
- Upscale only if needed: Higgsfield's video upscalers (Topaz, Bytedance Video Upscale) can lift the final cut, and FPS Boost can smooth motion. Test on one shot first.
- Before posting, optionally run the cut through Higgsfield's Virality Predictor for hook and retention risk. Publish as a Short with the audience set to **Made for kids**.
