# PRODUCTION PIPELINE — Painted Doodle Comedy

**Target:** 8–12 min, 1920×1080, 24 fps. Flat 2D cutout comedy. Solo, ~8–12 days.
**Reference family:** Sam O'Nella / Casually Explained writing, executed with
TheOdd1sOut-tier painting. Teardown of a worked example: `TEARDOWN-rarest-things-universe.md`.

## One clarification up front

This style is frequently misdiagnosed as "MS Paint crude." It is not, and building it
that way produces something that looks accidentally bad instead of deliberately dumb.

Look closely at any reference frame and you find: **tapered pressure-sensitive outlines,
scribbled interior fill texture, soft airbrush glows, blush shading, and painted gradient
backgrounds.** The craft is competent. What is crude is the *character design* — circles
with googly eyes, stick bodies, faces that hold one dumb expression.

> **The look is simple shapes drawn well, not complex shapes drawn badly.**

Get this backwards and nothing else in this document will save you.

---

## STYLE BIBLE

### Line

Thick black contour, **8–12 px at 1080p**, with visible taper at stroke ends and a slight
organic wobble. Pressure→size **ON**. One confident pass — do not undo and redo until it
is smooth, the wobble is the signature. Outline colour is a warm near-black `#141414`,
never pure `#000000`.

### Fill

Flat base colour, then a **scribble pass** on a clipped layer above it: loose hatching in
a lighter tint of the same hue at 20–35% opacity. This is what gives the sun and the stars
their "coloured-pencil" interior. Without it the shapes read as dead vector.

### Glow

Every luminous body gets a soft halo on its own layer *behind* the character — large soft
airbrush, hue-matched, blend mode **Add** or **Screen**, 30–50% opacity. Plus a faint inner
rim on the character itself. This is the main thing separating these frames from flat clip-art.

### Palette (sampled from reference — resample from your own frames)

| Token | Hex | Use |
|---|---|---|
| Ink | `#141414` | All outlines |
| Space ground | `#4A4744` | Space bg — **warm grey, never black** |
| Nebula bloom | `#5A4A5E` / `#3E5450` | Faint purple + teal blooms, very low opacity |
| Star white | `#FFFFFF` | Dots at 3 sizes, scattered non-uniformly |
| Sun yellow | `#F5A81C` | Narrator avatar |
| Cold star | `#2BA3E8` | Blue glow bodies |
| Sick pink | `#F2A9A4` | Diseased / distressed bodies |
| Alarm red | `#C4282A` | Rationed — spots, devils, ✗ marks |
| Sky mint | `#C8E8EC` | Earth-scene sky / interior walls |
| Hill teal | `#8FCFD4` | Midground |
| Grass | `#7DC242` | Foreground ground |

Note the space background is **warm desaturated grey, not black.** Pure black space is
the single most common tell of an imitation.

### Backgrounds

Two families only:
- **Space:** grey gradient + white dots at 3 sizes + two or three barely-visible colour
  blooms. Paint once, reuse across the whole video.
- **Earth/interior:** flat pastel bands (sky / hills / ground) with a light scribble
  texture over each band. Also paint once per location.

You need roughly **8–10 backgrounds for an 11-minute video**, not 80.

### The photo-composite gag — the signature move

Real photographic fragments dropped onto crude drawings: a human mouth and teeth on a
cartoon planet, real sneakers on stick-figure legs, a real baby's face inside the sun.
This is the channel's highest-frequency laugh device and it costs almost nothing.

Rules that make it work:
1. **No feathering.** Hard-edged selection. The seam is the joke.
2. **Do not colour-match.** Leave the photographic lighting wrong.
3. **Do not resize to anatomical correctness.** Slightly too large is funnier.
4. **Ration it.** Roughly one per 60–90 seconds. Every shot and it stops registering.

---

## TOOL ASSIGNMENTS

| Tool | Role | Share |
|---|---|---|
| **Krita** | Everything drawn: characters, expressions, backgrounds, glows, gag art | **~80%** |
| **GIMP** | Photo-composite fragments, thumbnail finishing | ~10% |
| **CapCut** | The cut, keyframing, VO sync, captions | ~10% |
| **ElevenLabs** | Narration — directed line by line, see below | thin but decisive |
| `ffmpeg` | Loudness normalisation, final mux | one command |
| Inkscape | Title cards, clean arrows/labels only | ~2% |
| Blender | Not used. | 0% |
| FLUX / ComfyUI | Thumbnail, and any *deliberately polished* render the script mocks | ~2% |

