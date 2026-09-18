#!/usr/bin/env python3
"""
stickstyle.py — hand-drawn-stroke SVG engine for the flat stick-figure cartoon look.

Every mark in this style is the same three moves:
    flat fill  +  wobbly black outline  +  no gradient, no shadow, no texture.

So the engine only has to do one interesting thing: take a polyline, resample it,
push each sample off the line by a little low-frequency noise, and run a
Catmull-Rom spline through the result. That is what makes a straight edge read as
drawn instead of ruled — and it is the whole difference between this look and
clip art.

Seeded, so the same seed redraws the same frame (needed if you ever animate it).
"""

import math
import random

# Sampled straight off the reference frame — five colours cover 85% of the image.
PALETTE = {
    "wall":   "#747474",   # 53.1% of pixels
    "ground": "#8a8788",   # 27.2%
    "skin":   "#ffffff",   # heads
    "wood":   "#766c56",   # ladder
    "rope":   "#a2a272",   # lashings
    "hair":   "#897c6c",
    "mouth":  "#633839",
    "ink":    "#000000",
}

# Line weights, also measured off the reference.
W_OUTLINE = 5.0   # head / limb contours
W_EDGE    = 4.0   # wood and rope edges
W_DETAIL  = 2.6   # face lines, wrinkles, wood grain


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def oval(cx, cy, rx, ry, rot=0.0, n=40, a0=0.0, a1=math.tau):
    """Point list on an ellipse. Partial arcs via a0/a1 (radians)."""
    c, s = math.cos(rot), math.sin(rot)
    pts = []
    for i in range(n + 1):
        a = a0 + (a1 - a0) * i / n
        x, y = rx * math.cos(a), ry * math.sin(a)
        pts.append((cx + x * c - y * s, cy + x * s + y * c))
    return pts


