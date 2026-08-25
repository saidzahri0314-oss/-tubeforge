# Blender / Krita / GIMP / Inkscape toolchain

Everything here runs **headless on Linux with no GPU**, which is what makes it
reproducible in CI or a container.

## Install

```bash
python3 -m venv .venv-bl
.venv-bl/bin/pip install bpy pillow          # Blender 5.0 as a Python module
apt-get install -y libegl1 libgl1-mesa-dri libglx-mesa0   # software GL for EEVEE
apt-get install -y inkscape gimp krita
```

## Run

```bash
# 1. author the 2D plates + hatch tiles, then raster them (Inkscape)
python3 ../art/make_svg.py && ../art/raster.sh

# 2. paper/ink overlay plate (GIMP, Script-Fu, headless)
../art/make_paper.sh

# 3. render (Blender EEVEE, software GL)
LIBGL_ALWAYS_SOFTWARE=1 EGL_PLATFORM=surfaceless GALLIUM_DRIVER=llvmpipe \
  ../../../.venv-bl/bin/python render_shots.py 00A 05G 10A 10B \
  --out ~/renders --res 1280x720 --samples 32

# 4. comp: paper, grain, vignette, grade
../../../.venv-bl/bin/python comp.py ~/renders/*.png --out ~/renders/comp
```

## Files

| File | Role |
|---|---|
| `woodcut.py` | Palette, toon shader, line art, lights, camera, render config |
| `render_shots.py` | Geometry primitives, figure/stage assembly, the four shots |
| `comp.py` | Post: paper overlay, grain, vignette, warm grade |
| `../art/make_svg.py` | Authors hatch tiles + film plates as SVG |
| `../art/raster.sh` | Inkscape SVG → PNG |
| `../art/make_paper.sh` | GIMP → paper fibre plate |

## Notes from getting this working

- **EEVEE needs a GL context.** Without `libegl1` + software GL it dies on
  `libEGL.so.1`. Cycles works headless with no setup, but `Shader to RGB` does
  not exist in Cycles, so the toon recipe requires EEVEE.
- **GPv3 renamed the Line Art modifier's `thickness` to `radius`**, and the
  default is `0.0025` — far too thin to read. These shots use `0.016`–`0.055`.
- **Blender 5.0 moved the compositor** off `scene.node_tree`, which is why the
  paper/vignette pass lives in `comp.py` rather than in the .blend.
- **Join primitives into one mesh before rendering line art.** Otherwise every
  primitive gets its own outline and a figure reads as a stack of lumps.
- The bpy module ships a minimal OCIO config: only the `NONE` view transform is
  available. That is effectively `Standard`, which is what the pipeline wants
  anyway — AgX would have muted the palette.
- **Krita has no usable headless painting API.** It installs and can convert
  files, but the 2D authoring here is done in Inkscape (vector plates, hatch
  tiles) and GIMP (raster textures), both of which script cleanly. Open the
  `art/svg` and `art/textures` output in Krita to paint over by hand.
