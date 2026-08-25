"""Post-comp for the Dancing Plague frames: paper, grain, vignette, grade.

The pipeline puts a Krita-painted paper plate over the render in Blender's
compositor. Blender 5.0 moved the compositor off `scene.node_tree`, and there
is no Krita in this environment, so the same job is done here in Pillow:
procedural paper fibre + ink bleed, an overlay mix, a vignette, and a small
warm grade.

    python comp.py IN.png [more.png ...] --out DIR
"""

import argparse, math, os, random
from PIL import Image, ImageChops, ImageDraw, ImageFilter


GIMP_PAPER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          'art', 'textures', 'paper_fibre.png')


def paper_plate(size, seed=1518):
    """Prefer the GIMP-authored plate; fall back to procedural fibre."""
    if os.path.exists(GIMP_PAPER):
        return Image.open(GIMP_PAPER).convert('L').resize(size, Image.BICUBIC)
    return _procedural_paper(size, seed)


def _procedural_paper(size, seed=1518):
    """Tileable-ish paper: fine fibre noise + a few long fibres + blotches."""
    w, h = size
    rnd = random.Random(seed)
    # fine fibre only -- coarse noise reads as video grain, not paper
    paper = Image.effect_noise(size, 8).filter(ImageFilter.GaussianBlur(0.35))
    broad = Image.effect_noise((max(2, w // 12), max(2, h // 12)), 10) \
                 .resize(size, Image.BICUBIC).filter(ImageFilter.GaussianBlur(5))
    paper = ImageChops.blend(paper, broad, 0.30)

    d = ImageDraw.Draw(paper)
    for _ in range(int(w * h / 26000)):           # sparse long fibres
        x, y = rnd.randrange(w), rnd.randrange(h)
        a = rnd.uniform(0, math.pi)
        ln = rnd.randint(18, 90)
        v = rnd.randint(118, 146)
        d.line([x, y, x + math.cos(a) * ln, y + math.sin(a) * ln], fill=v, width=1)
    return paper.filter(ImageFilter.GaussianBlur(0.5))


def vignette(size, strength=0.22):
    w, h = size
    m = Image.new('L', (w, h), 0)
    d = ImageDraw.Draw(m)
    steps = 48
    for i in range(steps):
        f = i / steps
        v = int(255 * (1 - strength * (f ** 2.1)))
        inset_x, inset_y = int(w * 0.5 * f * 0.86), int(h * 0.5 * f * 0.86)
        d.ellipse([-w * 0.18 + inset_x, -h * 0.30 + inset_y,
                   w * 1.18 - inset_x, h * 1.30 - inset_y], fill=v)
    return m.filter(ImageFilter.GaussianBlur(w / 44))


def overlay(base, top, opacity):
    """Photoshop-style overlay blend, mixed back by opacity."""
    b = base.convert('RGB')
    t = top.convert('L').convert('RGB')
    lo = ImageChops.multiply(b, t)
    hi = ImageChops.screen(b, t)
    mask = t.convert('L').point(lambda v: 255 if v > 128 else 0)
    blended = Image.composite(hi, lo, mask)
    return Image.blend(b, blended, opacity)


def grade(img, warm=(1.015, 1.0, 0.965), lift=4):
    r, g, b = img.convert('RGB').split()
    r = r.point(lambda v: min(255, int(v * warm[0]) + lift))
    g = g.point(lambda v: min(255, int(v * warm[1]) + lift))
    b = b.point(lambda v: min(255, int(v * warm[2])))
    return Image.merge('RGB', (r, g, b))


def comp_frame(path, out_dir, paper_opacity=0.10, seed=1518):
    img = Image.open(path).convert('RGB')
    img = grade(img)
    img = overlay(img, paper_plate(img.size, seed), paper_opacity)
    img = Image.composite(img, Image.new('RGB', img.size, (14, 11, 10)),
                          vignette(img.size))
    grain = Image.effect_noise(img.size, 5).convert('RGB')
    img = Image.blend(img, ImageChops.overlay(img, grain), 0.045)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, os.path.basename(path).replace('.png', '_comp.png'))
    img.save(dst)
    return dst


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('frames', nargs='+')
    ap.add_argument('--out', default='/home/user/renders/comp')
    ap.add_argument('--paper', type=float, default=0.10)
    a = ap.parse_args()
    for i, f in enumerate(a.frames):
        print('>>', comp_frame(f, a.out, a.paper, seed=1518 + i * 7))
