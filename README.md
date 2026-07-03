# 🔺 TubeForge (Streamlit)

AI copilot for launching your **first faceless YouTube media project** — niche analysis, script X-ray, and reverse-engineering. Powered by the Claude API (`claude-opus-4-8`).

## Deploy on Streamlit Community Cloud (free)

1. **Put this folder on GitHub**
   - Create a free account at [github.com](https://github.com)
   - Click **+** (top right) → **New repository** → name it `tubeforge` → **Create repository**
   - Click **uploading an existing file** → drag in: `app.py`, `requirements.txt`, `README.md`, and the `.streamlit/config.toml` file → **Commit changes**
   - ⚠️ Never upload `.streamlit/secrets.toml` — that's your local key file.

2. **Deploy**
   - Go to [share.streamlit.io](https://share.streamlit.io) → sign in with GitHub → **Create app**
   - Repository: `yourname/tubeforge` · Branch: `main` · Main file: `app.py` → **Deploy**

3. **Add your secrets**
   - In the app: menu (⋮, bottom right) → **Settings** → **Secrets** → paste:

     ```toml
     ANTHROPIC_API_KEY = "sk-ant-api03-your-real-key"
     APP_PASSWORD = "choose-any-access-code"
     ```

   - Save. The app reboots and is live at `https://yourname-tubeforge.streamlit.app`.

> **Why APP_PASSWORD matters:** your app URL is public, and every analysis spends *your* Anthropic credits. With `APP_PASSWORD` set, visitors must enter your access code first. Remove that line from secrets only if you truly want it open to everyone.

## Run locally

```bash
cd ~/tubeforge-streamlit
.venv/bin/streamlit run app.py
```

Local key goes in `.streamlit/secrets.toml` (already gitignored):

```toml
ANTHROPIC_API_KEY = "sk-ant-api03-..."
```
