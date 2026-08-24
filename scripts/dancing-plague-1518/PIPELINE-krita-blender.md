# PRODUCTION PIPELINE — Krita → Blender

**Target:** 8:08, 3840×2160, 24 fps, stylized cartoon.

## One clarification up front

Krita is a 2D application — it has no 3D modelling or rendering. So the "2D/3D cartoon" split works like this:

- **Krita owns every pixel that is drawn:** style frames, character design, textures, paper/ink overlays, the flat explainer plates, and all hand-animated 2D FX.
- **Blender owns everything that is built and lit:** models, rigs, crowds, cameras, and the render.
- **The cartoon look is not a Krita export — it is a Blender shading decision.** Toon ramps plus Grease Pencil line art are what make the 3D read as a drawing. Krita supplies the texture and the hand-made irregularity that stops it looking like default Blender.

---

## STYLE BIBLE

**"Woodcut Gothic."** Renaissance block-print — Dürer, Holbein's *Danse Macabre* — crossed with a modern stylized cartoon. Chunky silhouettes, heavy contour lines, cross-hatched shadow, visible paper grain under everything.

**Palette — 4 colours, and the discipline is the point:**

| Token | Hex | Use |
|---|---|---|
| Parchment | `#E8DCC0` | Base / paper / highlights |
| Ink | `#1A1614` | Lines, shadow, silhouette |
| Ochre | `#B07D3A` | Midtone, wood, skin shadow |
| **Plague red** | `#C42B1C` | **Rationed.** See below. |

**Red is the story.** Track it deliberately: Cold open = a few pixels. Act I = accents only. Act III = red dominates the frame. Act IV = drains to cold blue, red shoes are the *only* saturated object in the shot. Act V = flat white explainer mode, red used only for ✗ marks. Close = red returns and takes the frame.

**Colour script by act:** parchment/ochre → ochre + red accents → red-dominant, sickly greens → cold blue night → clean paper white → red.

---

## STAGE 1 — KRITA

Work at **3840×2160, 300 dpi, sRGB, 16-bit**. Keep layers; flatten only on export.

### 1.1 Style frames (do this first, do not skip)
Paint **six** finished frames — one per act — before a single model is built. They lock the palette, line weight, and lighting, and they are what you compare every render against. Deliver as `art/style/ACT-0X_styleframe.png`.

### 1.2 Character model sheets
For each hero character (Troffea, Physician, Councillor, Musician, Strongman): front / side / three-quarter / back turnaround on a shared horizontal guide grid, plus an expression sheet.

- Set up guide lines with **View → Show Rulers / Guides** so eye line and shoulder line match across all views. Blender will use these as reference planes and any mismatch becomes a modelling error.
- Export front and side views **separately** at identical pixel height → `art/sheets/<char>_front.png`, `_side.png`.

### 1.3 Texture painting (the round trip)

This is the part people get wrong, so in order:

1. **Blender:** UV unwrap the model. In the UV editor: `UV → Export UV Layout` → PNG, 2048 or 4096, fill opacity `0`.
2. **Krita:** open that PNG. Put it on the **top** layer, set blend mode **Normal** at ~30% opacity, lock it. Paint on layers *underneath* it.
3. Paint the albedo. Use `Ink_gpen` for line detail, `Chalk` / `Charcoal` for hatching, `Bristles` for broken wood and cloth.
4. Hide the UV guide layer → `File → Export` → PNG.
5. **Blender:** Image Texture node → **Colour Space: sRGB** for albedo.
6. Masks, roughness, occlusion → export as **grayscale** PNG → **Colour Space: Non-Color**. Getting this backwards is the single most common cause of "why does my texture look washed out."

### 1.4 Overlay plates (paint once, use in every shot)
Tileable 4K: paper fibre, ink bleed, cross-hatch at three densities, dust/scratch. → `art/overlays/`. These go into the Blender **compositor**, not the shaders — one place to control, no per-material fiddling.

