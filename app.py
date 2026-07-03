"""TubeForge — AI copilot for launching your first faceless YouTube project.

Three-step system:
  1. Niche Analyzer   — structured viability analysis of any niche
  2. Script X-Ray     — extract hook / structure / retention from a winning transcript
  3. Reverse Engineer — stream a full launch package + ready-to-record script
"""

import json
import os

import anthropic
import streamlit as st

MODEL = "claude-opus-4-8"

st.set_page_config(
    page_title="TubeForge — Faceless YouTube Copilot",
    page_icon="🔺",
    layout="wide",
)

# ------------------------------------------------------------------ styling

st.markdown(
    """
<style>
  .stApp { background: #060606; }
  .block-container { max-width: 1080px; padding-top: 2.5rem; }

  .tf-pill {
    display: inline-block; color: #ff4d4d; border: 1px solid rgba(255,31,31,.5);
    border-radius: 999px; padding: 5px 18px; font-size: 12px; font-weight: 700;
    letter-spacing: .25em;
  }
  .tf-hero { text-align: center; padding: 24px 0 8px; }
  .tf-hero h1 {
    font-size: 52px; font-weight: 800; line-height: 1.1; letter-spacing: -0.02em;
    color: #f5f5f5; margin: 22px 0 14px;
    text-shadow: 0 0 60px rgba(255,40,40,.25);
  }
  .tf-red { color: #ff1f1f; }
  .tf-sub { color: #9a9a9a; font-size: 17px; max-width: 700px; margin: 0 auto 8px; }
  .tf-fine { color: #6b6b6b; font-size: 12px; }

  .stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: 700; }
  div[data-testid="stMetricValue"] { color: #ff4d4d; }

  .tf-quote {
    border-left: 3px solid #ff1f1f; padding: 6px 0 6px 14px;
    color: #eaeaea; font-style: italic; margin: 8px 0;
  }
  .tf-tag {
    display: inline-block; font-size: 11px; font-weight: 700; border-radius: 999px;
    padding: 2px 12px; letter-spacing: .06em; text-transform: uppercase;
  }
  .tf-tag.low, .tf-tag.easy { background: rgba(46,204,113,.14); color: #5fdc96; }
  .tf-tag.medium { background: rgba(241,196,15,.14); color: #ffd75e; }
  .tf-tag.high, .tf-tag.hard { background: rgba(255,31,31,.16); color: #ff4d4d; }
  .tf-label {
    font-size: 12px; letter-spacing: .14em; color: #ff4d4d;
    text-transform: uppercase; font-weight: 700; margin-bottom: 6px;
  }
</style>
""",
    unsafe_allow_html=True,
)


def tag(level: str) -> str:
    return f'<span class="tf-tag {level}">{level}</span>'


def md(s) -> str:
    """Escape $ so Streamlit markdown doesn't treat model text as LaTeX math."""
    return str(s).replace("$", "\\$")


# ------------------------------------------------------------------ auth / client


def secret(name: str):
    try:
        return st.secrets[name]
    except Exception:
        return os.environ.get(name)


def access_gate() -> bool:
    """If APP_PASSWORD is configured, require it once per session."""
    password = secret("APP_PASSWORD")
    if not password:
        return True
    if st.session_state.get("authed"):
        return True
    st.markdown('<div class="tf-hero"><span class="tf-pill">PRIVATE BETA</span></div>', unsafe_allow_html=True)
    entered = st.text_input("Access code", type="password")
    if entered == str(password):
        st.session_state["authed"] = True
        st.rerun()
    elif entered:
        st.error("Wrong access code.")
    return False


@st.cache_resource
def get_client():
    key = secret("ANTHROPIC_API_KEY")
    if not key:
        return None
    return anthropic.Anthropic(api_key=key)


# ------------------------------------------------------------------ premium / cost protection

# Your Stripe Payment Link (create one at dashboard.stripe.com → Payment Links).
# Can also be set as a STRIPE_CHECKOUT_URL secret to avoid editing code.
STRIPE_CHECKOUT_URL = secret("STRIPE_CHECKOUT_URL") or "https://buy.stripe.com/YOUR_LINK_HERE"

# The premium access key you give to paying customers.
# Override with a PREMIUM_ACCESS_KEY secret (recommended) or change the fallback below.
PREMIUM_KEY = str(secret("PREMIUM_ACCESS_KEY") or "TUBEFORGE-PREMIUM-2026")

