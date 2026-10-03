# HIGGSFIELD PROMPTS — Pip Wants to Fly

**Every shot is two prompts:** a **Keyframe** (a still → Nano Banana Pro) and a **Motion** prompt (video → Kling 3.0, with that keyframe as the start frame). Each shot's settings sit just above its prompts; the reasoning behind them is in [`SETTINGS-higgsfield.md`](SETTINGS-higgsfield.md).

- **`@Pip`, `@Snowball-Point`, `@Under-the-Ice`, `@Balloon-Bunch`** are Higgsfield Elements you save in Step 0. Type `@` in the prompt box to insert one. Not using Elements? Attach those images as reference images instead.
- **Paste the prompts as they are.** The style, lighting and negative text is already filled in and word-for-word identical across shots. That repetition is what keeps the look consistent, so don't reword it per shot.
- **Negatives are the last line** (`NEGATIVE: …`). The models used here have no separate negative field; if a model page shows one, move the list there.
- **AUDIO lines** only matter if you switch native sound on for that shot.

## The locks

These are already pasted into every prompt below. They're here for reference, and for writing new shots in the same style.

**Style lock** — the art style, in every prompt

```text
Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
```

**Pip lock** — the full character description, used in the asset prompts (shots use the short tag after `@Pip`)

```text
Pip, a little round penguin: chubby egg-shaped body, glossy navy-black back and head, cream-white belly and heart-shaped face patch, oversized round dark-brown eyes with big white sparkles, tiny rounded orange beak, short orange webbed feet, two small stubby flippers, a curly tuft of three feathers on top of the head, and a chunky knitted cherry-red scarf with one white stripe.
```

**Light A** — outdoor shots (snow and sky)

```text
bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
```

**Light B** — underwater shots

```text
sunlit shallow water, shimmering caustic light patterns rippling over everything, soft god rays slanting down from the surface at the upper left, glowing aqua-turquoise ambient light, sparkly drifting bubbles.
```

**Negative — keyframes**

