# Pip Wants to Fly — production package

A 30-second animated kids' Short, planned for **Higgsfield** (keyframe stills → image-to-video).

| File | What's in it |
|---|---|
| [`STORY.md`](STORY.md) | Story outline, 13-shot beat sheet with timecodes, why each beat holds attention, optional 41-word VO, music + SFX plan, loop design |
| [`PROMPTS-higgsfield.md`](PROMPTS-higgsfield.md) | Style, character, lighting and negative locks; 6 asset prompts; 13 shots × keyframe + motion prompt (subject, art style, lighting, camera, negatives); 3 fast-route multi-shot prompts |
| [`SETTINGS-higgsfield.md`](SETTINGS-higgsfield.md) | Aspect ratio and resolution, models and credit costs, motion-strength and camera-control settings, per-shot settings table, QC, troubleshooting, export |

**Working title:** *Pip Wants to Fly* · Shorts title: *Can a Penguin Fly? 🐧*
**Runtime:** 0:30 · 9:16 · 1080×1920 · 13 shots
**Hook:** A tiny penguin flaps so hard his feet leave the ice — "Can a penguin fly?"
**Turn:** Three tries (flap, slide, balloons) end in a splash, and underwater Pip flies.
**Loop:** The last frame is the first frame, so the Short replays seamlessly.
**Budget:** ≈156 Higgsfield credits for a clean first pass; plan for ~300 with retakes (Kling 3.0 Pro 8.75 per clip, Nano Banana Pro 2 per image, quoted 2026-10-02).

## Start here

1. **Character first.** Generate Pip (prompts 0A–0C) and save him as a Higgsfield **Element**. Don't move on until he looks right; every shot inherits him.
2. **World.** Generate the two location plates and the balloon prop (0D–0F) and save them as Elements.
3. **Keyframes.** Generate all 15 stills (13 start frames plus the end frames for shots 05 and 12) and check each one against the character sheet. A bad still costs 2 credits to redo; a bad clip costs 8.75 or more.
4. **Animate shot 01 first** and compare it with the sheet; the first clip is where style drift shows up. Then animate the rest.
5. **Edit** to the beat sheet: 120 BPM music, SFX, optional VO. Check the loop.
6. **Publish.** Optionally run the cut through Higgsfield's Virality Predictor for hook and retention risk. Upload as a Short with the audience set to **Made for kids**.

In a hurry? The fast route at the end of `PROMPTS-higgsfield.md` makes the whole Short as three 10-second multi-shot clips (≈72 credits), with less control per shot.
