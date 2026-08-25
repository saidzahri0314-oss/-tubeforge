"""Author the film's 2D plates and hatch tiles as SVG, for Inkscape to raster.

This is the Krita half of the pipeline expressed in vector form: hatch tiles
that become image textures on the Blender toon shader, and finished plates
that cut straight into the edit.

    python3 make_svg.py && ./raster.sh
"""

import math, os, random

PARCHMENT, INK, OCHRE, RED = '#E8DCC0', '#1A1614', '#B07D3A', '#C42B1C'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg')


def write(name, body, w, h, bg='none'):
    os.makedirs(OUT, exist_ok=True)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}">\n'
           + (f'  <rect width="{w}" height="{h}" fill="{bg}"/>\n' if bg != 'none' else '')
           + body + '\n</svg>\n')
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(svg)
    print('svg:', name)


# ---------------------------------------------------------------- hatch tiles
def hatch(name, size=512, spacing=13, width=3.0, angle=38, cross=False,
          jitter=0.55, seed=7):
    """A seamless-ish engraving hatch. Jitter keeps it from reading as CG."""
    rnd = random.Random(seed)
    parts = [f'  <rect width="{size}" height="{size}" fill="#ffffff"/>']
    for pass_i, ang in enumerate([angle] + ([angle + 84] if cross else [])):
        a = math.radians(ang)
        dx, dy = math.cos(a), math.sin(a)
        span = size * 2
        n = int(span / spacing)
        for i in range(-n, n * 2):
            off = i * spacing + rnd.uniform(-jitter, jitter)
            # line through a point offset perpendicular to direction
            px, py = -dy * off + size / 2, dx * off + size / 2
            x1, y1 = px - dx * span, py - dy * span
            x2, y2 = px + dx * span, py + dy * span
            w = width * rnd.uniform(0.72, 1.28)
            parts.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" '
                         f'y2="{y2:.1f}" stroke="#000000" stroke-width="{w:.2f}" '
                         f'stroke-linecap="round"/>')
    write(name, '\n'.join(parts), size, size)


# --------------------------------------------------------- shot 03C: humours
def humours_wheel(size=1400):
    c = size / 2
    R = size * 0.36
    quads = [('BLOOD', RED, -90), ('YELLOW BILE', OCHRE, 0),
             ('BLACK BILE', INK, 90), ('PHLEGM', '#8B9A93', 180)]
    p = [f'  <rect width="{size}" height="{size}" fill="{PARCHMENT}"/>']

    for label, col, rot in quads:
        a0, a1 = math.radians(rot - 45), math.radians(rot + 45)
        x0, y0 = c + R * math.cos(a0), c + R * math.sin(a0)
        x1, y1 = c + R * math.cos(a1), c + R * math.sin(a1)
        p.append(f'  <path d="M {c} {c} L {x0:.1f} {y0:.1f} '
                 f'A {R} {R} 0 0 1 {x1:.1f} {y1:.1f} Z" fill="{col}" '
                 f'fill-opacity="{0.92 if label == "BLOOD" else 0.34}" '
                 f'stroke="{INK}" stroke-width="5"/>')
        am = math.radians(rot)
        lx, ly = c + R * 0.66 * math.cos(am), c + R * 0.66 * math.sin(am)
        fill = PARCHMENT if label == 'BLOOD' else INK
        p.append(f'  <text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" '
                 f'font-family="Georgia, serif" font-size="{size*0.038:.0f}" '
                 f'letter-spacing="2" fill="{fill}">{label}</text>')

    p.append(f'  <circle cx="{c}" cy="{c}" r="{R}" fill="none" stroke="{INK}" stroke-width="9"/>')
    p.append(f'  <circle cx="{c}" cy="{c}" r="{R*0.135:.0f}" fill="{PARCHMENT}" '
             f'stroke="{INK}" stroke-width="6"/>')
    # the overflow: blood spilling past the rim, per shot 03C
    for i in range(9):
        a = math.radians(-90 + (i - 4) * 7)
        r0, r1 = R * 0.99, R * (1.10 + 0.16 * math.cos(i))
        p.append(f'  <path d="M {c + r0*math.cos(a):.1f} {c + r0*math.sin(a):.1f} '
                 f'L {c + r1*math.cos(a):.1f} {c + r1*math.sin(a):.1f}" '
                 f'stroke="{RED}" stroke-width="{7 - i%3}" stroke-linecap="round"/>')
    p.append(f'  <text x="{c}" y="{size*0.945:.0f}" text-anchor="middle" '
             f'font-family="Georgia, serif" font-style="italic" '
             f'font-size="{size*0.034:.0f}" fill="{INK}">The four humours &#8212; '
             f'too much blood, overheated</text>')
    write('03C_humours_wheel.svg', '\n'.join(p), size, size)


# ------------------------------------------------------------ shot 01C: title
def title_card(w=1920, h=1080):
    p = [f'  <rect width="{w}" height="{h}" fill="{RED}"/>',
         f'  <rect width="{w}" height="{h}" fill="{PARCHMENT}" mask="url(#cut)"/>']
    defs = [
        '  <defs>',
        '    <mask id="cut">',
        f'      <rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'      <text x="{w/2}" y="{h*0.47:.0f}" text-anchor="middle" '
        f'font-family="Georgia, serif" font-weight="bold" font-size="{h*0.155:.0f}" '
        f'letter-spacing="6" fill="#000000">THE DANCING</text>',
        f'      <text x="{w/2}" y="{h*0.645:.0f}" text-anchor="middle" '
        f'font-family="Georgia, serif" font-weight="bold" font-size="{h*0.155:.0f}" '
        f'letter-spacing="6" fill="#000000">PLAGUE</text>',
        '    </mask>',
        '  </defs>']
    p.append(f'  <text x="{w/2}" y="{h*0.795:.0f}" text-anchor="middle" '
             f'font-family="Georgia, serif" font-size="{h*0.058:.0f}" '
             f'letter-spacing="16" fill="{INK}">STRASBOURG &#183; 1518</text>')
    write('01C_title_card.svg', '\n'.join(defs + p), w, h)


if __name__ == '__main__':
    hatch('hatch_fine.svg',   spacing=9,  width=2.2, angle=38)
    hatch('hatch_medium.svg', spacing=15, width=3.4, angle=38)
    hatch('hatch_cross.svg',  spacing=17, width=3.2, angle=34, cross=True)
    humours_wheel()
    title_card()