```text
photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Negative — motion**

```text
photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood
```

## Step 0 — Assets

All on Nano Banana Pro at 2K. Generate 0A until Pip looks exactly right, then make 0B and 0C with 0A attached as a reference.

| # | Asset | Aspect | Save as Element |
|---|---|---|---|
| 0A | Pip — full body | 2:3 | **Pip** (together with 0B) |
| 0B | Pip — turnaround sheet | 16:9 | **Pip** |
| 0C | Pip — expression sheet | 16:9 | — your reference for checking faces |
| 0D | Snowball Point | 9:16 | **Snowball-Point** |
| 0E | Under the Ice | 9:16 | **Under-the-Ice** |
| 0F | Balloon bunch | 1:1 | **Balloon-Bunch** |

### 0A · Pip — full body (2:3)

```text
SUBJECT: Pip, a little round penguin: chubby egg-shaped body, glossy navy-black back and head, cream-white belly and heart-shaped face patch, oversized round dark-brown eyes with big white sparkles, tiny rounded orange beak, short orange webbed feet, two small stubby flippers, a curly tuft of three feathers on top of the head, and a chunky knitted cherry-red scarf with one white stripe. Standing in a neutral, friendly pose facing the camera with both feet visible, centered on a plain flat pale-blue background.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: soft global illumination, three-point studio lighting, gentle rim light.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, background props
```

### 0B · Pip — turnaround sheet (16:9, attach 0A)

```text
SUBJECT: character turnaround model sheet of the same character as the reference image — four consistent full-body views in a row: front, three-quarter, side profile and back, evenly spaced, the identical original character in every view, standing in a neutral pose with both feet visible. Pip, a little round penguin: chubby egg-shaped body, glossy navy-black back and head, cream-white belly and heart-shaped face patch, oversized round dark-brown eyes with big white sparkles, tiny rounded orange beak, short orange webbed feet, two small stubby flippers, a curly tuft of three feathers on top of the head, and a chunky knitted cherry-red scarf with one white stripe.
SETTING: pure white seamless studio background, professional character sheet presentation.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic. Soft fluffy feather texture and visible knitted yarn on the scarf.
LIGHTING: soft global illumination, three-point studio lighting, gentle rim light.
NEGATIVE: photorealistic, live action, realistic feathers, text, letters, numbers, labels, watermark, logo, frame border, extra characters, background props, distorted anatomy, extra limbs, extra flippers, extra eyes, deformed beak, harsh shadows, blurry
```

### 0C · Pip — expression sheet (16:9, attach 0A)

```text
SUBJECT: character expression sheet of the same character as the reference image — one full-body view on the left and a grid of six head-and-shoulders close-ups on the right: determined (cheeks puffed, eyes squeezed shut), amazed (huge sparkly eyes), joyful (wide open-beak smile), mid-sneeze (scrunched face), surprised (eyes popped wide), cheeky wink. Pip, a little round penguin: chubby egg-shaped body, glossy navy-black back and head, cream-white belly and heart-shaped face patch, oversized round dark-brown eyes with big white sparkles, tiny rounded orange beak, short orange webbed feet, two small stubby flippers, a curly tuft of three feathers on top of the head, and a chunky knitted cherry-red scarf with one white stripe.
SETTING: pure white seamless studio background, professional character sheet presentation.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: soft global illumination, three-point studio lighting, gentle rim light.
NEGATIVE: photorealistic, live action, realistic feathers, text, letters, numbers, labels, watermark, logo, frame border, extra characters, background props, distorted anatomy, extra limbs, extra flippers, extra eyes, deformed beak, harsh shadows, blurry
```

### 0D · Snowball Point (9:16)

```text
SETTING: Snowball Point, a cheerful sunny polar shore. Empty scene — no characters, no animals, no figures. In the foreground a smooth, low, rounded ice ledge juts out over sparkling turquoise water; to the left a gentle snowy slope ends in a small curved snow ramp; a big fluffy snowdrift; soft rounded snowbanks; distant rounded icebergs; a bright blue sky with puffy white clouds.
FRAMING: wide establishing view, horizon in the upper third.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, characters, animals, birds, penguins
```

### 0E · Under the Ice (9:16)

```text
SETTING: Under the Ice, an underwater scene just below a sunny polar sea. Empty scene — no characters, no animals, no figures. Clear, bright aqua-turquoise water; the rippling silvery surface with a few floating rounded ice chunks above; gently swaying rounded sea plants and smooth pebbles on a sandy floor far below; a few tiny bubbles drifting up.
FRAMING: wide view with open water in the center.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: sunlit shallow water, shimmering caustic light patterns rippling over everything, soft god rays slanting down from the surface at the upper left, glowing aqua-turquoise ambient light, sparkly drifting bubbles.
FORMAT: vertical 9:16.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, characters, fish, sharks, murky dark water
```

### 0F · Balloon bunch (1:1)

```text
SUBJECT: a single bunch of exactly five shiny round balloons — cherry red, sunny yellow, sky blue, lime green, tangerine orange — with thin white curly strings gathered together at the bottom, centered on a plain flat pale-blue background.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: soft even studio light.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, hands, characters, other objects
```

## Shots 01–13

Settings line: time in the edit · how much of the clip to keep · model · mode · generated length · aspect · frames · native sound · motion level · camera move.

### 01 · Hook — "Flap!"

`0:00.0–0:02.5` · keep **2.5 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** Medium · **Camera:** slow push-in

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) standing at the very edge of the ice ledge in three-quarter view toward the camera, both flippers raised mid-flap, cheeks puffed, eyes squeezed shut with fierce determination, scarf ends lifting in the breeze.
SETTING: @Snowball-Point — the sparkling turquoise sea and puffy clouds softly blurred behind Pip.
FRAMING: medium close-up at eye level, Pip centered in the middle third of the frame.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: @Pip flaps his tiny flippers super fast in a cartoon blur and bounces on his toes, then his feet lift just off the ice and he hovers, wobbling, eyes still squeezed shut.
CAMERA: slow push-in toward Pip, nothing else.
MOTION: medium — bouncy, springy, energetic flapping; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood
```

> This keyframe is also the thumbnail and the loop point: shot 13 ends on this exact image.

### 02 · Want — "The birds"

