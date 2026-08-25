"""Build and render style frames for the Dancing Plague film.

    LIBGL_ALWAYS_SOFTWARE=1 EGL_PLATFORM=surfaceless \
      python render_shots.py [shot ...] --out DIR --res 1280x720 --samples 32

Shots map to the shot list in SCRIPT.md. With no shot named, renders all.
"""

import argparse, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bpy
import woodcut as W

TAU = math.pi * 2
D = math.radians


# ---------------------------------------------------------------- primitives
def box(name, loc, scale, mat):
    bpy.ops.mesh.primitive_cube_add(size=2, location=loc)
    ob = bpy.context.object
    ob.name, ob.scale = name, scale
    ob.data.materials.append(mat)
    return ob


def cyl(name, loc, r, depth, mat, rot=(0, 0, 0), verts=16):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=depth,
                                        location=loc, rotation=rot)
    ob = bpy.context.object
    ob.name = name
    ob.data.materials.append(mat)
    return ob


def cone(name, loc, r1, r2, depth, mat, rot=(0, 0, 0), verts=16):
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r1, radius2=r2,
                                    depth=depth, location=loc, rotation=rot)
    ob = bpy.context.object
    ob.name = name
    ob.data.materials.append(mat)
    return ob


def ball(name, loc, r, mat, segments=16):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=segments // 2,
                                         radius=r, location=loc)
    ob = bpy.context.object
    ob.name = name
    ob.data.materials.append(mat)
    bpy.ops.object.shade_smooth()
    return ob


def join(objs, name):
    """Join parts into one mesh so line art draws a single outer contour.

    Without this every primitive gets its own outline and a figure reads as
    a stack of separate lumps rather than one silhouette.
    """
    objs = [o for o in objs if o and o.type == 'MESH']
    if not objs:
        return None
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    ob = bpy.context.object
    ob.name = name
    return ob


def ground(mat, size=60):
    bpy.ops.mesh.primitive_plane_add(size=size, location=(0, 0, 0))
    ob = bpy.context.object
    ob.name = 'ground'
    ob.data.materials.append(mat)
    return ob


# ------------------------------------------------------------------ assemblies
def figure(name, loc, rot_z=0.0, dress=None, skin=None, lean=0.0, arm_swing=0.5):
    """A woodcut-cartoon figure: cone skirt, ball head, raised arms.

    Built at the origin, joined into one mesh, then placed -- so the line art
    gives one clean silhouette per figure.
    """
    parts = [
        cone(f'{name}_skirt', (0, 0, 0.55), 0.36, 0.14, 1.10, dress, verts=14),
        cyl(f'{name}_torso', (0, 0, 1.22), 0.165, 0.44, dress, verts=12),
        ball(f'{name}_head', (0, 0, 1.57), 0.135, skin, segments=14),
    ]
    for sign in (1, -1):
        swing = arm_swing * sign
        ax = sign * 0.185
        parts.append(cyl(f'{name}_arm', (ax, -0.02, 1.19 + 0.06 * arm_swing),
                         0.055, 0.52, skin,
                         rot=(swing * 0.45, 0, sign * D(40) + swing * 0.35), verts=8))
    ob = join(parts, name)
    ob.rotation_euler = (lean, 0, rot_z)
    ob.location = loc
    return ob


def plank_stage(mat_wood, origin=(0, 0, 0), w=3.2, d=2.1, h=0.95, planks=9):
    """Deck built from separate planks so line art finds every seam."""
    ox, oy, oz = origin
    step = (d * 2) / planks
    for i in range(planks):
        y = oy - d + step * (i + 0.5)
        box(f'plank{i}', (ox, y, oz + h), (w, step * 0.46, 0.05), mat_wood)
    for sx in (-1, 1):
        for sy in (-1, 1):
            box('post', (ox + sx * (w - 0.16), oy + sy * (d - 0.16), oz + h / 2),
                (0.11, 0.11, h / 2), mat_wood)
    box('beam_f', (ox, oy - d, oz + h - 0.12), (w, 0.08, 0.09), mat_wood)
    box('beam_b', (ox, oy + d, oz + h - 0.12), (w, 0.08, 0.09), mat_wood)
    return h + 0.05


