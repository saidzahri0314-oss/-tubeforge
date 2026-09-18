#!/usr/bin/env python3
"""
scene_ladder.py — a redraw of the reference frame in pure SVG.

Geometry is not eyeballed: the rails, horizon, rung angles and head radii were
measured off the reference by masking on its five flat colours. What is eyeballed
is everything the measurement cannot give you — where a wrinkle goes, how a
smirk sits.

    python3 scene_ladder.py && node render.cjs out/ladder.svg out/ladder.png
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stickstyle import Pen, PALETTE, oval, lerp, W_OUTLINE, W_EDGE, W_DETAIL  # noqa: E402

C = PALETTE
W, H = 1636, 980
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")

p = Pen(seed=1518)

# ---------------------------------------------------------------- background
# Horizon sampled every 150px off the reference: a soft colour change, no line.
horizon = [(0, 689), (170, 675), (320, 670), (470, 674), (620, 667), (770, 672),
           (920, 662), (1070, 659), (1220, 651), (1370, 658), (1520, 669), (1636, 672)]
p.add('<path d="%s L 1636 980 L 0 980 Z" fill="%s"/>'
      % (p.path_d(horizon, amp=1.4, step=120), C["ground"]))

# Flecks. Blob-counted off the reference: ~90 across the frame, median length 6px,
# p90 16px, a couple as long as 37. Heavily skewed small — a flat random length
# turns the wall into a snowstorm, which is the easiest way to lose this look.
rng = p.rng
for _ in range(96):
    x = rng.uniform(0, W)
    y = rng.uniform(-10, H)
    if y > 655 and rng.random() < 0.7:
        continue                                   # ground is cleaner than the wall
    length = 3 + 30 * rng.random() ** 2.6
    p.speck(x, y, length, rng.uniform(0, math.tau),
            w=rng.uniform(1.7, 2.7), opacity=rng.uniform(0.5, 0.9))

# ---------------------------------------------------------------- the ladder
# Rail centrelines, from the wood-mask column extents.
# Refit against the reference row by row: its ladder is near-constant width
# (~350px), it does not splay toward the camera. Reading the measured numbers as
# rail centres when they were outer edges pushed the right rail ~55px wide.
L0, L1 = (321, 96), (730, 895)
R0, R1 = (639, 66), (984, 748)


def rail_pt(t, top, bot):
    return lerp(top, bot, t)


# Rungs go behind the rails. Using the same t on both rails is what produces the
# reference's progressive rung tilt (-7deg at the top, -23deg at the plank) —
# the rails are not parallel, so the perspective falls out for free.
for t in (0.075, 0.18, 0.285, 0.39, 0.495, 0.60, 0.705, 0.81):
    a = rail_pt(t, L0, L1)
    b = rail_pt(t, R0, R1)
    thick = 21 + 13 * t
    p.plank((a[0] - 14, a[1] - 2), (b[0] + 16, b[1] + 2), thick, thick + 3)

# Rails on top, tapering wider toward the bottom, ends sharpened to a point.
p.plank(L0, L1, 30, 42, tip=26)
p.plank(R0, R1, 34, 48, tip=28)

# --------------------------------------------------------------- the face
FX, FY = 582, 220
face = oval(FX, FY, 62, 76, n=44)
face = [(x, y - 6 * max(0.0, -(y - FY) / 76)) for x, y in face]   # slightly egg-shaped
p.shape(face, C["skin"], w=W_OUTLINE, amp=2.0, step=34)

# forehead wrinkles — the density is the joke: everything else in frame is 5 lines
for y, sp in ((152, 26), (164, 34), (176, 40), (188, 44), (199, 45)):
    p.stroke([(FX - sp, y + 5), (FX, y - 3), (FX + sp, y + 4)],
             w=W_DETAIL, amp=1.0, step=22)
# eyes: small, ringed, pointing nowhere
for ex, ey in ((553, 213), (611, 207)):
    p.shape(oval(ex, ey, 13, 12, n=22), C["skin"], w=2.6, amp=0.9, step=14)
    p.stroke(oval(ex, ey, 7.5, 7, n=16), w=2.2, amp=0.7, step=10, closed=True)
    p.shape(oval(ex, ey, 3.2, 3.0, n=10), C["ink"], stroke=None, amp=0.4, step=8)
    p.stroke([(ex - 18, ey - 16), (ex - 4, ey - 21), (ex + 12, ey - 15)],
             w=3.0, amp=1.0, step=16)                     # brow
    p.stroke([(ex - 14, ey + 17), (ex + 1, ey + 20)], w=2.2, amp=0.9, step=14)
    p.stroke([(ex - 17, ey + 9), (ex - 24, ey + 17)], w=2.0, amp=0.8, step=12)
# nose
p.stroke([(FX - 1, 224), (FX + 10, 234), (FX - 4, 239)], w=2.4, amp=0.8, step=14)
# the scream
mouth = oval(590, 262, 41, 38, rot=0.12, n=30)
p.shape(mouth, C["mouth"], w=4.2, amp=1.4, step=20)
p.shape(oval(590, 243, 33, 13, n=18), C["gum"], stroke=None, amp=1.0, step=14)
p.shape(oval(592, 289, 28, 14, n=18), C["gum"], stroke=None, amp=1.0, step=14)  # tongue
for i in range(4):                                        # upper teeth
    tx = 562 + i * 15
    p.shape([(tx, 233), (tx + 11, 231), (tx + 11, 248), (tx, 250)],
            C["skin"], w=2.0, amp=0.7, step=10)
for i in range(3):                                        # lower teeth
    tx = 570 + i * 15
    p.shape([(tx, 291), (tx + 11, 290), (tx + 11, 278), (tx, 279)],
            C["skin"], w=2.0, amp=0.7, step=10)
# cheek and jaw creases
for sx in (-1, 1):
    for dx, dy, ln in ((48, 240, 22), (52, 268, 18), (44, 296, 14)):
        p.stroke([(FX + sx * dx, dy), (FX + sx * (dx + 9), dy + ln)],
                 w=2.3, amp=0.9, step=14)

# --------------------------------------------------- bottom plank, over rails
PK_A, PK_B = (636, 816), (1016, 652)
p.plank(PK_A, PK_B, 54, 58)
# the splintered sliver poking up-left out of it
p.plank((1010, 644), (944, 556), 24, 12, tip=12)

# ------------------------------------------------ the tortured, and his ropes
# He is a stick figure like the other two, spread-eagled on the ladder: wrists
# roped up to the top rung, ankles roped down to the plank. Traced off the
# reference at 3x — the neck and BOTH arms meet at a single shoulder point
# (642,367), and the torso splits into legs at the hip (683,467). Read those
# lines as rope instead of limbs and he ends up a head on a string.
SHOULDER = (642, 367)
HIP = (683, 467)
WRIST_L, WRIST_R = (487, 288), (674, 230)
ANKLE_L, ANKLE_R = (699, 601), (775, 550)

p.stroke([(604, 291), (624, 330), SHOULDER], w=W_OUTLINE, amp=1.5, step=34)   # neck
p.stroke([WRIST_L, (521, 314), (556, 344), (600, 360), SHOULDER],             # arms,
         w=W_OUTLINE, amp=1.8, step=40)                                       # hauled
p.stroke([WRIST_R, (684, 300), (664, 342), SHOULDER], w=W_OUTLINE, amp=1.8, step=40)
p.stroke([SHOULDER, (660, 414), HIP], w=W_OUTLINE, amp=1.5, step=44)          # torso
p.stroke([HIP, (689, 532), ANKLE_L], w=W_OUTLINE, amp=1.8, step=44)           # legs
p.stroke([HIP, (728, 508), ANKLE_R], w=W_OUTLINE, amp=1.8, step=44)

# top-rung lashings, and the ropes down to each wrist
p.coil((404, 152), (502, 141), 7, 48)
p.coil((558, 137), (656, 126), 7, 48)
p.cord([(470, 148), (458, 206), (470, 258), (488, 284)], w=9)
p.cord([(650, 133), (674, 178), (680, 210), (674, 234)], w=9)
p.coil((470, 268), (500, 300), 3, 26)          # wrist bindings, over the limb
p.coil((660, 214), (690, 244), 3, 26)
# ankle bindings, and the ropes down to the plank
p.coil((684, 582), (714, 618), 3, 28)
p.coil((760, 532), (792, 566), 3, 28)
p.cord([(702, 616), (710, 670), (730, 714), (750, 742)], w=9)
p.cord([(780, 566), (802, 626), (838, 686), (868, 724)], w=9)
# the big lashing round the plank
p.coil((704, 790), (882, 712), 11, 66)

# ------------------------------------------------------------------ figures


def head(cx, cy, r):
    p.shape(oval(cx, cy, r, r * 1.02, n=34), C["skin"], w=W_OUTLINE, amp=2.2, step=26)


def dot(x, y, r=4.6):
    p.shape(oval(x, y, r, r, n=12), C["ink"], stroke=None, amp=0.6, step=8)


# --- left figure: pigtailed, smug, holding the far end of the rope
head(352, 600, 60)
p.shape([(290, 592), (292, 552), (314, 524), (354, 512), (398, 524), (416, 550),
         (418, 572), (400, 562), (376, 552), (346, 550), (314, 558), (298, 574)],
        C["hair"], w=3.6, amp=1.8, step=24)
p.shape([(300, 556), (280, 600), (274, 650), (282, 682), (296, 678), (296, 640),
         (306, 596), (314, 566)], C["hair"], w=3.6, amp=1.6, step=22)
dot(370, 592)
dot(400, 587)
p.stroke([(388, 561), (414, 569)], w=3.4, amp=1.0, step=16)          # raised brow
p.stroke([(374, 620), (394, 619), (410, 605)], w=3.4, amp=1.2, step=18)  # smirk
p.stroke([(356, 660), (364, 728), (372, 790)], w=W_OUTLINE, amp=2.0, step=46)
p.stroke([(372, 790), (348, 850), (370, 940)], w=W_OUTLINE, amp=2.2, step=50)
p.stroke([(372, 790), (404, 850), (452, 942)], w=W_OUTLINE, amp=2.2, step=50)
p.stroke([(366, 694), (410, 682), (452, 658)], w=W_OUTLINE, amp=2.0, step=44)   # arm
p.stroke([(452, 658), (468, 648)], w=W_OUTLINE, amp=1.0, step=16)
p.stroke([(462, 664), (474, 652)], w=3.4, amp=0.9, step=14)                     # fingers

# --- right figure: scowling, gripping the plank
head(1082, 422, 64)
p.shape([(1014, 432), (1010, 392), (1022, 360), (1040, 350), (1050, 336),
         (1068, 346), (1084, 332), (1100, 346), (1118, 338), (1132, 356),
         (1148, 366), (1152, 400), (1148, 428), (1132, 400), (1108, 386),
         (1080, 380), (1048, 388), (1026, 408)], C["hair"], w=3.6, amp=1.8, step=22)
p.stroke([(1036, 404), (1066, 420)], w=4.0, amp=1.0, step=18)        # angry brows
p.stroke([(1128, 400), (1104, 418)], w=4.0, amp=1.0, step=18)
dot(1050, 436)
dot(1114, 434)
p.stroke([(1062, 464), (1086, 468), (1104, 458)], w=3.4, amp=1.2, step=18)   # smirk
p.stroke([(1082, 488), (1098, 566), (1118, 642)], w=W_OUTLINE, amp=2.0, step=46)
p.stroke([(1118, 642), (1114, 760), (1112, 946)], w=W_OUTLINE, amp=2.2, step=56)
p.stroke([(1118, 642), (1168, 730), (1242, 946)], w=W_OUTLINE, amp=2.2, step=56)
p.stroke([(1090, 502), (1030, 566), (972, 628)], w=W_OUTLINE, amp=2.0, step=46)  # arm
p.stroke([(972, 628), (956, 640)], w=W_OUTLINE, amp=1.0, step=16)
p.stroke([(966, 616), (952, 630)], w=3.4, amp=0.9, step=14)                      # fingers

# ------------------------------------------------------------------- write
os.makedirs(OUT, exist_ok=True)
path = os.path.join(OUT, "ladder.svg")
with open(path, "w") as f:
    f.write(p.svg(W, H, background=C["wall"]))
print("wrote", path, os.path.getsize(path), "bytes")