> **Note on the stack.** CapCut and ElevenLabs are proprietary and cloud-backed, so the
> pipeline is no longer fully local or fully FOSS. Two practical consequences: narration
> costs credits per character, and the ElevenLabs **free tier grants no commercial rights
> and requires attribution** — monetised YouTube needs the Starter tier or above. If either
> becomes a problem, Kdenlive and a recorded voice are drop-in replacements.

### Krita — setup

- Canvas **1920×1080, sRGB, 8-bit**. There is no reason to work at 4K here.
- Brush: duplicate `Ink_gpen_25`. In the brush editor keep **Size → Pressure** enabled,
  spacing ~0.1, antialiasing on. This is your only outline brush — do not switch mid-video.
- Second brush: a large soft **Airbrush_soft** for glows, opacity 20–40%.
- Third brush: `Pencil_2B` or any textured pencil for the scribble fill pass.
- Layer template per character: `glow` (bottom) → `fill` → `scribble` (clipped to fill) →
  `line` → `face` (top, separate). Save as a Krita template.

### Krita — the avatar rig

The narrator avatar is drawn **once**. Keep the face on its own layer group and build an
expression set: deadpan (flat bar eyes — the default), smug, wide-eyed alarm, half-lidded
annoyance, grin with teeth, eyes-closed-smiling. **Eight to twelve is plenty.**

Nearly all the acting is eyes and eyebrows. Flat black bars for deadpan; big round whites
with tiny pupils for alarm. Mouth does less work than you think.

Export each expression as a transparent PNG at 2× (3840 wide) so you can push in without
softening.

### GIMP — photo composites

Free-select or fuzzy-select the fragment from a stock photo, **no feather**, paste onto the
drawing, scale, done. Do not clean up the edge. Public-domain sources keep this safe:
NASA image library, Wikimedia Commons, openverse. Avoid identifiable private individuals.

### CapCut — where the video is actually made

There is no animation in this style. There is **keyframed position/scale/rotation on PNGs,
cut hard to the voice.** CapCut is well suited to exactly this and is faster than Kdenlive
for it.

- Project 1920×1080, 24 or 30 fps. Drop the VO first, build the picture to it.
- Transparent PNGs import with alpha intact. Keyframe via the diamond on
  Position / Scale / Rotation. Leave interpolation linear — **no easing**.
- Assets **pop in on a single frame**. No fades. A crossfade here reads as an error.
- Split the VO at every punch word before placing a single image. The cut lands *on* the
  punch word, not after it.
- **Auto Captions** is genuinely good and suits this format. Restyle to Patrick Hand.
- Avoid any effect or sticker marked Pro — those are what trigger the watermark. Plain
  keyframes, text and cuts do not.

**Export settings matter more than usual here.** The painted space backgrounds are large
smooth gradients, and they band badly at CapCut's default bitrate. Export 1080p, custom
bitrate **16–20 Mbps**, and keep thin saturated red off dark grey — 4:2:0 chroma
subsampling will fringe it.

### Where FLUX and ComfyUI belong

FLUX produces coherent, polished, plausible images. That is the opposite of this visual
language, and using it for the artwork would flatten the comedy. Three sanctioned uses:

1. **The thumbnail.** Thumbnails need real polish even when the video does not.
2. **Any "professional" render the script sets up to mock.** When the narration presents a
   slick version before undercutting it, generate that one properly — the polish is the setup.
3. **Photo-fragment source**, if a real photo is hard to find. Real ones are funnier.

Never let it touch the doodles.

---

## VO — direct it, don't generate it

This writing is a **comedy performance**, not narration. The beat before a one-word
dismissal, the flat delivery of an insult — that timing *is* the product.

ElevenLabs v3 can do this, but only if you treat it as an actor you are directing rather
than a renderer you are feeding. The failure mode is pasting the whole script and taking
one render: the model then owns your comic timing, and it will smooth every pause flat.

**The workflow:**

1. **Generate line by line, never in bulk.** One take per sentence, or per punchline.
   The silence *between* lines is where the jokes live, and you want to own it in CapCut.
