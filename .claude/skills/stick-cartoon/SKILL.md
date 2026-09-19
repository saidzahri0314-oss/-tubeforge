---
name: stick-cartoon
description: >-
  Draw frames in the flat stick-figure cartoon style — a flat grey world, one
  wobbly black ink weight, five flat colours, no gradients, shadows or texture.
  Use this whenever the task involves art in this look: a scene, a character, a
  thumbnail, a storyboard panel, an explainer plate, a title card. Use it when
  asked to copy, redraw, match or extend a reference frame drawn this way, and
  when asked to measure a reference image's palette and geometry before
  redrawing it — the measurement recipe here is what keeps a copy honest. Also
  use it when someone mentions the style lab, "stick figure style", "that
  cartoon style", or points at scripts/style-lab. Reach for it even when the
  style is not named: if the request is a simple cartoon frame for a video in
  this repo, this is the default look.
---

# Stick-figure cartoon

A flat two-tone world with stick people in it. The whole look is three moves:
**flat fill, one wobbly black contour, nothing else.** No gradients, no soft
shadows, no photographic texture, no 3D. That restraint is what makes it cheap
to produce and why it survives being generated from code.

The thing that makes it *funny* rather than merely cheap is the **effort gap**:
everything in frame is drawn at minimum effort — a face is four marks — except
one element rendered at maximum effort. In the source frame, two stick figures
with 4-mark faces torture a third whose face has thirty wrinkles, ringed eyes,
teeth, gums and a tongue. Copy the palette and the wobble and you are most of
the way there; copy the effort gap and you are done. If a frame feels flat in
the wrong way, it is usually because everything got the same amount of care.

`assets/sample-frame.png` is the reference output. Match it.

## The spec

All measured off the source frame at 1636×980. Lengths and stroke weights scale
with the canvas *dimension*; fleck count scales with its *area*. Mixing those up
is easy and over-flecks a small canvas, so the fleck row below is given as a
density rather than a count.

| | Value |
|---|---|
| Wall / sky | `#747474` — 53% of all pixels |
| Ground | `#8a8788` — 27% |
| Heads, teeth | `#ffffff` |
| Wood | `#766c56` |
| Rope | `#a2a272` |
| Hair | `#897c6c` |
| Mouth throat / gums | `#653737` / `#865455` |
| Ink | `#000000` |
| Horizon | a **soft colour change with no line**, gently wavy, ~68% down the frame |
| Contour weight | 5px (heads, limbs) |
| Wood and rope edges | 4px |
| Interior detail | 2.6px |
| Background flecks | **~56 per megapixel** (90 on a 1636×980 frame), median 6px long, p90 16px, max 37px, ~2.5px wide |

Five colours carry 85% of the frame. Adding a sixth is almost always a mistake —
if something needs to separate from its background, change its value, not its hue.

The flecks matter more than they look. They are the only texture in the frame and
they read as grain; without them the wall is dead, and with too many it becomes a
snowstorm. Skew them small — `3 + 30 * random() ** 2.6` gives the measured
distribution, where a flat random draw over the same range looks wrong. Thin them
out over the ground, which is cleaner than the wall.

## Drawing

`scripts/stickstyle.py` is the engine. Import `Pen` and compose with it; do not
hand-write SVG path data, because the wobble is the point and it needs to come
from one place.

```python
import sys, os
sys.path.insert(0, ".claude/skills/stick-cartoon/scripts")
from stickstyle import Pen, PALETTE, oval, W_OUTLINE, W_EDGE, W_DETAIL

p = Pen(seed=1518)                      # seeded: same seed redraws the same frame
p.add('<path d="%s L 1636 980 L 0 980 Z" fill="%s"/>'
      % (p.path_d(horizon_pts, amp=1.4, step=120), PALETTE["ground"]))
p.speck(x, y, length, angle)            # one background fleck
p.shape(pts, PALETTE["skin"], w=W_OUTLINE)   # flat fill + ink contour, one path
p.stroke(pts, w=W_OUTLINE)              # a limb
p.plank(a, b, w0, w1, tip=26)           # tapered beam, optional sharpened end
p.coil(a, b, turns, girth)              # rope wound round a bar
p.cord(pts, w=9)                        # rope as a stroke: ink underlay + colour
open("out.svg", "w").write(p.svg(1636, 980, background=PALETTE["wall"]))
```

