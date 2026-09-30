# ComfyUI workflows — stick-figure history style

Workflows for the flat cartoon look: bold outlines, stick figures with blank white round heads and dot eyes, detailed period backgrounds.

**To open one:** drag the `.json` file onto the ComfyUI canvas (or Workflow → Open). Every workflow has a yellow **READ ME** note listing the model files it needs.

| File | What it does | Needs |
|---|---|---|
| `workflows/01_sdxl_scene.json` | Prompt → image, SDXL | ~8 GB VRAM |
| `workflows/02_sdxl_style_reference.json` | Same, but copies the look of a reference picture | SDXL + the **ComfyUI_IPAdapter_plus** custom nodes (install from ComfyUI Manager) |
| `workflows/03_flux_scene.json` | Prompt → image, FLUX.1 (follows long prompts better) | More VRAM than SDXL; set `weight_dtype` to `fp8_e4m3fn` on smaller cards |
| `workflows/04_flux_style_reference.json` | FLUX + a reference picture (Redux) | Core nodes only |
| `workflows/05_upscale_to_4k.json` | Any finished frame → exactly 3840×2160 | A 4× upscale model |

Suggested order: generate with 01 or 03 → fix in Krita → upscale the keepers with 05.

## Model files

Put each file in the folder shown, inside `ComfyUI/models/`, then press **R** in ComfyUI to refresh the lists.

| File | Folder | Download |
|---|---|---|
| `sd_xl_base_1.0.safetensors` | `checkpoints/` | [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) |
| `flux1-dev.safetensors` | `diffusion_models/` | [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) (accept the licence first) |
| `flux1-schnell.safetensors` *(optional)* | `diffusion_models/` | [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) |
| `ae.safetensors` | `vae/` | same FLUX repos |
| `clip_l.safetensors`, `t5xxl_fp8_e4m3fn.safetensors` | `text_encoders/` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) |
| `flux1-redux-dev.safetensors` | `style_models/` | [black-forest-labs/FLUX.1-Redux-dev](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev) |
| `sigclip_vision_patch14_384.safetensors` | `clip_vision/` | [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) |
| `ip-adapter-plus_sdxl_vit-h.safetensors` | `ipadapter/` | [h94/IP-Adapter](https://huggingface.co/h94/IP-Adapter), folder `sdxl_models/` |
| `CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors` | `clip_vision/` | [h94/IP-Adapter](https://huggingface.co/h94/IP-Adapter), `models/image_encoder/model.safetensors` — **rename it** to this name |
| `RealESRGAN_x4plus_anime_6B.pth` | `upscale_models/` | [Real-ESRGAN release v0.2.2.4](https://github.com/xinntao/Real-ESRGAN/releases/tag/v0.2.2.4) |

Older ComfyUI installs use `unet/` instead of `diffusion_models/` and `clip/` instead of `text_encoders/`; both work.

**Licences for a monetized channel:** SDXL allows commercial use. FLUX.1 [dev] and Redux are under Black Forest Labs' non-commercial licence — read it before using them on a channel that earns money. FLUX.1 [schnell] is Apache 2.0: pick it in 03's loader and set KSampler steps to **4**.

## Prompts

Keep the style words at the start of every prompt so all shots match, and change only the scene after them.

**Style (always first):**
```
flat 2D cartoon illustration, bold clean black outlines, simple cel shading, bright saturated colors, stick-figure characters with plain white round heads, simple black dot eyes, thin black stick arms and legs, historical costumes, highly detailed background
```

**Full scene** (the default in every workflow):
```
a medieval crusader knight in chainmail with a nose-guard helmet, white tabard with a red cross and a red cape, lying knocked out on the ground with X eyes, next to a worried woman in a long red medieval dress with a gold circlet and a cream headscarf, sunny Moorish market street, horseshoe arches, carved wooden balconies, hanging brass lanterns, palm trees, clay pots and woven baskets, wide 16:9 shot
```

**Background only** (add characters later in Krita or Inkscape) — replace the style's character words with `no people, empty street` and describe only the place:
```
flat 2D cartoon illustration, bold clean black outlines, simple cel shading, bright saturated colors, highly detailed background, no people, empty street, sunny Moorish market street, horseshoe arches, carved wooden balconies, hanging brass lanterns, palm trees, clay pots and woven baskets, wide 16:9 shot
```

## Tips

- **Seeds** are set to *randomize*, so every run gives a new image. When one is close, set the seed to *fixed* and change only the prompt.
- **Same characters in every shot** is what image models are worst at. Either draw the characters once as vector templates and place them over generated backgrounds, or fix faces and costumes with the [Krita AI Diffusion](https://github.com/Acly/krita-ai-diffusion) plugin, which uses this same ComfyUI.
- **More consistent style:** give 02 or 04 one of your own finished frames as the reference, so each new shot matches your channel rather than someone else's.
