"""Woodcut Gothic look library for the Dancing Plague film.

Implements the style bible in PIPELINE-krita-blender.md as reusable Blender
calls: the four-colour palette, the toon shader recipe
(Diffuse -> Shader to RGB -> ColorRamp[CONSTANT] -> Emission), scene-wide
Grease Pencil line art, and the render configuration.

Run headless with the bpy module; see render_shots.py.
"""

import os

import bpy

ART = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'art')

# --- style bible palette (PIPELINE-krita-blender.md) ------------------------
PARCHMENT = (0.910, 0.863, 0.753)
INK       = (0.102, 0.086, 0.078)
OCHRE     = (0.690, 0.490, 0.227)
RED       = (0.769, 0.169, 0.110)
BLUE      = (0.239, 0.337, 0.439)   # Act IV cold night
STONE     = (0.545, 0.510, 0.451)
WOOD      = (0.478, 0.353, 0.208)
SKIN      = (0.812, 0.671, 0.529)


def _srgb_to_linear(c):
    out = []
    for v in c:
        out.append(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4)
    return tuple(out)


def _mix(a, b, f):
    return tuple(a[i] * (1 - f) + b[i] * f for i in range(3))


def reset_scene():
    """Wipe the default scene so each shot builds from nothing."""
    bpy.ops.wm.read_factory_settings(use_empty=True)
    return bpy.context.scene


def hatch_texture(kind='medium'):
    """Path to an Inkscape-authored hatch tile (see art/make_svg.py)."""
    return os.path.join(ART, 'textures', f'hatch_{kind}.png')


def toon_material(name, base, shadow_mix=0.62, mid_mix=0.26,
                  hatch=True, hatch_scale=140.0, hatch_angle=0.6,
                  hatch_image='medium', hatch_tile=5.0):
    """The pipeline's toon recipe, plus screen-space engraving hatch.

    Diffuse -> Shader to RGB -> ColorRamp[CONSTANT] -> Emission.
    Shader to RGB is EEVEE-only; this will not render in Cycles.

    The hatch is a Wave texture in Window space, masked to the shadow band
    only -- it stands in for the cross-hatch plates Krita would supply, and
    it is what makes the shading read as a block print rather than as CG.
    """
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    L = nt.links.new

    diffuse = nt.nodes.new('ShaderNodeBsdfDiffuse')
    diffuse.inputs['Color'].default_value = (1, 1, 1, 1)
    diffuse.location = (-1100, 100)

    to_rgb = nt.nodes.new('ShaderNodeShaderToRGB')
    to_rgb.location = (-920, 100)

    ramp = nt.nodes.new('ShaderNodeValToRGB')
    ramp.location = (-740, 180)
    ramp.color_ramp.interpolation = 'CONSTANT'      # <- the whole trick

    shadow = _mix(base, INK, shadow_mix)
    mid    = _mix(base, INK, mid_mix)
    els = ramp.color_ramp.elements
    while len(els) > 1:
        els.remove(els[-1])
    els[0].position, els[0].color = 0.0, (*_srgb_to_linear(shadow), 1)
    for pos, col in ((0.28, mid), (0.60, base)):
        els.new(pos).color = (*_srgb_to_linear(col), 1)

    emit = nt.nodes.new('ShaderNodeEmission')
    emit.location = (-160, 100)
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    out.location = (40, 100)

    L(diffuse.outputs['BSDF'], to_rgb.inputs['Shader'])
    L(to_rgb.outputs['Color'], ramp.inputs['Fac'])

    if not hatch:
        L(ramp.outputs['Color'], emit.inputs['Color'])
        L(emit.outputs['Emission'], out.inputs['Surface'])
        return mat

    # --- engraving hatch, screen space, shadow band only -------------------
    coord = nt.nodes.new('ShaderNodeTexCoord');  coord.location = (-1400, -260)
    mapn  = nt.nodes.new('ShaderNodeMapping');   mapn.location = (-1220, -260)
    mapn.inputs['Rotation'].default_value = (0, 0, hatch_angle)

    tile_path = hatch_texture(hatch_image) if hatch_image else None
    if tile_path and os.path.exists(tile_path):
        # authored in Inkscape, rastered to PNG -- the Krita half of the pipeline
        mapn.inputs['Scale'].default_value = (hatch_tile, hatch_tile, 1.0)
        wave = nt.nodes.new('ShaderNodeTexImage'); wave.location = (-1020, -260)
        wave.image = bpy.data.images.load(tile_path, check_existing=True)
        wave.image.colorspace_settings.name = 'Non-Color'
        wave.extension = 'REPEAT'
        wave.interpolation = 'Linear'
    else:
        wave = nt.nodes.new('ShaderNodeTexWave');    wave.location = (-1020, -260)
        wave.wave_type = 'BANDS'
        wave.bands_direction = 'X'
        wave.wave_profile = 'SAW'
        wave.inputs['Scale'].default_value = hatch_scale
        wave.inputs['Distortion'].default_value = 1.6
        wave.inputs['Detail'].default_value = 1.0

    hramp = nt.nodes.new('ShaderNodeValToRGB');  hramp.location = (-840, -260)
    hramp.color_ramp.interpolation = 'CONSTANT'
    hramp.color_ramp.elements[0].position = 0.0
    hramp.color_ramp.elements[0].color = (0, 0, 0, 1)      # line
    hramp.color_ramp.elements[1].position = 0.55
    hramp.color_ramp.elements[1].color = (1, 1, 1, 1)      # gap

    # shadow band mask: 1 where the toon ramp is in its darkest step
    smask = nt.nodes.new('ShaderNodeValToRGB');  smask.location = (-740, -60)
    smask.color_ramp.interpolation = 'CONSTANT'
    smask.color_ramp.elements[0].position = 0.0
    smask.color_ramp.elements[0].color = (1, 1, 1, 1)
    smask.color_ramp.elements[1].position = 0.28
    smask.color_ramp.elements[1].color = (0, 0, 0, 1)

    inv = nt.nodes.new('ShaderNodeMath');  inv.location = (-620, -260)
    inv.operation = 'SUBTRACT'
    inv.inputs[0].default_value = 1.0

    fac = nt.nodes.new('ShaderNodeMath');  fac.location = (-460, -160)
    fac.operation = 'MULTIPLY'

    mix = nt.nodes.new('ShaderNodeMixRGB'); mix.location = (-320, 100)
    mix.blend_type = 'MIX'
    mix.inputs['Color2'].default_value = (*_srgb_to_linear(_mix(base, INK, 0.86)), 1)

    L(coord.outputs['Window'], mapn.inputs['Vector'])
    L(mapn.outputs['Vector'], wave.inputs['Vector'])
    L(wave.outputs['Color'], hramp.inputs['Fac'])
    L(hramp.outputs['Color'], inv.inputs[1])
    L(to_rgb.outputs['Color'], smask.inputs['Fac'])
    L(smask.outputs['Color'], fac.inputs[0])
    L(inv.outputs['Value'], fac.inputs[1])
    L(ramp.outputs['Color'], mix.inputs['Color1'])
    L(fac.outputs['Value'], mix.inputs['Fac'])
    L(mix.outputs['Color'], emit.inputs['Color'])
    L(emit.outputs['Emission'], out.inputs['Surface'])
    return mat