`0:02.5–0:04.5` · keep **2.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** Low · **Camera:** slow tilt up

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: seen from just behind @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe): the back of Pip's round head, feather tuft and red scarf fill the lower foreground as he gazes up; three small round white seabirds with grey wingtips swoop low overhead in a neat line from left to right.
SETTING: @Snowball-Point — bright blue sky with puffy white clouds filling the upper two thirds of the frame.
FRAMING: wide shot from a low angle over Pip's shoulder, looking up at the sky.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, more than three birds
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: the three seabirds swoop low over @Pip from left to right, so close his feather tuft ruffles, then glide gracefully up into the sky while Pip's head tilts back to follow them.
CAMERA: slow tilt up, following the birds into the sky, nothing else.
MOTION: low — calm, floaty, graceful; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, extra birds, birds merging together
```

### 03 · Try 1 — "Plop!"

`0:04.5–0:07.0` · keep **2.5 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound optional (snow poof) · **Motion:** Medium → High on the drop · **Camera:** static

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) seen from the side, hovering a few inches above the snowy top of the ice ledge, flippers a blur mid-flap, eyes squeezed shut, little feet dangling.
SETTING: @Snowball-Point — a soft snowbank behind Pip, the sea and sky beyond.
FRAMING: medium shot, static camera at Pip's height, Pip in the center.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: @Pip wobbles in the air for a moment, stops flapping and opens his eyes wide in surprise — then drops belly-first onto the soft snow with a cartoon squash-and-stretch bounce; a puff of powdery snow bursts up and his red scarf flops over his face.
CAMERA: static, locked off.
MOTION: medium, then one quick high-energy drop that settles into a gentle wiggle; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
AUDIO (only if native sound is on): a soft cartoon boing, then a fluffy snow poof — no voice, no music.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, injury, pain, crying
```

### 04 · Try 2 — "Slide!"

`0:07.0–0:09.0` · keep **2.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** High · **Camera:** fast tracking backward at snow level

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) belly-sliding head-first down a snowy slope straight toward the camera, flippers swept back like jet wings, beak open in a huge grin, scarf streaming behind him, a spray of sparkly snow kicked up.
SETTING: @Snowball-Point — the snowy slope rising behind Pip, blue sky above.
FRAMING: ground-level front view with the lens just above the snow, Pip centered in the middle third.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: @Pip zooms down the slope on his belly toward the camera, faster and faster, snow spraying in a sparkly wake and his scarf flapping behind him.
CAMERA: fast tracking shot moving backward at snow level, keeping Pip centered, nothing else.
MOTION: high — fast, zippy and exciting while Pip's shape stays solid and on model; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, motion blur smearing the face
```

### 05 · Fail 2 — "Whoosh… fwump!"

`0:09.0–0:12.0` · keep **3.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start + end frame · native sound optional (whoosh, fwump) · **Motion:** High → settles · **Camera:** static wide

**Start keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) shooting off the top of a small curved snow ramp into the air on the left side of the frame, flippers spread wide, beak open in a triumphant grin, scarf flying; a big fluffy snowdrift waits on the right side of the frame.
SETTING: @Snowball-Point — blue sky with puffy clouds, distant rounded icebergs.
FRAMING: wide side-profile view, static camera, the ramp on the left third and the snowdrift on the right third.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**End keyframe** — Nano Banana Pro · 2K · 9:16 · attach the start keyframe as the base image, so the background stays identical

```text
EDIT: use the attached start keyframe as the base image — keep the camera, background, lighting and art style exactly the same; change only Pip.
SUBJECT: @Pip is now stuck head-first in the big fluffy snowdrift on the right side of the frame — only his round lower body, orange feet and the end of his red scarf poke out, feet kicking; small puffs of snow hang in the air; the ramp on the left is empty.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, Pip's head visible, a second penguin
```

**Motion** — Kling 3.0 · start frame + end frame = the two keyframes above

```text
ACTION: @Pip soars off the ramp in a short, hopeful arc, flapping, then tips forward and dives head-first into the snowdrift — fwump — snow puffs up and his little orange feet wiggle in the air.
CAMERA: static wide shot; Pip crosses the frame from left to right.
MOTION: high on the jump, settling into a comic feet-wiggle; motion starts on frame 1 and lands on the end frame.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
AUDIO (only if native sound is on): a whoosh, then a soft fwump into the snow — no voice, no music.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, injury, pain
```

### 06 · Try 3 — "Balloons!"

`0:12.0–0:15.0` · keep **3.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** Medium · **Camera:** crane up

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) on tiptoe on the snowy shore, holding the white strings of @Balloon-Bunch in one flipper — five shiny balloons (cherry red, sunny yellow, sky blue, lime green, tangerine orange) floating above him and tugging upward — eyes wide with delight.
SETTING: @Snowball-Point — the sparkling sea and rounded icebergs behind him.
FRAMING: medium shot at eye level, Pip in the lower middle of the frame, the balloons in the upper third.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, strings around the neck or body
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: the five balloons tug @Pip gently upward; his feet leave the snow and he rises into the sky, kicking his little feet happily, beak open in a joyful smile.
CAMERA: smooth crane up, rising with Pip and revealing the sparkling sea and icebergs below, nothing else.
MOTION: medium — light, floaty, buoyant; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, strings wrapped around the neck or body, balloons popping, balloons changing number or color
```