def timber_wall(mat_plaster, mat_beam, mat_dark, x=0.0, y=3.0, w=5.0, h=3.4):
    box('wall', (x, y, h / 2), (w, 0.16, h / 2), mat_plaster)
    for bx in (-w + 0.5, -1.5, 1.5, w - 0.5):
        box('stud', (x + bx, y - 0.18, h / 2), (0.11, 0.05, h / 2), mat_beam)
    for bz in (1.55, h - 0.12):
        box('rail', (x, y - 0.18, bz), (w, 0.05, 0.11), mat_beam)
    box('brace', (x - 3.1, y - 0.19, 2.4), (1.15, 0.04, 0.07), mat_beam,
        ).rotation_euler = (0, D(34), 0)
    # doorway: a dark recess, the door of shot 00A
    box('door_hole', (x + 0.9, y - 0.10, 1.05), (0.52, 0.06, 1.05), mat_dark)
    box('lintel', (x + 0.9, y - 0.20, 2.16), (0.66, 0.06, 0.09), mat_beam)
    return


# ---------------------------------------------------------------------- shots
def shot_00A():
    """Cold open: Troffea steps out of the door into the street."""
    W.reset_scene()
    stone   = W.toon_material('stone', W.STONE, shadow_mix=0.70, hatch_scale=210)
    plaster = W.toon_material('plaster', W.PARCHMENT, shadow_mix=0.60, hatch_scale=170)
    beam    = W.toon_material('beam', W.WOOD, shadow_mix=0.66, hatch_scale=190)
    dark    = W.toon_material('dark', W.INK, shadow_mix=0.20, hatch=False)
    wool    = W.toon_material('wool', W.OCHRE, shadow_mix=0.64, hatch_scale=200)
    skin    = W.toon_material('skin', W.SKIN, shadow_mix=0.54, hatch_scale=220)

    ground(stone)
    timber_wall(plaster, beam, dark, y=3.2, w=5.4, h=3.8)
    box('wall_far', (0, -3.4, 2.2), (6.5, 0.18, 2.2), plaster)

    figure('troffea', (0.9, 2.15, 0), rot_z=D(14), dress=wool, skin=skin,
           arm_swing=0.85, lean=0.06)

    W.world(W.PARCHMENT, 0.16)
    W.sun((D(62), 0, D(34)), energy=5.4, warm=(1.0, 0.93, 0.76))
    W.camera((3.35, -1.35, 1.42), lens=34, look_at=(0.85, 2.25, 0.92))
    W.add_line_art(thickness=0.055)


def shoe(name, x, y, z, mat, tilt=0.0):
    """A simple last: flattened ellipsoid body plus a raised heel."""
    body = ball(f'{name}_body', (x, y, z + 0.055), 1.0, mat, segments=20)
    body.scale = (0.105, 0.215, 0.058)
    body.rotation_euler = (0, 0, tilt)
    heel = ball(f'{name}_heel', (x - math.sin(tilt) * 0.13, y + math.cos(tilt) * 0.13,
                                 z + 0.105), 1.0, mat, segments=18)
    heel.scale = (0.093, 0.075, 0.105)
    heel.rotation_euler = (0, 0, tilt)
    return join([body, heel], name)


def shot_05G():
    """Macro insert: the red shoes on stone. The only saturated colour."""
    W.reset_scene()
    rock = W.toon_material('rock', W.STONE, shadow_mix=0.76, hatch_scale=200)
    red  = W.toon_material('red', W.RED, shadow_mix=0.46, hatch_scale=240)

    ground(rock, size=20)
    box('slab',  (0, 0, 0.05), (0.85, 0.62, 0.05), rock)
    box('slab2', (-0.95, 0.42, 0.04), (0.55, 0.42, 0.04), rock)
    box('slab3', (0.92, -0.30, 0.045), (0.5, 0.45, 0.045), rock)

    shoe('shoe_l', -0.155, 0.01, 0.10, red, tilt=D(-9))
    shoe('shoe_r',  0.165, -0.02, 0.10, red, tilt=D(11))

    W.world(W.INK, 0.05)
    W.sun((D(44), 0, D(-52)), energy=4.0, warm=(1.0, 0.76, 0.52))
    W.camera((0.10, -0.92, 0.50), lens=40, look_at=(0.0, 0.02, 0.13))
    W.add_line_art(thickness=0.016)