### 1.5 2D FX and explainer plates
Krita's animation timeline handles everything that should look hand-drawn: ink-splatter transitions, smoke, the red spread in shots `00F` / `04G`, the ✗ stamps.

- `Window → Workspace → Animation` to get the Animation Timeline docker.
- Enable onion skinning; work on 2s (12 drawings per second) — full 24 is wasted effort at this scale and 2s reads as more hand-made, not less.
- `File → Render Animation → PNG Image Sequence`, name `fx_inkwipe_####.png`.
- Into Blender either as an Image Sequence on a plane with alpha (**Settings → Blend Mode: Alpha Blend**, tick **Show Backface: off**), or straight into the compositor / VSE.

The Act V explainer plates (`06C`–`06E`), the humours wheel (`03C`), the anatomy cutaway (`03D`) and the map (`02A`) are **pure Krita**. They are supposed to look like a different medium — that visual break is doing retention work.

---

## STAGE 2 — BLENDER

**Blender 4.2 LTS or newer** (EEVEE Next). Check your version's Grease Pencil naming — GPv3 in 4.3+ renamed some panels.

Scene: 24 fps, 3840×2160, metric, 1 unit = 1 m.

### 2.1 Modelling from the sheets
`Add → Image → Reference` for `_front.png` and `_side.png`, rotate to front and side ortho, lock both (`Object Properties → Visibility → Selectable: off`). Model low-poly and chunky — silhouette does the work, and line art rewards clean topology. Crease-tag every edge you want inked.

### 2.2 The toon shader

Base recipe, EEVEE only:

```
Diffuse BSDF ──▶ Shader to RGB ──▶ ColorRamp ──▶ Emission ──▶ Material Output
                                   (Constant,
                                    3 stops)
```

- **ColorRamp interpolation must be `Constant`.** That is what produces hard cel bands instead of a gradient. This is the whole trick.
- Three stops: shadow / midtone / light, pulled from the palette above. Do not use pure black in the shadow stop — use Ink `#1A1614`.
- Mix the Krita albedo in: `Image Texture → Mix (Multiply, factor 1.0)` against the ColorRamp output.
- Rim light: `Layer Weight (Facing) → ColorRamp (Constant) → Mix (Add)`. Keep it subtle except on the Act IV cave shots, where it does all the work.

> **`Shader to RGB` does not exist in Cycles.** If any shot needs Cycles, that shot needs Freestyle instead, and a different shader. Decide per sequence, not per shot.

### 2.3 Line art
Add a Grease Pencil object → **Line Art modifier** → Source: Scene or Collection.

- Edge types on: **Contour, Crease, Material, Intersection**. Leave Edge Marks off unless you are hand-tagging.
- Add a **Noise** GP modifier at low strength for hand-drawn wobble. Without it the lines are too perfect and the whole thing reads as CG.
- Add **Thickness** modifier with a slight taper.
- **Bake Line Art** before final render. Live evaluation on every frame is a large chunk of your render time, and baking also lets you fix bad lines by hand.

### 2.4 The 400-dancer crowd

Do not rig 400 characters. Three tiers:

| Tier | Count | Method |
|---|---|---|
| Hero | 1–8 | Full rig, hand-animated. Only these get close-ups. |
| Mid | ~60 | Linked duplicates of 3 rigs, randomised NLA offsets |
| Far | 300+ | Krita-painted dance-cycle cards on billboards |

Randomise the mid tier so it doesn't pulse in unison — select the duplicates and run:

```python
import bpy, random
random.seed(1518)
for ob in bpy.context.selected_objects:
    ad = ob.animation_data
    if not ad:
        continue
    for track in ad.nla_tracks:
        for strip in track.strips:
            strip.frame_start_ui += random.randint(0, 47)  # ±2 s spread @ 24 fps
            strip.repeat = 30
```

Vary hue per instance too: `Object Info → Random → Hue/Saturation (Hue)` at ~0.03 strength. Tiny, but it kills the clone-army read.