2. **Tag the delivery.** v3 reads bracketed cues as direction. The useful vocabulary for
   this voice: `[deadpan]`, `[flatly]`, `[matter-of-fact]`, `[understated]`,
   `[sarcastically]`, `[continues after a beat]`, `[slows down]`, `[rushed]`.
3. **Set stability to Natural or Creative — not Robust.** Robust actively reduces
   responsiveness to tags, so a `[deadpan]` on a Robust setting gets ignored. This is the
   opposite of the intuitive choice.
4. **Pauses:** use `[pause]` / `[short pause]` / `[long pause]`. v3 does **not** support
   SSML `<break>` tags. Use them sparingly — stacking pause tags in one generation causes
   audible artefacts. Prefer building long gaps in the edit instead.
5. **Pick takes.** Regenerate the load-bearing punchlines three or four times and choose.
   This is the single highest-leverage habit in the whole pipeline.
6. **Test tags against your chosen voice.** A serious, professional voice will not respond
   well to playful direction; some tags are inconsistent across voices.

**Then normalise.** ElevenLabs output is already clean, so no noise reduction is needed —
just loudness:

```
ffmpeg -i vo_raw.wav -af loudnorm=I=-14:TP=-1:LRA=11 -ar 48000 vo.wav
```

Assemble the per-line takes on the CapCut timeline **before you draw anything.** The edit
is built on the voice, and drawing to an untimed script means drawing for beats that get cut.

## TYPOGRAPHY

Handwritten or rounded-casual only. Free and correct: **Patrick Hand**, **Comic Neue**,
**Gloria Hallelujah**. Impact for caption-gag overlays. Segment cards are large, centred,
on-screen 1.5–2 s.

---

## FOLDER STRUCTURE

```
<video-slug>/
├── SCRIPT.md
├── SHOTS.md            # timecode → asset needed
├── art/
│   ├── avatar/         # body + expression set, PNG @2x
│   ├── cast/           # supporting characters
│   ├── bg/             # 8–10 painted backgrounds
│   ├── gags/           # one-off drawings
│   └── photo/          # composite fragments
├── audio/              # VO raw + cleaned, music, SFX
└── out/                # renders
```

Keep `.kra` masters out of git (or in LFS). Commit the exported PNGs.

---

## SCHEDULE (solo, part-time)

| Phase | Days | Output |
|---|---|---|
| Script + joke pass | 1.5 | Locked script, gags marked |
| VO record + cut to time | 0.5 | Timed voice track |
| Avatar + expression set | 1 | Rig + 8–12 faces |
| Backgrounds | 1 | 8–10 painted plates |
| Supporting cast | 1 | ~15 characters |
| Gag art | 2.5 | ~25 one-offs |
| Photo composites | 0.5 | ~15 fragments |
| Assembly + keyframing | 2.5 | Full cut |
| Sound, music, captions | 0.5 | Master |
| Thumbnail | 0.5 | |
| **Total** | **~11.5 days** | |

For contrast: `scripts/dancing-plague-1518/PIPELINE-krita-blender.md` budgets **58 days**
for 10 minutes. Same runtime, one fifth the cost. The aesthetic *is* the budget, and that
is the whole reason this format exists.

---

## GOTCHAS

1. Pure black space background. Use warm grey. Most common tell.
2. Flat fills with no scribble pass — reads as dead clip-art.
3. Pressure→size disabled. You get uniform vector-looking strokes and lose the whole line quality.
4. Feathering the photo composites. The hard seam is the joke.
5. Crossfades and eased motion. Everything is hard cuts and linear moves.
6. Drawing before the VO is cut. You will draw for beats that get trimmed.
7. Over-rationing expressions. Build 8–12 up front; drawing a new face mid-edit breaks flow.
8. Letting FLUX near the artwork. Polish is the enemy of this specific joke.
9. Too many photo composites. One per 60–90 s. It is seasoning.
10. Generating the VO as one block. You hand your comic timing to the model. Line by line.
11. Robust stability on ElevenLabs. It suppresses the delivery tags you need most.
12. Default CapCut export bitrate. The gradient backgrounds will band. 16–20 Mbps.
13. Shipping on the ElevenLabs free tier. No commercial rights, attribution required.