### 07 · Uh-oh — "ACHOO!"

`0:15.0–0:17.0` · keep **2.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** Medium (one big jolt) · **Camera:** static

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) floating high in the bright sky, one flipper holding the balloon strings above his head, a single sparkly snowflake drifting down toward the tip of his beak, eyes crossed watching it, face starting to scrunch.
SETTING: open sky with soft white clouds; the five balloons (cherry red, sunny yellow, sky blue, lime green, tangerine orange) at the top edge of the frame.
FRAMING: close-up on Pip's head and shoulders, centered.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: the snowflake lands on @Pip's beak; his face scrunches, he leans back… and does one big cartoon sneeze — his whole body jolts, both flippers fling open, and the balloon strings slip away and float up out of frame.
CAMERA: static.
MOTION: medium, with one big comic jolt on the sneeze; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, mucus, spit, gross details
```

### 08 · Fall — "SPLASH!"

`0:17.0–0:19.0` · keep **2.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound optional (splash) · **Motion:** High · **Camera:** static top-down

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) falling toward the sea, seen from directly above, flippers and feet spread out like a starfish, scarf fluttering upward, eyes wide in surprise.
SETTING: the sparkling turquoise sea far below with a few small floating ice chunks, just off the shore of @Snowball-Point.
FRAMING: top-down bird's-eye view looking straight down, Pip small in the center of the frame.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: @Pip falls away from the camera, getting smaller, flippers flailing comically, then hits the water — splash — a big round crown of sparkly water bursts up and rings ripple outward.
CAMERA: static, top-down.
MOTION: high; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
AUDIO (only if native sound is on): a cartoon falling whistle, then a big splash — no voice, no music.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, violent crash, debris, injury
```

### 09 · Surprise — "Eyes open"

`0:19.0–0:21.0` · keep **2.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** Low · **Camera:** slow push-in

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) underwater, eyes shut tight and cheeks puffed, a swirl of bubbles around his head, red scarf floating softly upward.
SETTING: @Under-the-Ice — bright aqua water behind him.
FRAMING: close-up on Pip's head and shoulders, centered.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: sunlit shallow water, shimmering caustic light patterns rippling over everything, soft god rays slanting down from the surface at the upper left, glowing aqua-turquoise ambient light, sparkly drifting bubbles.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: the bubbles drift away; @Pip's eyes pop open wide in surprise, he blinks twice, looks around, and a curious smile spreads across his face.
CAMERA: slow push-in, nothing else.
MOTION: low — gentle, floaty and calm; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, drowning, distress, gasping, murky dark water
```

### 10 · Twist — "He's flying!"

`0:21.0–0:23.0` · keep **2.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** High · **Camera:** static (Pip passes the lens)

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) swimming fast straight toward the camera like a little rocket, flippers stretched like wings mid-stroke, huge joyful grin, red scarf streaming behind him, a trail of bubbles; a small school of round friendly fish in sunny yellow, coral pink and lime green parting around him.
SETTING: @Under-the-Ice — god rays and floating ice chunks above.
FRAMING: wide front view, Pip in the center at mid-distance.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: sunlit shallow water, shimmering caustic light patterns rippling over everything, soft god rays slanting down from the surface at the upper left, glowing aqua-turquoise ambient light, sparkly drifting bubbles.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, sharks, fish with teeth
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: @Pip beats his flippers like wings and rockets toward the camera, then whooshes past the lens; the little fish swirl apart in a sparkle and a bubble trail spirals behind him.
CAMERA: static; Pip flies past the camera.
MOTION: high — fast, joyful, swooping; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, sharks, fish with teeth, collision
```

### 11 · Joy — "Loop-de-loop"