def _square(mat_stone, mat_wood, mat_far, mat_win):
    """The market square: small stage, a lot of emptiness around it."""
    ground(mat_stone, size=90)
    deck = plank_stage(mat_wood, origin=(-1.2, 1.0, 0))
    # buildings pushed well back so the square reads as empty
    for i, (x, y, w, h) in enumerate(((-19, 30, 3.2, 3.6), (-8, 33, 3.6, 4.4),
                                      (4, 31, 2.8, 3.2), (15, 29, 3.0, 4.0),
                                      (25, 32, 3.4, 3.4))):
        parts = [box(f'bldg{i}', (x, y, h), (w, 2.2, h), mat_far),
                 box(f'roof{i}', (x, y, h * 2 + 0.5), (w * 0.98, 2.2, 0.5), mat_far)]
        join(parts, f'bldg{i}')
        for wx in (-0.55, -0.18, 0.18, 0.55):
            for wz in (0.55, 0.95, 1.35):
                box(f'win{i}', (x + wx * w, y - 2.24, h * wz),
                    (w * 0.075, 0.05, h * 0.085), mat_win)
    return deck


def shot_10A():
    """Close: the empty stage, weathered, in an empty square."""
    W.reset_scene()
    stone = W.toon_material('stone', W.STONE, shadow_mix=0.68, hatch_scale=230)
    wood  = W.toon_material('wood', W.WOOD, shadow_mix=0.66, hatch_scale=180)
    far   = W.toon_material('far', W.OCHRE, shadow_mix=0.70, hatch_scale=150)
    ink_win = W.toon_material('window', W.INK, shadow_mix=0.15, hatch=False)
    _square(stone, wood, far, ink_win)
    W.world(W.PARCHMENT, 0.18)
    W.sun((D(44), 0, D(-36)), energy=5.0, warm=(0.99, 0.95, 0.86))
    W.camera((6.0, -9.2, 2.75), lens=34, look_at=(-1.0, 1.4, 1.35))
    W.add_line_art(thickness=0.05)


def shot_10B():
    """Close: silhouettes fill the stage until it is packed."""
    W.reset_scene()
    stone = W.toon_material('stone', W.STONE, shadow_mix=0.68, hatch_scale=230)
    wood  = W.toon_material('wood', W.WOOD, shadow_mix=0.66, hatch_scale=180)
    far   = W.toon_material('far', W.OCHRE, shadow_mix=0.70, hatch_scale=150)
    ink_win = W.toon_material('window', W.INK, shadow_mix=0.15, hatch=False)
    ink   = W.toon_material('silhouette', W.INK, shadow_mix=0.12, hatch=False)
    red   = W.toon_material('red', W.RED, shadow_mix=0.42, hatch_scale=260)
    top = _square(stone, wood, far, ink_win)

    import random
    random.seed(1518)
    n = 0
    for gx in range(-2, 3):
        for gy in range(-1, 2):
            x = -1.2 + gx * 1.18 + random.uniform(-0.14, 0.14)
            y = 1.0 + gy * 1.02 + random.uniform(-0.14, 0.14)
            mat = red if n == 7 else ink          # one dancer keeps the red
            figure(f'd{n}', (x, y, top + 0.01), rot_z=random.uniform(0, TAU),
                   dress=mat, skin=mat, lean=random.uniform(-0.22, 0.22),
                   arm_swing=random.choice([-0.9, -0.4, 0.5, 1.0, 1.4]))
            n += 1
    W.world(W.PARCHMENT, 0.18)
    W.sun((D(44), 0, D(-36)), energy=4.8, warm=(0.99, 0.94, 0.84))
    W.camera((6.0, -9.2, 2.75), lens=34, look_at=(-1.0, 1.4, 1.35))
    W.add_line_art(thickness=0.05)


SHOTS = {'00A': shot_00A, '05G': shot_05G, '10A': shot_10A, '10B': shot_10B}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('shots', nargs='*', default=[])
    ap.add_argument('--out', default='/home/user/renders')
    ap.add_argument('--res', default='1280x720')
    ap.add_argument('--samples', type=int, default=32)
    a = ap.parse_args([x for x in sys.argv[1:] if not x.startswith('--python')])

    w, h = (int(v) for v in a.res.lower().split('x'))
    os.makedirs(a.out, exist_ok=True)
    todo = a.shots or list(SHOTS)

    for name in todo:
        if name not in SHOTS:
            print(f'!! unknown shot {name}'); continue
        print(f'--- building {name} ---', flush=True)
        SHOTS[name]()
        sc = W.configure_render((w, h), a.samples)
        sc.render.filepath = os.path.join(a.out, f'{name}.png')
        bpy.ops.render.render(write_still=True)
        print(f'>> {name}.png  {os.path.getsize(sc.render.filepath)} bytes', flush=True)


if __name__ == '__main__':
    main()