`shape()` draws fill and contour from a single path, so they can never drift
apart — that is why it exists rather than you stroking and filling separately.

**How the wobble works**, since it is the one non-obvious part. Every mark is
resampled every ~36px, each sample is displaced along its local normal by
`sin(i·freq + phase) · amp` plus a little noise, and a Catmull-Rom spline runs
through the result. Sample spacing sets the wavelength and is the knob that
matters most. Low frequency reads as *drawn*; high frequency reads as *shaky*,
which is a different and worse look. Amplitude runs 1–2.5px — past about 4px it
stops looking hand-drawn and starts looking melted.

Sharp corners need two points a few px apart, not one. A single vertex gets
rounded away by the spline and comes out a blob.

## Rendering

No `rsvg`, ImageMagick or Inkscape in this container, but Chromium is installed
for Playwright and renders SVG correctly:

```bash
NODE_PATH=/opt/node22/lib/node_modules node .claude/skills/stick-cartoon/scripts/render.cjs \
  "$PWD/out.svg" "$PWD/out.png" 1636 980
# trailing arg is deviceScaleFactor — 2.348 gives 4K from the same source
```

Output is vector, so one SVG serves both a thumbnail and a 4K plate.

## Matching a new reference

When copying a frame rather than inventing one, measure it — do not eyeball it.
Eyeballing gets the palette roughly right and the geometry quietly wrong, and the
errors only show up once the drawing is finished. With Pillow:

1. **Palette** — histogram the whole image. In a style this flat, the top 5
   colours are the palette, and their percentages tell you the composition.
2. **Geometry** — mask on each flat colour and take per-row extents. That
   recovers edges, widths and angles far more precisely than looking.
3. **Flecks** — connected-component count in a clean patch of background, then
   scale to the frame. Record median and p90 length, not just the range.
4. **Stroke weights** — scan one row across an edge and print the colour runs.
   You get the contour width and the fill width directly.
5. **Check your work with a diff, not with your eyes.** Re-measure your own
   render the same way and compare row by row against the original. A composite
   at full scale hides errors that a width table makes obvious immediately.

## Traps

These each cost a rewrite, so they are worth reading before starting.

**Masking gives you geometry, not meaning.** It tells you where a line is, never
what it *is*. In the source frame the tortured figure's arms and legs were read
as rope, so he came out a head on a string — every line roughly in the right
place and the drawing still wrong. Before trusting a mask, crop the confusing
region at 3x and *look* at it. Structure questions ("is this a limb or a rope?",
"where do these lines converge?") are answered by zooming, not by measuring.

**Do not confuse outer edges with centre lines.** Reading measured edge positions
as centre lines splayed the ladder 70px too wide and survived several rounds of
visual comparison. Write down which one each number is when you record it.

**Detail is a budget, not a finish.** Resist levelling everything up. If the
second-most-detailed thing in the frame is close to the most-detailed thing, the
effort gap is gone and the joke goes with it.

## What is here

```
SKILL.md                    this
scripts/stickstyle.py       the engine — Pen, palette, wobble, coils, flecks
scripts/render.cjs          SVG -> PNG via headless Chromium
assets/sample-frame.png     the reference output to match
```

A full worked scene lives at `scripts/style-lab/scene_ladder.py`, with notes in
`scripts/style-lab/README.md` including the open-source hand-drawing and
animation tools that produce this look (Krita, Inkscape, Blender Grease Pencil,
Synfig, OpenToonz, Pencil2D, Glaxnimate). Read the scene when you need an example
of how the primitives compose into a full frame.