`0:23.0–0:25.5` · keep **2.5 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame · native sound off · **Motion:** Medium–High · **Camera:** lateral tracking

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) gliding upward into a big swooping loop, body arched, flippers spread like wings, red scarf streaming behind him like a superhero cape; three round friendly fish follow him in a playful line; a spiral of bubbles.
SETTING: @Under-the-Ice — sun rays slanting down from the surface.
FRAMING: medium side view, Pip in the center.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: sunlit shallow water, shimmering caustic light patterns rippling over everything, soft god rays slanting down from the surface at the upper left, glowing aqua-turquoise ambient light, sparkly drifting bubbles.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above

```text
ACTION: @Pip swoops through one big loop like a little jet, scarf streaming like a cape, then zooms off to the right; the three fish copy his loop one by one.
CAMERA: smooth lateral tracking alongside Pip, left to right, nothing else.
MOTION: medium-high — graceful, swooping, dreamy; motion starts on frame 1.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood
```

> If the loop bends Pip out of shape, change "one big loop" to "a big swooping S-curve". For a floatier camera, run this one shot on Cinematic Studio Video 3.5 with camera style Dreamy Flow (≈50 credits instead of 8.75).

### 12 · Leap — "Ta-da!"

`0:25.5–0:27.5` · keep **2.0 s** · Kling 3.0 · Pro · 5 s · 9:16 · start + end frame · native sound optional (water burst, chime) · **Motion:** High, in slow motion · **Camera:** static low angle

**Start keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) bursting up out of the sparkling turquoise sea in a big arc on the left side of the frame, flippers spread wide, beak open in a joyful cheer, a glittering spray of water droplets around him.
SETTING: @Snowball-Point — the ice ledge on the right side of the frame, blue sky with puffy clouds.
FRAMING: low-angle wide view from just above the water surface, static camera.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**End keyframe** — Nano Banana Pro · 2K · 9:16 · attach the start keyframe as the base image, so the background stays identical

```text
EDIT: use the attached start keyframe as the base image — keep the camera, background, lighting and art style exactly the same; change only Pip.
SUBJECT: @Pip has landed on top of the ice ledge on the right in a proud hero pose — chest puffed, flippers on his hips, scarf fluttering — with a few water droplets still sparkling in the air; the water on the left is calm again.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background, a second penguin
```

**Motion** — Kling 3.0 · start frame + end frame = the two keyframes above

```text
ACTION: in slow motion, @Pip arcs through the air in a glittering spray of water, then lands neatly on the ice ledge with a little bounce and strikes a proud hero pose.
CAMERA: static low angle.
MOTION: high action played in slow motion, settling into the pose; motion starts on frame 1 and lands on the end frame.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
AUDIO (only if native sound is on): a water burst and a sparkly chime, then a soft landing thump — no voice, no music.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, crash landing, slipping, injury
```

### 13 · Loop — "Wink"

`0:27.5–0:30.0` · keep **the last 2.5 s** · Kling 3.0 · Pro · 5 s · 9:16 · start frame + end frame = the shot 01 keyframe · native sound off · **Motion:** Low → Medium · **Camera:** static, eye level

**Keyframe** — Nano Banana Pro · 2K · 9:16

```text
SUBJECT: @Pip (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) standing proudly at the edge of the ice ledge in a hero pose — chest puffed, flippers on his hips — beaming at the camera, a few water droplets sparkling on his feathers.
SETTING: @Snowball-Point — the sparkling turquoise sea and puffy clouds softly blurred behind Pip.
FRAMING: medium close-up at eye level, Pip centered in the middle third of the frame — the same framing as shot 01.
ART STYLE: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic.
LIGHTING: bright late-morning sunshine, warm soft key light from the upper left, cool sky-blue fill light, gentle rim light on rounded edges, soft rounded shadows, tiny sparkles glinting in the light.
FORMAT: vertical 9:16 composition, Pip and the action in the middle of the frame, the bottom fifth of the frame plain and uncluttered.
NEGATIVE: photorealistic, live action, realistic feathers, scary or sad mood, dark lighting, text, letters, numbers, captions, watermark, logo, frame border, extra limbs, extra flippers, extra eyes, deformed beak, duplicate characters, humans, harsh shadows, grainy, blurry, neon colors, cluttered background
```

**Motion** — Kling 3.0 · start frame = the keyframe above · end frame = the shot 01 keyframe