FREE_GENERATIONS = 2  # free Claude calls per visitor session


def is_premium() -> bool:
    return bool(st.session_state.get("premium"))


def generations_used() -> int:
    return int(st.session_state.get("gen_count", 0))


def can_generate() -> bool:
    return is_premium() or generations_used() < FREE_GENERATIONS


def record_generation():
    st.session_state["gen_count"] = generations_used() + 1


def paywall_notice():
    st.warning(
        f"🔒 You've used your {FREE_GENERATIONS} free generates. "
        "Upgrade to Premium in the sidebar, then enter your access key to unlock unlimited generates."
    )


def render_sidebar():
    with st.sidebar:
        st.markdown("## 🔺 TubeForge")
        if is_premium():
            st.success("💎 Premium unlocked — unlimited generates.")
            return
        left = max(FREE_GENERATIONS - generations_used(), 0)
        st.markdown(f"**Free plan:** {left} of {FREE_GENERATIONS} free generates left")
        st.progress(left / FREE_GENERATIONS if FREE_GENERATIONS else 0.0)
        st.link_button(
            "🚀 Upgrade to Premium for Unlimited Generates",
            STRIPE_CHECKOUT_URL,
            type="primary",
            use_container_width=True,
        )
        st.caption("After payment you'll receive your access key.")
        entered = st.text_input("Enter Premium Access Key", type="password", key="premium_key_input")
        if entered:
            if entered == PREMIUM_KEY:
                st.session_state["premium"] = True
                st.rerun()
            else:
                st.error("Invalid access key.")


# ------------------------------------------------------------------ schemas

NICHE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "niche_name", "overall_score", "verdict", "competition", "monetization",
        "audience_profile", "sub_niches", "video_ideas", "red_flags",
    ],
    "properties": {
        "niche_name": {"type": "string"},
        "overall_score": {"type": "integer", "description": "0-100 viability score for a brand-new faceless creator"},
        "verdict": {"type": "string", "description": "2-3 sentence bottom line: should a beginner enter this niche, and how"},
        "competition": {
            "type": "object",
            "additionalProperties": False,
            "required": ["level", "analysis"],
            "properties": {
                "level": {"type": "string", "enum": ["low", "medium", "high"]},
                "analysis": {"type": "string"},
            },
        },
        "monetization": {
            "type": "object",
            "additionalProperties": False,
            "required": ["estimated_rpm", "revenue_streams"],
            "properties": {
                "estimated_rpm": {"type": "string", "description": "Typical AdSense RPM range, e.g. '$4-$12'"},
                "revenue_streams": {"type": "array", "items": {"type": "string"}},
            },
        },
        "audience_profile": {"type": "string"},
        "sub_niches": {
            "type": "array",
            "description": "3-5 sharper sub-niches with less competition",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["name", "why_it_works", "difficulty"],
                "properties": {
                    "name": {"type": "string"},
                    "why_it_works": {"type": "string"},
                    "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]},
                },
            },
        },
        "video_ideas": {
            "type": "array",
            "description": "5 first-video ideas optimized for a channel with zero subscribers",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["title", "hook", "format"],
                "properties": {
                    "title": {"type": "string"},
                    "hook": {"type": "string", "description": "The first 10 seconds, written out"},
                    "format": {"type": "string"},
                },
            },
        },
        "red_flags": {"type": "array", "items": {"type": "string"}},
    },
}

SCRIPT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["hook", "structure", "retention_devices", "cta", "tone_and_pacing", "reusable_template"],
    "properties": {
        "hook": {
            "type": "object",
            "additionalProperties": False,
            "required": ["text", "technique", "why_it_works"],
            "properties": {
                "text": {"type": "string", "description": "The exact opening lines quoted from the transcript"},
                "technique": {"type": "string", "description": "Named technique, e.g. curiosity gap, open loop, bold claim"},
                "why_it_works": {"type": "string"},
            },
        },
        "structure": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["segment", "purpose", "retention_tactic"],
                "properties": {
                    "segment": {"type": "string"},
                    "purpose": {"type": "string"},
                    "retention_tactic": {"type": "string"},
                },
            },
        },
        "retention_devices": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["device", "example"],
                "properties": {
                    "device": {"type": "string"},
                    "example": {"type": "string"},
                },
            },
        },
        "cta": {
            "type": "object",
            "additionalProperties": False,
            "required": ["placement", "approach"],
            "properties": {
                "placement": {"type": "string"},
                "approach": {"type": "string"},
            },
        },
        "tone_and_pacing": {"type": "string"},
        "reusable_template": {"type": "array", "items": {"type": "string"}},
    },
}

