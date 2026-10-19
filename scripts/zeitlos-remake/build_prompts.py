"""Write prompts.json: one Higgsfield Ad Multiplier video-edit prompt per clip that needs fixing.

Only shots where a host is out of uniform are edited; every other shot of the original is kept.
Each single-host clip gets [host photo, uniform reference]; the group clip gets three host
photos plus the uniform reference. The uniform reference is a crop of the light-blue scrubs
already worn in the kept shots (see pipeline.sh uniform_ref), so the fixed parts match them.
"""
import json, os, sys

S = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

UNIFORM = ("a medium light-blue (cornflower) short-sleeve V-neck medical scrub top with thin seam piping and a chest pocket holding a pen, "
           "matching light-blue straight-leg scrub trousers and a small white clip-on photo ID badge on the left chest; "
           "no stethoscope, no jacket, no sweater, no hoodie, no visible undershirt sleeves and no logos")
LOOK = {
    "photo1": "dark-brown skin, short black hair in neat cornrow braids pulled straight back into a small low bun, dark-brown eyes, rounded cheeks and a soft natural smile",
    "photo2": "fair skin, short tousled light-brown hair, short light-brown stubble beard and moustache, blue-grey eyes and a full round face",
    "photo4": "tanned skin, long voluminous glossy black hair in big soft waves with a centre part, full groomed eyebrows, long lashes, glam makeup, glossy pink lips and a thin gold cross necklace",
    "photo5": "light skin, long straight jet-black hair with a centre part and long face-framing layers, dark-brown eyes, pink lips and a calm closed-mouth smile",
}
PRESERVE = ("Preserve every caption, subtitle, and other untargeted on-screen text element from @Video1 exactly as it appears, "
            "including its wording, styling, placement, animation, and timing. Text physically attached to a replaced target follows that replacement.")

# clip: (start s, end s, [(photo, alias, source target)], untouched content)
CLIPS = {
    "f01": (40, 58, [("photo5", "HOST B", "the long-black-haired presenter in the bright-blue sweater in the bathroom and the shared kitchen")],
            "the walk-in shower, grab bars, kitchen counters, vegetables and dough"),
    "f02": (58, 85, [("photo5", "HOST B", "the long-black-haired presenter in the bright-blue sweater in the lounge, the hallway with the calendar and by the window, including the brief partial view under the ring ceiling light")],
            "the lounge, wall calendar, team photos, clock, ring ceiling light and windows"),
    "f03": (85, 109, [("photo2", "HOST C", "the short-haired presenter in navy-blue scrubs in the sensory garden and beside the standing-aid chair")],
            "the garden, gazebo, raised flower bed, standing-aid device and dining room"),
    "f04": (109, 133, [("photo2", "HOST C", "the short-haired presenter in navy-blue scrubs in the documentation room and the fitness room, including the fast transition shots")],
            "the documentation desk, monitors, lift device, fitness machines and the elderly resident on the exercise bike"),
    "f05": (133, 145, [("photo2", "HOST C", "the short-haired presenter in navy-blue scrubs helping the elderly resident stand up, and in the final outdoor close-up")],
            "the elderly resident in the dark vest, chairs, windows and the wall mural"),
    "f06": (145, 157, [("photo4", "HOST D", "the presenter with long wavy black hair in teal scrubs at the training-shop counter")],
            "the elderly shopper, the older cashier behind the counter in the teal top, shop shelves, products and the picture shopping list"),
    "f07": (169, 181, [("photo4", "HOST D", "the presenter with long wavy black hair in teal scrubs in the chair-yoga room and at the therapy pool")],
            "the chair-yoga residents and their clothes, yoga mats, therapy pool, pool lift and windows"),
    "f08": (193, 217, [("photo1", "HOST E", "the presenter with dark hair in turquoise scrubs in the baking kitchen and at the craft table")],
            "the elderly residents baking, dough, bowls, craft materials and the hand seen in the craft close-up"),
    "f09": (229, 241, [("photo1", "HOST E", "the presenter with dark hair wearing a red blouse and black leather jacket in the activity room")],
            "the activity room, brain mural, posters, tables and chairs"),
    "f10": (241, 252.5, [("photo4", "HOST D", "the 1st person from the left (black top)"),
                         ("photo5", "HOST B", "the 4th person from the left (blue sweater)"),
                         ("photo2", "HOST C", "the 5th person from the left (grey hoodie)")],
            "the 2nd and 3rd people from the left exactly as they are (their faces, light-blue scrubs and stethoscopes), the LVR Klinik building and sign, the pathway, hedges and trees"),
}