```text
ACTION: @Pip beams at the camera and gives one big cheeky wink, wiggles happily, then raises both flippers and starts to flap, cheeks puffing and eyes squeezing shut with determination.
CAMERA: static, eye level.
MOTION: low to medium — gentle and bouncy; motion starts on frame 1 and ends exactly on the end frame.
ART STYLE: keep the exact look of the start frame — stylized 3D preschool cartoon, soft toy-like surfaces, candy colors, non-photorealistic. Pip stays on model (navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe) and only emotes — no talking.
NEGATIVE: photorealistic, live action, morphing, melting face, flicker, jitter, warping, extra limbs, extra flippers, deformed beak, scarf changing color, duplicate penguins, humans, talking, lip-sync, on-screen text, captions, watermark, scene cut, dissolve, fade, frozen opening frame, shaky handheld camera, dutch angle, flashing lights, dark or scary mood, beak moving as if speaking
```

> End frame: reuse the shot 01 keyframe image itself — don't regenerate it. Use the last 2.5 s of the clip so it cuts back into shot 01 invisibly.

## Fast route — three 10-second multi-shot clips

Same story in three generations instead of thirteen: each prompt below makes one 10-second clip with four hard cuts, the same way Higgsfield's own kids-video workflow builds its scenes.

**Settings:** MiniMax H3 · 2K · 10 s · 9:16 · ≈20 credits per block (quoted 2026-10-02). Attach the reference images in the order the REFERENCES line lists them (location → character → prop); they become `@Image1`, `@Image2`, … Keep it to 7 references or fewer per block.

**What you give up:** per-shot control, the loop-de-loop (shot 11) and the end-frame tricks, so the loop back to the start won't be pixel-perfect.

**Count the cuts.** Multi-shot models sometimes merge shots. If a block comes back with fewer than four cuts, or one shot runs 3 s or longer, regenerate it once. If it merges again, combine its last two shots into one and generate three.

### Block 1 · 0:00–0:10 · shots 01–04

```text
Style: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic. Springy, bouncy, friendly cartoon motion with smooth, gentle camera moves — the look is exactly as in the reference images.
PALETTE LOCK: use only the colors of the reference images — no new colors, no recoloring of Pip, his scarf or the balloons.
A single 10-second scene of FOUR hard-cut shots. Do not open on a reference image — stage everything fresh. Pip only emotes and gestures; he does not talk. Motion starts on frame 1.
REFERENCES: @Image1 = SNOWBALL POINT (sunny polar shore: low ice ledge over turquoise water, snowy slope with a small snow ramp, big snowdrift). @Image2 = PIP (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe).
SHOT 1 — 0.0s to 2.5s — MEDIUM CLOSE-UP, eye level, slow push-in: Pip at the edge of the ice ledge flaps his tiny flippers super fast in a blur, eyes squeezed shut, and his feet lift just off the ice.
HARD CUT.
SHOT 2 — 2.5s to 5.0s — LOW-ANGLE WIDE over Pip's shoulder, slow tilt up: three small white seabirds swoop low over Pip, ruffling his tuft, then glide up into the blue sky.
HARD CUT.
SHOT 3 — 5.0s to 7.5s — MEDIUM side view, static: Pip hovers, wobbles, then drops belly-first onto the snow; a puff of snow bursts up and his scarf flops over his face.
HARD CUT.
SHOT 4 — 7.5s to 10.0s — GROUND-LEVEL front view, fast tracking backward: Pip belly-slides down the snowy slope straight toward the camera with a huge grin, snow spraying behind him.
Four hard-cut shots at 2.5s, 5.0s and 7.5s, no dissolves, no fades. Continuous motion within each shot, never freezes.
AUDIO: a rapid flapping flutter, bird chirps, a soft snow poof, a slide swoosh — no voice, no narration, no music.
NEGATIVE: opening on a reference image, static first frame, dissolves or fades, new or foreign colors, recolored Pip or scarf, style drift, extra characters, cloned penguins, talking, lip-sync, on-screen text, captions, photorealism, watermark
```

### Block 2 · 0:10–0:20 · shots 05–08

