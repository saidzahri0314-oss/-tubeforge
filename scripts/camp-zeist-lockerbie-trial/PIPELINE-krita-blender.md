# PRODUCTION PIPELINE — Krita → Blender

**Target:** 11:10, 3840×2160, 24 fps, stylized 3D in a courtroom-sketch look. 11 sequences, 74 shots.

## What carries over from *Dancing Plague*

This package uses the same toolchain as `../dancing-plague-1518/PIPELINE-krita-blender.md`. These sections apply **unchanged** and are not repeated here:

- the Krita/Blender split (Krita owns every drawn pixel, Blender owns everything built and lit),
- §1.3 the UV → Krita → Blender texture round trip, including sRGB vs Non-Color,
- §2.1 modelling from reference sheets,
- §2.3 Grease Pencil Line Art setup and baking,
- §2.6 compositor chain and §2.7 render settings (**View Transform `Standard`**, PNG sequences, encode afterwards).

Everything below either replaces or adds to that document.

---

## GROUND RULES — read before you draw anything

This film is about a real bombing that killed 270 people, and the families are still alive and still arguing. The cartoon pipeline has to bend in a few places. These rules aren't up for negotiation shot by shot:

1. **No victim is ever depicted.** No passengers, no crew, no Sherwood Crescent residents. Not even as silhouettes in the aircraft. `02A` shows anonymous travellers *at the gate*. `02B` shows empty lit windows.
2. **The explosion is never shown.** It happens off screen, between two radar sweeps (`02C`). No fireball, no falling wreckage, no impact. `02D` cuts **before** anything happens.
3. **No bodies, no remains, no blood**, anywhere in the film.
4. **Real people get courtroom-sketch likenesses, not cartoon caricatures.** Recognisable, accurate, and unexaggerated. This is the one place the "cartoon" brief gives way completely.
5. **People who are alive and were never convicted are handled with care.** Fhimah was acquitted, so he is drawn exactly like everyone else in the dock and never framed or lit as sinister. Mas'ud has not been tried, so he appears **from behind only** (`09B`), and every caption about him uses *accused* / *alleged*. Dr Jim Swire appears **as a name caption only**, with no likeness.
6. **No trademarks on screen.** Pan Am, Libyan Arab Airlines, Toshiba, Samsonite, Syracuse University: the VO can name them, but the picture shows plain text or generic shapes. No globe logo, no tail livery.
7. **Quotes on screen are verbatim** and match `SOURCES.md` character for character. If you shorten one, use an ellipsis and say so in `SOURCES.md`.

---

## STYLE BIBLE

**"Courtroom Pastel."** British courts have kept cameras out for most of their history, so the public has usually seen trials the way courtroom artists drew them. The whole film looks as if one of those artists drew it from the public gallery. Toned paper, pastel and conté strokes, loose construction lines left in, and highlights picked out in chalk. The 3D does the staging. The look says *witness*, not *cartoon*.

**Palette — 4 base colours + 1 rationed:**

| Token | Hex | Use |
|---|---|---|
| Slate paper | `#56626C` | Base / toned paper / the shadow side of everything |
| Chalk | `#ECE6DA` | Light, highlights, all on-screen text |
| Charcoal | `#1F2226` | Line, deep shadow, silhouettes |
| Sanguine | `#B9805F` | Skin, wood panelling, Maltese limestone. The warm midtone |
| **Christmas gold** | `#E6B23A` | **Rationed.** See below. |

The judges' red crosses are Sanguine pushed darker (`#8E4A3A`), not a new hue. They should never compete with the gold.

**Gold is the story.** The case turned on whether some Christmas lights were up, so gold means *light someone might have to testify about*. Track it deliberately:

| Where | Gold |
|---|---|
| Cold open | One window, `00A` / `00G`. A few hundred pixels |
| Act I | Lockerbie's window lights in `02D`. Then gone for the rest of the act |
| Act II | Only on the fragment's traces, `03G` |
| Act III | **None.** The stalemate years have no gold at all |
| Act IV | The court's windows at nightfall, last frames of `05A` |
| Act V | **None** |
| Act VI | **Dominant.** Sliema's lights fill the frame (`07B`–`07H`) |
| Act VII | **None.** Not on the reward envelope. Putting gold on money would be an editorial claim, and the film doesn't make it |
| Act VIII | **None.** Modern palette |
| Close | The lights alone on black, flickering, cut mid-flicker |

**Colour script by act:** night slate → chalk-on-slate title → night blue with gold windows, then frost-grey dawn → wet grey-green hills and **clinical white evidence plates** → cold archival slate and typed-paper beige → fluorescent institutional green-white → the same, harsher → **warm Maltese dusk** → faded and overexposed → **desaturated modern digital (Act VIII)** → night slate, gold.

