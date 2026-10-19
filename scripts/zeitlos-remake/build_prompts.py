import json, os, sys
S = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
UNIFORM = ("the universal staff uniform: a soft light-blue (ceil blue) short-sleeve V-neck medical scrub top with one chest pocket, "
           "matching light-blue straight-leg scrub trousers, a small plain white clip-on name badge on the left chest and clean white sneakers; "
           "no stethoscope, no jacket, no sweater, no hoodie, no visible undershirt sleeves and no logos")
LOOK = {
 "photo1": "dark-brown skin, short black hair in neat cornrow braids pulled straight back into a small low bun, dark-brown eyes, rounded cheeks and a soft natural smile",
 "photo2": "fair skin, short tousled light-brown hair, short light-brown stubble beard and moustache, blue-grey eyes and a full round face",
 "photo3": "light-olive skin, very long straight dark-brown hair worn half-up with a raised crown, defined dark eyebrows, warm brown eyes, small ear piercings and a bright smile",
 "photo4": "tanned skin, long voluminous glossy black hair in big soft waves with a centre part, full groomed eyebrows, long lashes, glam makeup, glossy pink lips and a thin gold cross necklace",
 "photo5": "light skin, long straight jet-black hair with a centre part and long face-framing layers, dark-brown eyes, pink lips and a calm closed-mouth smile",
}
PRESERVE = ("Preserve every caption, subtitle, and other untargeted on-screen text element from @Video1 exactly as it appears, "
            "including its wording, styling, placement, animation, and timing. Text physically attached to a replaced target follows that replacement.")