# ------------------------------------------------------------------ prompts

NICHE_SYSTEM = """You are TubeForge, an expert YouTube strategist who specializes in FACELESS channels run by beginners using AI production workflows (AI voiceover, stock/AI footage, outsourced editing).

Analyze niches for someone with: zero subscribers, no camera, small budget, and the goal of building a monetizable channel business — not going viral once. Judge niches on: search + browse demand, competition saturation for newcomers, RPM and non-AdSense monetization, content repeatability (can a beginner ship 2-3 videos/week with AI tools), and longevity (evergreen vs trend-dependent).

Be honest and specific. If a niche is saturated or low-RPM, say so and steer toward sharper sub-niches. Never invent fake statistics — give realistic ranges and label them as estimates."""

SCRIPT_SYSTEM = """You are TubeForge's script analyst. You dissect transcripts of successful YouTube videos and reverse-engineer WHY they hold attention.

You will receive a transcript (and possibly a title). Extract the anatomy: the hook and its named technique, the segment-by-segment structure, the retention devices (open loops, pattern interrupts, payoff previews, re-hooks, curiosity resets), the CTA strategy, and the tone/pacing. Then distill it into a reusable fill-in-the-blank template a beginner could follow with a completely different topic.

Quote the transcript directly when citing hooks and examples. If the transcript is too short or clearly not a video transcript, still do your best but note limitations inside the relevant fields."""

REVERSE_SYSTEM = """You are TubeForge's reverse-engineering engine. You take (a) a niche analysis and/or (b) a script blueprint extracted from a proven video, and transplant the proven mechanics into a NEW niche for a beginner faceless creator.

Produce a complete launch package in clean Markdown with these sections:

# The Play
One paragraph: the new niche angle and why the proven mechanics transfer to it.

# Channel Blueprint
Channel name ideas (3), positioning statement, target viewer, upload cadence a solo beginner can sustain with AI tools.

# The First Video
A full, ready-to-record script for video #1 — written word-for-word for an AI voiceover, with [VISUAL] cues for stock/AI footage. Apply the extracted hook technique and retention devices at the same structural beats. Aim for a 6-8 minute video (roughly 900-1200 spoken words).

# Why Each Beat Works
A short table mapping each script beat to the retention mechanic it borrows from the source blueprint.

# Next 5 Videos
Titles + one-line hooks that build on video #1.

Write the script in a natural spoken voice — contractions, short sentences, no corporate filler. Never promise specific income results."""

# ------------------------------------------------------------------ Claude calls


def structured_call(client, system: str, user_text: str, schema: dict) -> dict:
    with client.messages.stream(
        model=MODEL,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=system,
        messages=[{"role": "user", "content": user_text}],
        output_config={"format": {"type": "json_schema", "schema": schema}},
    ) as stream:
        msg = stream.get_final_message()
    if msg.stop_reason == "refusal":
        raise RuntimeError("The model declined this request.")
    text = next((b.text for b in msg.content if b.type == "text"), "")
    return json.loads(text)


def reverse_stream(client, user_text: str):
    with client.messages.stream(
        model=MODEL,
        max_tokens=32000,
        thinking={"type": "adaptive"},
        system=REVERSE_SYSTEM,
        messages=[{"role": "user", "content": user_text}],
    ) as stream:
        yield from stream.text_stream


def show_api_error(err: Exception):
    if isinstance(err, anthropic.AuthenticationError):
        st.error("Invalid Anthropic API key — check the ANTHROPIC_API_KEY secret in your Streamlit app settings.")
    elif isinstance(err, anthropic.RateLimitError):
        st.error("Rate limited by the Claude API — wait a moment and retry.")
    elif isinstance(err, anthropic.APIError):
        st.error(f"Claude API error: {err.message}")
    else:
        st.error(f"Error: {err}")


# ------------------------------------------------------------------ renderers