---

## STAGE 1 — KRITA

Work at **3840×2160, 300 dpi, sRGB, 16-bit**, as in *Dancing Plague*.

### 1.1 Style frames (do this first, do not skip)
Paint **eight** frames, one per colour world, before any model is built:

| # | Frame | Proves |
|---|---|---|
| 1 | `00A` the fence and the gold window | Night slate, gold ration at its smallest |
| 2 | `02D` Lockerbie from the hillside | Restraint: how much can a still, quiet frame carry |
| 3 | `03C` evidence plate | The clinical white "second medium" |
| 4 | `05F` the courtroom in session | Hero set, all likenesses, fluorescent palette |
| 5 | `06E` the judgment plate | Typography on paper. Font, size, line-lighting style |
| 6 | `07B` Sliema at dusk | Gold at full strength, sanguine limestone |
| 7 | `08E` Tripoli, overexposed | The faded act |
| 8 | `09A` Washington courthouse | The modern, desaturated library |

Deliver as `art/style/0X_styleframe.png`.

### 1.2 Character sheets
Most characters here sit down, so most rigs only need the upper body.

| Character | Rig | Likeness | Notes |
|---|---|---|---|
| Presiding judge + 2 judges + additional judge | Upper body, shared robe/wig rig, 4 heads | Courtroom-sketch | White robes with red crosses and short wigs. **Work from photos of the verdict day, not from English court dramas** |
| Megrahi | Upper body | Courtroom-sketch | Two age states: 2000–01 and 2009 (`08D`) |
| Fhimah | Upper body | Courtroom-sketch | See ground rule 5 |
| Tony Gauci | Full body | Courtroom-sketch, warm | Shop-counter acting only |
| Robert Black | Upper body | Courtroom-sketch | One scene (`04E`) |
| Counsel ×4, macer, interpreters | Upper body | Generic | Don't attempt real likenesses for unnamed people |
| Police officer, searcher, traveller | Full body | Generic | The searcher is instanced (see 2.5) |

Export front and side views separately at identical pixel height, as in *Dancing Plague* §1.2.

### 1.3 Brushes and paper
- Build one **Pastel** and one **Conté** preset from Krita's chalk/charcoal presets (Brush Presets docker → filter `chalk` / `charcoal`). In the Brush Editor, enable **Texture** and load a toned-paper pattern so the paper grain catches every stroke. That grain is what makes this look like pastel instead of a digital airbrush.
- Paint textures with these two presets only. Two tools make one hand. Five tools look like a committee.

### 1.4 Overlay plates
Tileable 4K, into `art/overlays/`: toned-paper tooth (honeycomb Mi-Teintes texture), loose pastel dust, finger smudge, fixative spatter. They go into the **compositor**, as before.

### 1.5 The "drawn-in" reveal
Several shots (`00C`, `00E`, `04A`, `05F`) show a figure being **sketched into existence**. This is a Krita animation used as a **mask** on a Blender render, not a Blender effect:

1. Render the Blender shot normally.
2. In Krita, over a still of the final frame, animate white-on-black **strokes** that gradually cover the figure, like an artist blocking it in. Work on 2s (12 drawings per second).
3. `File → Render Animation → PNG Image Sequence` → `fx_reveal_<shot>_####.png`.
4. In the Blender compositor: `Mix (Factor ← reveal sequence)`, with the bare paper plate in the top input and the render in the bottom. The render shows through only where the strokes have been drawn.

### 1.6 Plates
**24 pure-Krita shots** (`K`): `01A`–`01C`, `02E`, `02F`, `03C`, `03H`, `04A`, `04C`, `04D`, `04F`, `05C`, `05D`, `06E`, `06F`, `07A`, `07D`, `07G`, `08A`, `08F`, `08G`, `09B`–`09D`.
**7 more start in Krita and finish in Blender** (`K → B`): `00F`, `00G`, `02C`, `02H`, `03F`, `05G`, `08B`.
That's over 40% of the film, so budget for it (see Schedule).

They come in three deliberately different families, and the families should **not** match each other:

| Family | Look | Shots |
|---|---|---|
| **Evidence** | White paper, thin technical line, one charcoal weight | `03C`, `03H`, `07D` |
| **Documents** | Typeset text on cream paper, lit line by line in chalk white | `05C`, `06E`, `07G`, `08A`, `08G`, `09C`, `09D` |
| **Maps & ledgers** | Chalk on slate, hand-lettered | everything else |

**Typesetting quotes:** pick one serif face for every document plate and never change it. The lit-line effect is a mask animated in Krita, as in §1.5.