```text
Style: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic. Springy, bouncy, friendly cartoon motion with smooth, gentle camera moves — the look is exactly as in the reference images.
PALETTE LOCK: use only the colors of the reference images — no new colors, no recoloring of Pip, his scarf or the balloons.
A single 10-second scene of FOUR hard-cut shots. Do not open on a reference image — stage everything fresh. Pip only emotes and gestures; he does not talk. Motion starts on frame 1.
REFERENCES: @Image1 = SNOWBALL POINT (sunny polar shore: low ice ledge over turquoise water, snowy slope with a small snow ramp, big snowdrift). @Image2 = PIP (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe). @Image3 = BALLOON BUNCH (five shiny balloons: cherry red, sunny yellow, sky blue, lime green, tangerine orange; white strings).
SHOT 1 — 0.0s to 2.5s — WIDE side profile, static: Pip shoots off the small snow ramp, arcs through the air and dives head-first into a big snowdrift, his little feet wiggling.
HARD CUT.
SHOT 2 — 2.5s to 5.0s — MEDIUM, crane up: holding the balloon strings in one flipper, Pip is lifted off the snow and rises into the sky, kicking his feet happily, the sea revealed below.
HARD CUT.
SHOT 3 — 5.0s to 7.5s — CLOSE-UP, static: a snowflake lands on Pip's beak; he does one big cartoon sneeze and the balloon strings slip away out of frame.
HARD CUT.
SHOT 4 — 7.5s to 10.0s — TOP-DOWN, static: Pip falls toward the turquoise sea and lands with a big sparkly splash; the ripples settle.
Four hard-cut shots at 2.5s, 5.0s and 7.5s, no dissolves, no fades. Continuous motion within each shot, never freezes.
AUDIO: a whoosh and a soft fwump into snow, a balloon squeak, a tiny tinkle, a falling whistle, a big splash — no voice, no narration, no music.
NEGATIVE: opening on a reference image, static first frame, dissolves or fades, new or foreign colors, recolored Pip or scarf, style drift, extra characters, cloned penguins, talking, lip-sync, on-screen text, captions, photorealism, watermark, strings around the neck, balloons popping
```

### Block 3 · 0:20–0:30 · shots 09, 10, 12, 13

```text
Style: Stylized 3D animated-feature look for a preschool cartoon: chunky rounded characters with soft, clay-smooth, toy-like surfaces and a gentle subsurface glow, oversized glossy expressive eyes, clean readable silhouettes, simple rounded environments with no sharp edges, bright saturated candy palette of icy sky blue, snow white, sunny yellow, cherry red and ocean teal, soft global illumination, gentle rim light, soft rounded shadows, shallow depth of field, cheerful and cozy, non-photorealistic. Springy, bouncy, friendly cartoon motion with smooth, gentle camera moves — the look is exactly as in the reference images.
PALETTE LOCK: use only the colors of the reference images — no new colors, no recoloring of Pip, his scarf or the balloons.
A single 10-second scene of FOUR hard-cut shots. Do not open on a reference image — stage everything fresh. Pip only emotes and gestures; he does not talk. Motion starts on frame 1.
REFERENCES: @Image1 = UNDER THE ICE (bright aqua water, god rays, floating ice chunks above). @Image2 = SNOWBALL POINT (sunny polar shore: low ice ledge over turquoise water). @Image3 = PIP (little round navy-and-cream penguin, three-feather tuft, cherry-red scarf with one white stripe).
SHOT 1 — 0.0s to 2.5s — UNDERWATER CLOSE-UP, slow push-in: the bubbles clear, Pip's eyes pop open in surprise and a curious smile spreads across his face.
HARD CUT.
SHOT 2 — 2.5s to 5.0s — UNDERWATER WIDE front view, static: Pip beats his flippers like wings and rockets toward the camera past a school of round candy-colored fish, then whooshes past the lens.
HARD CUT.
SHOT 3 — 5.0s to 7.5s — LOW-ANGLE WIDE from just above the water, static: in slow motion Pip bursts out of the sea in a glittering arc and lands on the ice ledge in a proud hero pose.
HARD CUT.
SHOT 4 — 7.5s to 10.0s — MEDIUM CLOSE-UP, eye level, static: Pip beams at the camera, gives a cheeky wink, then raises his flippers and starts flapping again, eyes squeezed shut.
Four hard-cut shots at 2.5s, 5.0s and 7.5s, no dissolves, no fades. Continuous motion within each shot, never freezes.
AUDIO: bubbles, an underwater whoosh, a water burst, a sparkly chime, a soft landing thump — no voice, no narration, no music.
NEGATIVE: opening on a reference image, static first frame, dissolves or fades, new or foreign colors, recolored Pip or scarf, style drift, extra characters, cloned penguins, talking, lip-sync, on-screen text, captions, photorealism, watermark, dark water, sharks, distress
```