def render_niche(r: dict):
    c1, c2 = st.columns([1, 3])
    with c1:
        st.metric("Viability score", f"{r['overall_score']} / 100")
        st.progress(min(max(int(r["overall_score"]), 0), 100) / 100)
    with c2:
        st.markdown('<div class="tf-label">Verdict</div>', unsafe_allow_html=True)
        st.write(md(r["verdict"]))

    c1, c2 = st.columns(2)
    with c1, st.container(border=True):
        st.markdown(f'<div class="tf-label">Competition</div>{tag(r["competition"]["level"])}', unsafe_allow_html=True)
        st.write(md(r["competition"]["analysis"]))
    with c2, st.container(border=True):
        st.markdown('<div class="tf-label">Monetization</div>', unsafe_allow_html=True)
        st.write(f"**Est. RPM:** {md(r['monetization']['estimated_rpm'])}")
        for s in r["monetization"]["revenue_streams"]:
            st.markdown(f"- {md(s)}")

    c1, c2 = st.columns(2)
    with c1, st.container(border=True):
        st.markdown('<div class="tf-label">Audience</div>', unsafe_allow_html=True)
        st.write(md(r["audience_profile"]))
    with c2, st.container(border=True):
        st.markdown('<div class="tf-label">Red flags</div>', unsafe_allow_html=True)
        for s in r["red_flags"] or ["None noted."]:
            st.markdown(f"- {md(s)}")

    with st.container(border=True):
        st.markdown('<div class="tf-label">Sharper sub-niches</div>', unsafe_allow_html=True)
        for s in r["sub_niches"]:
            st.markdown(f"**{s['name']}** {tag(s['difficulty'])}", unsafe_allow_html=True)
            st.caption(md(s["why_it_works"]))

    with st.container(border=True):
        st.markdown('<div class="tf-label">First-video ideas (built for 0 subscribers)</div>', unsafe_allow_html=True)
        for v in r["video_ideas"]:
            st.markdown(f"**{md(v['title'])}**  ·  _{md(v['format'])}_")
            st.markdown(f'<div class="tf-quote">{v["hook"]}</div>', unsafe_allow_html=True)