class Pen:
    def __init__(self, seed=1518):
        self.rng = random.Random(seed)
        self.parts = []

    # ---------------------------------------------------------------- noise

    def _resample(self, pts, step):
        out = [pts[0]]
        carry = 0.0
        for a, b in zip(pts, pts[1:]):
            dx, dy = b[0] - a[0], b[1] - a[1]
            L = math.hypot(dx, dy)
            if L < 1e-9:
                continue
            d = step - carry
            while d <= L:
                out.append((a[0] + dx * d / L, a[1] + dy * d / L))
                d += step
            carry = L - (d - step)
        if math.dist(out[-1], pts[-1]) > 1e-6:
            out.append(pts[-1])
        return out

    def _jitter(self, pts, amp, closed):
        """Displace along the local normal. Low frequency = a drawn line;
        high frequency = a shaky line. This style wants low."""
        n = len(pts)
        phase = self.rng.uniform(0, math.tau)
        freq = self.rng.uniform(0.30, 0.65)
        out = []
        for i, p in enumerate(pts):
            a = pts[(i - 1) % n] if closed else pts[max(0, i - 1)]
            b = pts[(i + 1) % n] if closed else pts[min(n - 1, i + 1)]
            dx, dy = b[0] - a[0], b[1] - a[1]
            L = math.hypot(dx, dy) or 1.0
            nx, ny = -dy / L, dx / L
            k = math.sin(i * freq + phase) * 0.62 + self.rng.uniform(-0.5, 0.5)
            # let the ends drift too on closed shapes, hold them on open ones
            hold = 1.0 if (closed or 0 < i < n - 1) else 0.3
            out.append((p[0] + nx * k * amp * hold, p[1] + ny * k * amp * hold))
        return out

    @staticmethod
    def _spline(pts, closed):
        """Catmull-Rom through the points, emitted as cubic beziers."""
        n = len(pts)
        get = (lambda i: pts[i % n]) if closed else (lambda i: pts[max(0, min(n - 1, i))])
        d = "M %.1f %.1f" % pts[0]
        last = n if closed else n - 1
        for i in range(last):
            p0, p1, p2, p3 = get(i - 1), get(i), get(i + 1), get(i + 2)
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += " C %.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
        return d + (" Z" if closed else "")

    def path_d(self, pts, amp=2.4, step=36, closed=False):
        pts = list(pts)
        if closed and math.dist(pts[0], pts[-1]) > 1e-6:
            pts.append(pts[0])
        pts = self._resample(pts, step)
        if closed and math.dist(pts[0], pts[-1]) < 1e-6:
            pts.pop()
        return self._spline(self._jitter(pts, amp, closed), closed)

    # ---------------------------------------------------------------- marks

    def add(self, svg):
        self.parts.append(svg)

    def stroke(self, pts, w=W_OUTLINE, color=PALETTE["ink"], amp=2.4, step=36,
               closed=False, opacity=1.0):
        d = self.path_d(pts, amp, step, closed)
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w:.1f}" '
                 f'stroke-linecap="round" stroke-linejoin="round" opacity="{opacity:g}"/>')
        return d

    def shape(self, pts, fill, stroke=PALETTE["ink"], w=W_EDGE, amp=2.2, step=40):
        """Flat fill + ink contour, sharing one wobbly outline. The workhorse."""
        d = self.path_d(pts, amp, step, closed=True)
        s = f' stroke="{stroke}" stroke-width="{w:.1f}" stroke-linejoin="round"' if stroke else ""
        self.add(f'<path d="{d}" fill="{fill}"{s}/>')
        return d

    def cord(self, pts, w=9.0, fill=PALETTE["rope"], amp=2.0, step=40):
        """A rope drawn as a stroke: ink underlay, colour on top."""
        d = self.path_d(pts, amp, step)
        self.add(f'<path d="{d}" fill="none" stroke="{PALETTE["ink"]}" '
                 f'stroke-width="{w + 5:.1f}" stroke-linecap="round"/>')
        self.add(f'<path d="{d}" fill="none" stroke="{fill}" '
                 f'stroke-width="{w:.1f}" stroke-linecap="round"/>')

    def plank(self, a, b, w0, w1, fill=PALETTE["wood"], tip=0.0, amp=1.8):
        """Tapered beam from a to b. tip>0 sharpens the far end to a point."""
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1.0
        ux, uy = dx / L, dy / L
        nx, ny = -uy, ux
        pts = [(a[0] + nx * w0 / 2, a[1] + ny * w0 / 2),
               (b[0] + nx * w1 / 2, b[1] + ny * w1 / 2)]
        if tip:
            # two points a few px apart read as a cut end; one point gets rounded
            # away by the spline and comes out looking like a blob.
            pts.append((b[0] + ux * tip + nx * 5, b[1] + uy * tip + ny * 5))
            pts.append((b[0] + ux * tip - nx * 5, b[1] + uy * tip - ny * 5))
        pts += [(b[0] - nx * w1 / 2, b[1] - ny * w1 / 2),
                (a[0] - nx * w0 / 2, a[1] - ny * w0 / 2)]
        self.shape(pts, fill, amp=amp, step=46)
        return (ux, uy), (nx, ny)

    def coil(self, a, b, turns, girth, fill=PALETTE["rope"]):
        """Rope wound round a bar: a chain of fat overlapping bands a->b."""
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1.0
        ux, uy = dx / L, dy / L
        nx, ny = -uy, ux
        pitch = L / turns
        for i in range(turns):
            t = (i + 0.5) * pitch
            c = (a[0] + ux * t, a[1] + uy * t)
            band = [(c[0] + nx * girth / 2 - ux * pitch * 0.62,
                     c[1] + ny * girth / 2 - uy * pitch * 0.62),
                    (c[0] + nx * girth / 2 + ux * pitch * 0.62,
                     c[1] + ny * girth / 2 + uy * pitch * 0.62),
                    (c[0] - nx * girth / 2 + ux * pitch * 0.52,
                     c[1] - ny * girth / 2 + uy * pitch * 0.52),
                    (c[0] - nx * girth / 2 - ux * pitch * 0.52,
                     c[1] - ny * girth / 2 - uy * pitch * 0.52)]
            self.shape(band, fill, w=3.4, amp=1.3, step=22)

    def speck(self, x, y, length, angle, w=2.6, color="#1f1f1f", opacity=0.85):
        """One background fleck. Short, slightly curved, randomly rotated."""
        c, s = math.cos(angle), math.sin(angle)
        bow = self.rng.uniform(-0.28, 0.28) * length
        pts = [(x, y),
               (x + c * length / 2 - s * bow, y + s * length / 2 + c * bow),
               (x + c * length, y + s * length)]
        d = self._spline(pts, False)
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w:.1f}" '
                 f'stroke-linecap="round" opacity="{opacity:.2f}"/>')

    # ---------------------------------------------------------------- output

    def svg(self, w, h, background=None):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
                f'viewBox="0 0 {w} {h}">')
        bg = f'<rect width="{w}" height="{h}" fill="{background}"/>' if background else ""
        return head + bg + "\n" + "\n".join(self.parts) + "\n</svg>\n"