### 2.5 Camera
28 mm for streets, 50 mm for the face shots, 85 mm for `05E` and `06F`. Every move is slow and mechanical — dolly and crane, no handheld — **except** the three-cut sequences (`02C`, `04F`, `05D`), which are the only handheld in the film. That contrast is why they land.

Shot `07A` is one continuous 18-second lateral track with no cuts. Build it as one long set dressed along a straight line and move the camera on a linear F-curve. Do not be tempted to cut it up.

### 2.6 Compositor

```
Render Layers ─▶ Mix(Overlay, 0.2) ◀── Krita paper texture
              ─▶ Lens Distortion (Dispersion 0.005)
              ─▶ Mix(Overlay) ◀── film grain
              ─▶ Vignette
              ─▶ Composite
```

### 2.7 Render settings
- **EEVEE Next**, 64 samples, Motion Blur **on** (shutter 0.5).
- **View Transform: `Standard`**, Look: None. The 4.x default AgX will desaturate your flat cel colours and quietly undo the palette work. This matters more than the sample count.
- `Render Properties → Performance → Persistent Data: on`.
- Output **PNG sequence** (or OpenEXR), never straight to MP4 — a crash four hours in should not cost you the sequence.
- Encode after the fact:
  ```
  ffmpeg -framerate 24 -i render/shot_%04d.png -i vo.wav \
         -c:v libx264 -crf 16 -pix_fmt yuv420p -c:a aac -b:a 192k out.mp4
  ```

---

## FOLDER STRUCTURE

```
dancing-plague-1518/
├── SCRIPT.md
├── PIPELINE-krita-blender.md
├── SOURCES.md
├── art/            # Krita — .kra masters
│   ├── style/      # 6 style frames
│   ├── sheets/     # character turnarounds
│   ├── textures/   # albedo + masks, exported PNG
│   ├── overlays/   # tileable paper / hatch
│   ├── plates/     # Act V explainer art, map, diagrams
│   └── fx/         # 2D animated PNG sequences
├── blend/
│   ├── assets/     # characters, props, sets — linked, not appended
│   ├── shots/      # one .blend per shot, links from assets/
│   └── lib/        # master materials + node groups
├── audio/          # VO, tabor stems, SFX
└── render/         # PNG sequences, one folder per shot
```

**Link, never append.** One material fix in `lib/` should propagate to every shot. Appending means fixing it 30 times.

---

## SCHEDULE (solo, part-time)

| Phase | Days | Output |
|---|---|---|
| Script lock + VO scratch | 2 | Timed animatic audio |
| Krita style frames + palette | 3 | 6 frames — **do not start Blender before this** |
| Character sheets | 4 | 5 turnarounds + expressions |
| Modelling / rigging | 8 | 5 hero characters, 4 sets |
| Krita textures + overlays | 4 | Full texture set |
| Krita plates + 2D FX | 4 | Act V plates, transitions, map |
| Layout / animatic in Blender | 4 | Full 8:08 at low quality |
| Animation | 12 | All 30 shots |
| Lighting / shading | 5 | Toon pass locked |
| Render | 3 | Mostly unattended |
| Sound + edit + grade | 4 | Master |
| **Total** | **~53 days** | |

The animatic at day 21 is the real checkpoint. If the film isn't working at animatic stage, no amount of rendering fixes it — recut before you animate.

---

## GOTCHAS

1. `Shader to RGB` is EEVEE-only. Committing to Cycles halfway means re-shading everything.
2. AgX view transform will mute your palette. Set `Standard` on day one.
3. Non-Color colour space on masks and roughness — sRGB on those is the classic washed-out bug.
4. Bake line art before final render, or triple your render time.
5. Don't unify the crowd's animation phase. Unison movement reads as a bug, not a plague.
6. Krita `.kra` files with many animation frames get large fast. Keep exported PNG sequences in git; keep `.kra` masters out (or in LFS).
7. Render PNG sequences, not video files.
8. The Act V explainer plates should look like a *different film*. Resist the urge to make them match.