---

## STAGE 2 — BLENDER

**Blender 4.2 LTS or newer** (EEVEE Next). As before, check Grease Pencil panel names if you're on 4.3+ (GPv3).

### 2.1 Shader — changes from the *Dancing Plague* toon recipe
Start from `../dancing-plague-1518/PIPELINE-krita-blender.md` §2.2, then:

- **Two ColorRamp stops, not three** (Slate paper / Sanguine or Chalk). Pastel sketches have fewer value steps than cel animation.
- Multiply a Krita-painted **pastel stroke** texture over the ramp in **object or UV space, never screen space.** Screen-space texture "swims" when the camera moves (the shower-door effect).
- Make the strokes **boil** like hand-drawn animation: offset the stroke texture's Mapping node once every two frames. Add a driver on the Mapping node's *Location X*:

  ```
  fmod(floor(frame / 2) * 0.37, 1.0)
  ```

  Stepping on 2s matches the Krita FX. A smooth per-frame offset looks like video noise, not drawing.

### 2.2 Line art — changes
- Thinner overall than *Dancing Plague*. Contour plus Crease only. Turn **Intersection off**, because courtroom furniture throws dozens of fussy intersection lines.
- Give the Line Art object a stroke material with **Style: Texture** using a chalk-stroke image, so the lines read as conté, not ink.
- Animate the **Noise** modifier's seed on 2s for the same boil as 2.1.

### 2.3 Sets — build in this order

| Set | Shots | Priority |
|---|---|---|
| **Camp Zeist courtroom** (bench, dock, counsel tables, interpreters' booth, glass-fronted gallery) | ~20 | **Hero.** Most of the budget goes here |
| Camp Zeist exterior (pines, fence, barrier, low blocks) | `00A`, `00B`, `05A`, `05E`, `06D`, `10A` | High |
| Sliema street + Mary's House shopfront | `03E`, `07B`, `07C`, `07E`, `07H` | High. Also built as a **miniature** for `07H` |
| Evidence table / photo table | `03B`, `07F`, `07H` | Medium |
| Lockerbie hillside, frosted field | `02D`, `02G`, `03A` | Medium. Matte painting plus a few 3D layers is enough |
| Departure gate, airfield, Tripoli aircraft door | `02A`, `04H`, `08E` | Low. Silhouette-driven |
| Washington courthouse, 2022 tents | `09A`, `10A` | Low, but uses the **modern library** (2.7) |

**Courtroom reference:** use the published photographs of the Camp Zeist courtroom. The court was built for a trial without a jury, so check the photos before dressing in a jury box. Don't add a gavel (Scottish courts don't use them), and don't borrow the layout of an English Crown Court.

### 2.4 Cameras
Courts run on procedure, so the camera does too. **Nothing handheld in this film.** Locked-off or slow mechanical moves only.

- 35 mm for the courtroom, 85 mm for dock and bench close-ups, 135 mm for the "news camera" long-lens shots (`02B`, `03A`, `04H`, `08E`).
- **Matched framings are part of the script.** Build each pair as one camera duplicated across shot files, never by eye: `00B`↔`05E`, `00C`↔`10B`, `03E`↔`07E`, `06G`↔`08I`, `07B`↔`07C`↔`07H`.

### 2.5 The search line (`03A`) — the film's only crowd
About 80 searchers in one line. Use linked duplicates of one walk-cycle rig with phase offsets so they don't step in unison:

```python
import bpy, random
random.seed(1988)
for ob in bpy.context.selected_objects:
    ad = ob.animation_data
    if not ad:
        continue
    for track in ad.nla_tracks:
        for strip in track.strips:
            strip.frame_start_ui += random.randint(0, 23)  # up to 1 s of phase spread @ 24 fps
            strip.repeat = 12
```

Silhouettes only, so no hue variation is needed. Vary **height** by ±4% instead (`ob.scale *= random.uniform(0.96, 1.04)`).

### 2.6 The toggle shot (`07C`)
The Sliema lights have to **snap** between off and on, never fade. Drive every bulb from one scene property and key it with constant interpolation:

```python
import bpy

scene = bpy.context.scene
scene["lights_on"] = 0.0

# Every bulb uses the "XmasBulb" material; drive its emission from the scene property.
mat = bpy.data.materials["XmasBulb"]
strength = mat.node_tree.nodes["Emission"].inputs["Strength"]
drv = strength.driver_add("default_value").driver
drv.type = 'SCRIPTED'
var = drv.variables.new()
var.name = "on"
var.targets[0].id_type = 'SCENE'
var.targets[0].id = scene
var.targets[0].data_path = '["lights_on"]'
drv.expression = "on * 12.0"

# Key the flips with constant interpolation (frames = caption changes in the edit).
prefs = bpy.context.preferences.edit
old = prefs.keyframe_new_interpolation_type
prefs.keyframe_new_interpolation_type = 'CONSTANT'
for frame, on in [(1, 0), (31, 1), (61, 0), (91, 1), (121, 0), (151, 1)]:
    scene["lights_on"] = float(on)
    scene.keyframe_insert(data_path='["lights_on"]', frame=frame)
prefs.keyframe_new_interpolation_type = old
```

Add the celesta hit on the same frames in the edit (see Audio Design in `SCRIPT.md`). EEVEE Next has no Bloom checkbox any more. For the bulb glow, add a **Glare** node (type **Bloom**) in the compositor.

The same rig drives `10D`. Key the last flip **on the cut frame**, so the film ends mid-flicker.

### 2.7 Act VIII and the Close — the modern library
As with the 1962 sequence in *Dancing Plague*: keep a separate material library for the present-day shots (`09A`, `10A`). That means three-stop ramp, no stroke texture, no boil, and **no paper overlay** in the compositor. The present should look like a different, flatter world. Otherwise the film stops feeling like it's moving from history into news.

### 2.8 Render settings
Same as *Dancing Plague* §2.7, plus the compositor Glare node from 2.6. Motion blur **off**. Pastel strokes smeared by motion blur read as a rendering error.

---

## FOLDER STRUCTURE

```
camp-zeist-lockerbie-trial/
├── README.md
├── SCRIPT.md
├── PIPELINE-krita-blender.md
├── SOURCES.md
├── art/            # Krita — .kra masters
│   ├── style/      # 8 style frames
│   ├── sheets/     # likeness sheets + generic turnarounds
│   ├── textures/   # pastel albedo + stroke textures
│   ├── overlays/   # toned paper / dust / smudge
│   ├── plates/     # evidence / documents / maps (three families)
│   └── fx/         # reveal masks, lit-line masks
├── blend/
│   ├── assets/     # characters, props, sets — linked, not appended
│   ├── shots/      # one .blend per shot
│   └── lib/        # sketch library + modern library, node groups
├── audio/          # VO, drone, celesta, room tones
└── render/         # PNG sequences, one folder per shot
```

---

## SCHEDULE (solo, part-time)

| Phase | Days | Output |
|---|---|---|
| Script lock + VO scratch | 2 | Timed animatic audio |
| Krita style frames + palette | 4 | 8 frames. **Do not start Blender before this** |
| Likeness + character sheets | 5 | 8 likenesses, 4 generic sheets |
| Modelling / rigging | 6 | Mostly upper-body rigs |
| Sets | 6 | Courtroom (hero) + 6 secondary sets |
| Krita textures + overlays | 3 | Pastel/stroke texture set |
| **Krita plates + 2D FX** | **8** | 24 plates + 7 hybrid shots, reveal and lit-line masks |
| Layout / animatic in Blender | 4 | Full 11:10 at low quality |
| Animation | 8 | Courtroom acting is small and still |
| Lighting / shading | 4 | Sketch pass locked |
| Render | 3 | Mostly unattended |
| Sound + edit + grade | 4 | Master |
| **Total** | **~57 days** | |

Compared with *Dancing Plague*, crowd animation drops and plate work grows. As before, the **animatic is the real checkpoint** (around day 38). If the radar shot and the toggle shot don't land in the animatic, rendering won't save them.

---

## GOTCHAS

1. **No gavels.** Scottish courts don't use them. Neither do English ones. Someone in the comments will notice.
2. **Robes:** Scottish High Court judges on the criminal bench wear white robes with red crosses. English red robes are a different court in a different country. Confirm against verdict-day photos.
3. **Jury box:** there was no jury, so don't assume the room had a jury box. The ghost chairs in `05G` are a plate, not set dressing.
4. Screen-space textures swim. Use object or UV space with the 2s boil (2.1).
5. `07C` must use **constant** interpolation. One fade and the film's central image turns into a dimmer switch.
6. AgX will mute the gold, and the gold *is* the story. `Standard` from day one.
7. No logos (ground rule 6). That includes the tail of the aircraft in `02G`. Silhouette and plain metal only.
8. Act VIII captions say *accused*, *alleged* and *pleaded not guilty*. Don't let an editor "tidy" them into *the bomb-maker*.
9. Re-record the last VO line of Act VIII on recording day if the trial date has moved, and check it again on publish day (`SOURCES.md` → *Before you publish*).
10. Keep `.kra` masters out of git (or in LFS). Commit exported PNGs.