def add_line_art(thickness=0.05, wobble=0.006, colour=INK):
    """Scene-wide Grease Pencil line art with hand-drawn wobble.

    GPv3 (Blender 4.3+) renamed the modifier's `thickness` to `radius`.
    """
    bpy.ops.object.grease_pencil_add(type='LINEART_SCENE', location=(0, 0, 0))
    gp = bpy.context.object
    gp.name = 'LineArt'

    lineart = next((m for m in gp.modifiers if 'LINEART' in m.type), None)
    if lineart:
        if hasattr(lineart, 'radius'):
            lineart.radius = thickness
        elif hasattr(lineart, 'thickness'):
            lineart.thickness = thickness
        for attr, val in (('use_contour', True), ('use_crease', True),
                          ('use_intersection', True), ('use_material', True)):
            if hasattr(lineart, attr):
                setattr(lineart, attr, val)
        if hasattr(lineart, 'crease_threshold'):
            lineart.crease_threshold = 0.35

    # Noise keeps the line from reading as CG
    try:
        noise = gp.modifiers.new('wobble', 'GREASE_PENCIL_NOISE')
        for attr in ('factor', 'factor_strength', 'factor_thickness'):
            if hasattr(noise, attr):
                setattr(noise, attr, wobble)
    except Exception:
        pass

    for slot in gp.material_slots:
        m = slot.material
        if m and getattr(m, 'grease_pencil', None):
            m.grease_pencil.color = (*_srgb_to_linear(colour), 1)
    return gp


def sun(rot, energy=3.5, warm=None, angle=0.35):
    lamp = bpy.data.lights.new('sun', 'SUN')
    lamp.energy = energy
    lamp.angle = angle
    if warm:
        lamp.color = _srgb_to_linear(warm)
    ob = bpy.data.objects.new('sun', lamp)
    ob.rotation_euler = rot
    bpy.context.collection.objects.link(ob)
    return ob


def camera(loc, rot=None, lens=35, look_at=None):
    """Camera placed by target rather than by guessed Euler angles."""
    from mathutils import Vector
    cam = bpy.data.cameras.new('cam')
    cam.lens = lens
    ob = bpy.data.objects.new('cam', cam)
    ob.location = loc
    if look_at is not None:
        d = Vector(look_at) - Vector(loc)
        ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    elif rot is not None:
        ob.rotation_euler = rot
    bpy.context.collection.objects.link(ob)
    bpy.context.scene.camera = ob
    return ob


def world(colour, strength=0.55):
    w = bpy.data.worlds.new('w')
    w.use_nodes = True
    bg = w.node_tree.nodes['Background']
    bg.inputs[0].default_value = (*_srgb_to_linear(colour), 1)
    bg.inputs[1].default_value = strength
    bpy.context.scene.world = w
    return w


def configure_render(res=(1280, 720), samples=32):
    """EEVEE, flat view transform -- AgX would mute the palette."""
    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    sc.render.film_transparent = False
    sc.render.image_settings.file_format = 'PNG'
    sc.eevee.taa_render_samples = samples
    try:
        sc.view_settings.view_transform = 'Standard'
    except TypeError:
        sc.view_settings.view_transform = 'NONE'    # bpy module ships a minimal OCIO config
    sc.view_settings.look = 'None'
    return sc