def prompt(start, end, people, keep):
    dur = round(end - start, 3)
    multi = len(people) > 1
    utag = f"@Image{len(people) + 1}"
    decl, ops, aliases = [], [], []
    for i, (ph, alias, target) in enumerate(people, start=1):
        tag = f"@Image{i}"
        aliases.append(f"{alias} from {tag}")
        if multi:
            decl.append(f"[{tag}] — {alias}, replacement for {target}: exact face, skin tone and hair from {tag}, wearing the uniform from {utag}.")
            ops.append(f"{i}. REPLACE — 0-{dur:g}s: {target} in @Video1 never appears; replace that person completely with {alias} from {tag} "
                       f"in the uniform from {utag}, keeping only the source pose, position and motion.")
        else:
            decl.append(f"[{tag}] — {alias}, the replacement person for {target}: the exact face, facial structure, skin tone and hair from {tag} ({LOOK[ph]}). "
                        f"Wardrobe instruction from the user overrides the clothing in {tag}: {alias} wears the uniform from {utag}.")
            ops.append(f"{i}. REPLACE — 0-{dur:g}s: The original source person identified as {target} in @Video1 must never appear in any frame of the output. "
                       f"Replace that person completely with {alias} from {tag} in every appearance, transferring the face, skin tone and hair from {tag} and dressing {alias} in the uniform from {utag}, "
                       f"retaining only the original performance, speaking mouth movements, expressions, gestures, pose, blocking, interactions, and timing, including through cuts, transitions, motion blur and partial views.")
    decl.append(f"[{utag}] — UNIFORM, garment reference only (no person): {UNIFORM}. Match its exact light-blue shade, cut, piping, pen and badge.")
    lock = (f"IDENTITY lock: {', '.join(aliases)}. Each face must match its reference exactly and stay identical in every frame, in wide shots and close-ups, "
            f"with no drift, morphing or blending with the source face"
            + ("; identities must never cross, merge, swap or duplicate between people" if multi else "")
            + f". Nothing from {utag} except the clothing is used. No other person, object, text, environment, action, cut, camera move, lighting treatment or timing changes.")
    body = [PRESERVE,
            "Video edit. Keep this @Video1 clip exactly as it is — the same shots and cuts, camera moves, framing, composition, unmapped people, setting, "
            "held and environmental props, lighting, pacing, and timing. "
            f"Change only {'three of the five people' if multi else 'the presenter'}, keeping source blocking, poses, motion, lip movements, position, "
            "screen placement, and timing while rendering the reference face and the light-blue uniform."]
    return "\n".join(decl + body + ops + [
        lock,
        f"Render {', '.join(aliases)} with the reference face and the {utag} light-blue scrub uniform, inheriting only the source performance and timing.",
        f"Everything else — {keep}, the CapCut AI watermark, lighting, the camera moves and all timing — stays exactly the same."])


out = {}
for k, (a, b, people, keep) in CLIPS.items():
    p = prompt(a, b, people, keep)
    assert len(p) <= 3900, (k, len(p))
    out[k] = {"start": a, "end": b, "duration": round(b - a, 3), "images": [x[0] for x in people] + ["uniform_ref"], "prompt": p}
    print(k, a, b, out[k]["images"], len(p))
json.dump(out, open(os.path.join(S, "prompts.json"), "w"), ensure_ascii=False, indent=1)