# chunk: (start, end, [(photo, alias, source target description)], other people/content to keep)
CH = {
 "c01": (0, 20,  [("photo3","HOST A","the long-haired presenter in light-blue scrubs with a stethoscope, outside the building entrance and in the lounge hallway")], "the building entrance, garden, hallway and lounge furniture"),
 "c02": (20, 40, [("photo3","HOST A","the long-haired presenter in light-blue scrubs with a stethoscope standing in the resident room and beside the care bed")], "the resident room, care bed, armchair, photos and window"),
 "c03": (40, 58, [("photo5","HOST B","the long-black-haired presenter in the bright-blue sweater in the bathroom and the shared kitchen")], "the walk-in shower, grab bars, kitchen counters, vegetables and dough"),
 "c04": (58, 85, [("photo5","HOST B","the long-black-haired presenter in the bright-blue sweater in the lounge, the hallway with the calendar and by the window, including the brief partial view under the ring ceiling light")], "the lounge, wall calendar, team photos, clock, ring ceiling light and windows"),
 "c05": (85, 109, [("photo2","HOST C","the short-haired presenter in navy-blue scrubs in the sensory garden and beside the standing-aid chair")], "the garden, gazebo, raised flower bed, standing-aid device and dining room"),
 "c06": (109, 133, [("photo2","HOST C","the short-haired presenter in navy-blue scrubs in the documentation room and the fitness room, including the fast transition shots")], "the documentation desk, monitors, lift device, fitness machines and the elderly resident on the exercise bike"),
 "c07": (133, 145, [("photo2","HOST C","the short-haired presenter in navy-blue scrubs helping the elderly resident stand up, and in the final outdoor close-up")], "the elderly resident in the dark vest, chairs, windows and the wall mural"),
 "c08": (145, 169, [("photo4","HOST D","the presenter with long wavy black hair in teal scrubs at the training-shop counter and at the bus stop")], "the elderly shoppers, the older cashier behind the counter, shop shelves, bus-stop shelter and the elderly woman on the bench"),
 "c09": (169, 193, [("photo4","HOST D","the presenter with long wavy black hair in teal scrubs in the chair-yoga room, at the therapy pool and beside the dining table with the dog")], "the chair-yoga residents, therapy pool and pool lift, golden retriever, residents at the table and the food"),
 "c10": (193, 217, [("photo1","HOST E","the presenter with dark braided hair in turquoise scrubs in the baking kitchen and at the craft table")], "the elderly residents baking, dough, bowls, craft materials and the hand seen in the craft close-up"),
 "c11": (217, 241, [("photo1","HOST E","the presenter with dark braided hair, first in light-blue scrubs at the daily-schedule board and in the lounge, then wearing a red blouse and black leather jacket in the activity room")], "the daily-schedule board, lounge sofas, activity room, brain mural and tables"),
 "c12": (241, 252.5, [("photo4","HOST D","the 1st person from the left (black top)"),
                      ("photo1","HOST E","the 2nd person from the left"),
                      ("photo3","HOST A","the 3rd person from the left"),
                      ("photo5","HOST B","the 4th person from the left (blue sweater)"),
                      ("photo2","HOST C","the 5th person from the left (grey hoodie)")], "the LVR Klinik building and sign, the pathway, hedges and trees"),
}
out = {}
for k,(a,b,people,keep) in CH.items():
    dur = round(b-a, 3)
    decl = []; ops = []; aliases = []; multi = len(people) > 1
    for i,(ph,alias,target) in enumerate(people, start=1):
        tag = f"@Image{i}"; aliases.append(f"{alias} from {tag}")
        if multi:
            decl.append(f"[{tag}] — {alias}, replacement for {target}: exact face, skin tone and hair from {tag}, wearing the universal light-blue scrub uniform.")
        else:
            decl.append(f"[{tag}] — {alias}, the replacement person for {target}: the exact face, facial structure, skin tone and hair from {tag} ({LOOK[ph]}). "
                        f"Wardrobe instruction from the user overrides the clothing in {tag}: {alias} wears {UNIFORM}.")
        if multi:
            ops.append(f"{i}. REPLACE — 0-{dur:g}s: {target} in @Video1 never appears; replace that person completely with {alias} from {tag}, keeping only the source pose, position and motion.")
            continue
        ops.append(f"{i}. REPLACE — 0-{dur:g}s: The original source person identified as {target} in @Video1 must never appear in any frame of the output. "
                   f"Replace that person completely with {alias} from {tag} in every appearance, transferring the face, skin tone and hair from {tag} and dressing {alias} in the universal light-blue scrub uniform, "
                   f"retaining only the original performance, speaking mouth movements, expressions, gestures, pose, blocking, interactions, and timing, including through cuts, transitions, motion blur and partial views.")
    if multi:
        decl.append(f"Universal light-blue scrub uniform worn by all five: {UNIFORM}.")
    lock = (f"IDENTITY lock: {', '.join(aliases)}. Each face must match its reference exactly and stay identical in every frame, in wide shots and close-ups, with no drift, morphing or blending with the source face"
            + ("; identities must never cross, merge, swap or duplicate between people" if multi else "")
            + ". The uniform is the same light-blue scrub set in every frame. No other person, object, text, environment, action, cut, camera move, lighting treatment or timing changes.")
    p = "\n".join(decl + [PRESERVE,
        f"Video edit. Keep this @Video1 clip exactly as it is — the same shots and cuts, camera moves, framing, composition, unmapped people, setting, held and environmental props, lighting, pacing, and timing. "
        f"Change only {'the five people' if multi else 'the presenter'}, keeping source blocking, poses, motion, lip movements, position, screen placement, and timing while rendering the reference face and the universal light-blue scrub uniform."]
        + ops + [lock,
        f"Render {', '.join(aliases)} with the reference face and the identical light-blue scrub uniform, inheriting only the source performance and timing.",
        f"Everything else — {keep}, the CapCut AI watermark, lighting, the camera moves and all timing — stays exactly the same."])
    assert len(p) <= 3900, (k, len(p))
    out[k] = {"start": a, "end": b, "duration": dur, "images": [x[0] for x in people], "prompt": p}
    print(k, a, b, [x[0] for x in people], len(p))
json.dump(out, open(os.path.join(S, "prompts.json"), "w"), ensure_ascii=False, indent=1)