def render_xray(r: dict):
    with st.container(border=True):
        st.markdown(f'<div class="tf-label">The hook — {r["hook"]["technique"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tf-quote">{r["hook"]["text"]}</div>', unsafe_allow_html=True)
        st.caption(md(r["hook"]["why_it_works"]))

    c1, c2 = st.columns(2)
    with c1, st.container(border=True):
        st.markdown('<div class="tf-label">Structure map</div>', unsafe_allow_html=True)
        for s in r["structure"]:
            st.markdown(f"🔴 **{md(s['segment'])}** — {md(s['purpose'])}")
            st.caption(f"🧲 {md(s['retention_tactic'])}")
    with c2, st.container(border=True):
        st.markdown('<div class="tf-label">Retention devices</div>', unsafe_allow_html=True)
        for d in r["retention_devices"]:
            st.markdown(f"**{md(d['device'])}**")
            st.markdown(f'<div class="tf-quote">{d["example"]}</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1, st.container(border=True):
        st.markdown('<div class="tf-label">CTA strategy</div>', unsafe_allow_html=True)
        st.write(f"**Placement:** {md(r['cta']['placement'])}")
        st.write(f"**Approach:** {md(r['cta']['approach'])}")
    with c2, st.container(border=True):
        st.markdown('<div class="tf-label">Tone &amp; pacing</div>', unsafe_allow_html=True)
        st.write(md(r["tone_and_pacing"]))

    with st.container(border=True):
        st.markdown('<div class="tf-label">Reusable template</div>', unsafe_allow_html=True)
        for i, step in enumerate(r["reusable_template"], 1):
            st.markdown(f"**{i}.** {md(step)}")


# ------------------------------------------------------------------ app

if not access_gate():
    st.stop()

client = get_client()
render_sidebar()

st.markdown(
    """
<div class="tf-hero">
  <span class="tf-pill">AI POWERED</span>
  <h1>The AI Copilot For Your<br/><span class="tf-red">First Faceless Channel</span></h1>
  <p class="tf-sub">TubeForge analyzes niches, X-rays the scripts behind winning videos — hooks,
  structure, retention — and reverse-engineers them into a launch plan and a ready-to-record
  script for <em>your</em> new channel. No camera. No guesswork.</p>
  <p class="tf-fine">Powered by Claude Opus 4.8 · Results are estimates, not guarantees.</p>
</div>
""",
    unsafe_allow_html=True,
)

if client is None:
    st.error(
        "No ANTHROPIC_API_KEY configured. On Streamlit Community Cloud: app menu → Settings → Secrets → add\n\n"
        '`ANTHROPIC_API_KEY = "sk-ant-api03-..."`'
    )
    st.stop()

tab1, tab2, tab3 = st.tabs(["🎯  1 · Niche Analyzer", "🧬  2 · Script X-Ray", "⚡  3 · Reverse Engineer"])

# ---------------- Step 1
with tab1:
    st.caption("Type a niche you're considering. TubeForge judges it like a strategist, not a cheerleader.")
    niche = st.text_input("Niche", placeholder='e.g. "AI tools tutorials", "sleep music", "true crime shorts"', label_visibility="collapsed")
    if st.button("Analyze Niche", type="primary"):
        if not niche.strip():
            st.warning("Type a niche first.")
        elif not can_generate():
            paywall_notice()
        else:
            with st.spinner("Analyzing niche with Claude — this takes ~30–60s…"):
                try:
                    st.session_state["niche_analysis"] = structured_call(
                        client, NICHE_SYSTEM,
                        f'Analyze this niche for a brand-new faceless YouTube channel: "{niche.strip()}"',
                        NICHE_SCHEMA,
                    )
                    record_generation()
                except Exception as e:
                    show_api_error(e)
    if st.session_state.get("niche_analysis"):
        render_niche(st.session_state["niche_analysis"])
        st.success("Done — move to **2 · Script X-Ray** next.")

# ---------------- Step 2
with tab2:
    st.caption("Find a successful video in (or near) your niche, copy its transcript from YouTube, and paste it here.")
    title = st.text_input("Video title (optional)")
    transcript = st.text_area("Transcript", height=260, placeholder="Paste the full video transcript here…")
    if st.button("X-Ray This Script", type="primary"):
        if len(transcript.strip()) < 100:
            st.warning("Paste a fuller transcript — at least a few paragraphs.")
        elif not can_generate():
            paywall_notice()
        else:
            with st.spinner("X-raying the script — extracting hook, structure, retention…"):
                try:
                    user_text = (f"Video title: {title.strip()}\n\n" if title.strip() else "") + f'Transcript:\n"""\n{transcript.strip()}\n"""'
                    st.session_state["script_blueprint"] = structured_call(client, SCRIPT_SYSTEM, user_text, SCRIPT_SCHEMA)
                    record_generation()
                except Exception as e:
                    show_api_error(e)
    if st.session_state.get("script_blueprint"):
        render_xray(st.session_state["script_blueprint"])
        st.success("Blueprint extracted — move to **3 · Reverse Engineer**.")

# ---------------- Step 3
with tab3:
    st.caption("TubeForge combines your niche analysis + the extracted blueprint into a launch package and full first script.")
    na = st.session_state.get("niche_analysis")
    sb = st.session_state.get("script_blueprint")
    c1, c2 = st.columns(2)
    c1.markdown(("✅ Niche analysis: **" + na["niche_name"] + "**") if na else "◽ Niche analysis: not loaded")
    c2.markdown(("✅ Script blueprint: **" + sb["hook"]["technique"] + "**") if sb else "◽ Script blueprint: not loaded")

    target = st.text_input("Your new target niche", value=(na["niche_name"] if na else ""))
    notes = st.text_input("Optional notes — audience, language, video length…")

    if st.button("⚡ Generate My Launch Package", type="primary"):
        if not target.strip():
            st.warning("Enter the new target niche.")
        elif not na and not sb:
            st.warning("Run Step 1 or Step 2 first — there's nothing to reverse-engineer yet.")
        elif not can_generate():
            paywall_notice()
        else:
            parts = [f'New target niche: "{target.strip()}"']
            if na:
                parts.append("Niche analysis (JSON):\n" + json.dumps(na, indent=2))
            if sb:
                parts.append("Proven script blueprint (JSON):\n" + json.dumps(sb, indent=2))
            if notes.strip():
                parts.append(f"Creator notes: {notes.strip()}")
            try:
                st.session_state["launch_package"] = st.write_stream(reverse_stream(client, "\n\n".join(parts)))
                record_generation()
                st.success("Launch package complete. Copy it and start recording. 🎬")
            except Exception as e:
                show_api_error(e)

    if st.session_state.get("launch_package"):
        st.download_button(
            "⬇ Download launch package (.md)",
            st.session_state["launch_package"],
            file_name="tubeforge-launch-package.md",
        )

st.divider()
st.caption("🔺 TubeForge — built for beginner faceless creators. Results are not typical; individual results will vary.")
