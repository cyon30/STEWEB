import streamlit as st
import base64
import requests
import feedparser
from datetime import datetime
from zoneinfo import ZoneInfo
import time as _time


st.set_page_config(page_title="Sky Tech Enterprise", layout="wide", page_icon="⚡")

# --- LOAD LOGO ---
def get_base64_logo(path):
    try:
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()
    except:
        return ""

logo_base64 = get_base64_logo("logo.png")

# --- LIVE ZAR/USD EXCHANGE RATE ---
@st.cache_data(ttl=300)  # Refresh every 5 minutes
def get_zar_usd():
    try:
        r = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=4
        )
        data = r.json()
        zar = data["rates"]["ZAR"]
        return round(zar, 2)
    except Exception:
        return None

zar_rate = get_zar_usd()
if zar_rate:
    zar_display = f"R{zar_rate:.2f}"
    zar_sub = "R per $1 USD"
else:
    zar_display = "R--"
    zar_sub = "ZAR / USD"

# --- LIVE BTC PRICE IN ZAR ---
@st.cache_data(ttl=180)  # Refresh every 3 minutes
def get_btc_zar():
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=zar",
            timeout=4
        )
        data = r.json()
        price = data["bitcoin"]["zar"]
        if price >= 1_000_000:
            return f"R{price/1_000_000:.2f}M"
        return f"R{price:,.0f}"
    except Exception:
        return None

btc_zar = get_btc_zar() or "R--"

# --- SERVER-SIDE TIMES (no JS needed, always works in Streamlit) ---
_now = datetime.now(ZoneInfo("UTC"))
et_time  = _now.astimezone(ZoneInfo("America/New_York")).strftime("%H:%M")
il_time  = _now.astimezone(ZoneInfo("Asia/Jerusalem")).strftime("%H:%M")

# Threats counter: grows ~3 per minute since a fixed epoch
_base_threats = 14_382
_minutes_elapsed = int(_time.time() // 60) - 28_300_000
threats_display = f"{_base_threats + max(0, _minutes_elapsed * 3):,}"

# --- LIVE ETH PRICE IN ZAR ---
@st.cache_data(ttl=180)
def get_eth_zar():
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=zar",
            timeout=4
        )
        price = r.json()["ethereum"]["zar"]
        return f"R{price:,.0f}"
    except Exception:
        return None

eth_zar = get_eth_zar() or "R--"

# --- CYBER NEWS: The Hacker News RSS ---
@st.cache_data(ttl=600)  # Refresh every 10 min
def get_cyber_news(limit=6):
    try:
        feed = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")
        items = []
        for e in feed.entries[:limit]:
            items.append({
                "title": e.get("title", ""),
                "link":  e.get("link", "#"),
                "date":  e.get("published", "")[:16]
            })
        return items
    except Exception:
        return []

cyber_news = get_cyber_news()

# --- LATEST CVEs from NIST NVD ---
@st.cache_data(ttl=900)  # Refresh every 15 min
def get_cves(limit=4):
    try:
        r = requests.get(
            "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=4&startIndex=0",
            timeout=6,
            headers={"User-Agent": "SkyTechEnterprise/1.0"}
        )
        data = r.json()
        items = []
        for v in data.get("vulnerabilities", [])[:limit]:
            cve   = v["cve"]
            cid   = cve["id"]
            desc  = cve["descriptions"][0]["value"][:120] + "..."
            score_data = cve.get("metrics", {})
            # Try CVSS v3.1 then v3.0 then v2
            score = "N/A"
            sev   = "UNKNOWN"
            for key in ["cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
                if key in score_data:
                    s = score_data[key][0].get("cvssData", {})
                    score = s.get("baseScore", "N/A")
                    sev   = s.get("baseSeverity", score_data[key][0].get("baseSeverity", "N/A"))
                    break
            items.append({"id": cid, "desc": desc, "score": score, "severity": sev})
        return items
    except Exception:
        return []

cves = get_cves()


# --- GLOBAL CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Inter:wght@300;400;600;700&display=swap');

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
    background-color: #020712 !important;
    color: #e0e8ff;
}

/* Hide Streamlit chrome */
header, footer, #MainMenu { visibility: hidden !important; }

/* CRITICAL: Force true full-width centering — Streamlit adds left padding by default */
.stApp {
    width: 100vw !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow-x: hidden;
}

.block-container {
    padding: 0 !important;
    max-width: 100vw !important;
    width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
}

/* Remove Streamlit's inner left-side gap */
[data-testid="stAppViewContainer"] > section {
    padding: 0 !important;
}

[data-testid="stVerticalBlock"] {
    gap: 0 !important;
    width: 100% !important;
}

.element-container, .stMarkdown {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
    text-align: center !important;
}

/* ============================
   MATRIX RAIN CANVAS
============================ */
#matrix-canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 0;
    opacity: 0.07;
    pointer-events: none;
}

/* ============================
   SCANLINE OVERLAY
============================ */
.scanlines {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 1;
    pointer-events: none;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0, 191, 255, 0.015) 2px,
        rgba(0, 191, 255, 0.015) 4px
    );
}

/* ============================
   CONTENT WRAPPER
============================ */
.content-wrapper {
    position: relative;
    z-index: 10;
    text-align: center;
    width: 100%;
}

/* Force ALL direct stMarkdown children to be block-level full width */
.element-container > .stMarkdown {
    display: block !important;
    width: 100% !important;
    text-align: center !important;
}

/* Force .section to always fill the full wrapper width so margin:auto works */
.stMarkdown > div {
    width: 100% !important;
    display: block !important;
}

/* ============================
   HERO SECTION
============================ */
.hero {
    position: relative;
    padding: 100px 20px 120px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    min-height: 100vh;
}

/* Radial glow burst */
.hero::before {
    content: "";
    position: absolute;
    width: 900px;
    height: 900px;
    background: radial-gradient(circle, rgba(0,191,255,0.22) 0%, rgba(120,0,255,0.1) 40%, transparent 70%);
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    filter: blur(80px);
    animation: pulseGlow 5s ease-in-out infinite;
    z-index: 0;
}

@keyframes pulseGlow {
    0%   { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
    50%  { opacity: 1;   transform: translate(-50%, -50%) scale(1.15); }
    100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
}

.hero > * { position: relative; z-index: 2; }

/* Status badge */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0,191,255,0.08);
    border: 1px solid rgba(0,191,255,0.3);
    border-radius: 50px;
    padding: 8px 20px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 2px;
    color: #00BFFF;
    text-transform: uppercase;
    margin-bottom: 30px;
}

.status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #00ff88;
    box-shadow: 0 0 8px #00ff88;
    animation: blink 1.2s ease-in-out infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.2; }
}

/* Logo container — adds glowing corona ring behind logo */
.logo-wrap {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 55px;
}

/* Outer corona pulse ring */
.logo-wrap::before {
    content: "";
    position: absolute;
    width: 560px;
    height: 560px;
    border-radius: 50%;
    background: radial-gradient(circle,
        rgba(0,191,255,0.18) 0%,
        rgba(0,80,255,0.08) 40%,
        transparent 70%);
    filter: blur(30px);
    animation: coronaPulse 4s ease-in-out infinite;
    z-index: 0;
    max-width: 90vw;
    max-height: 90vw;
}

/* Inner sharp ring */
.logo-wrap::after {
    content: "";
    position: absolute;
    width: 480px;
    height: 480px;
    border-radius: 50%;
    border: 1px solid rgba(0,191,255,0.12);
    box-shadow:
        0 0 40px rgba(0,191,255,0.15),
        inset 0 0 40px rgba(0,191,255,0.05);
    animation: coronaPulse 4s ease-in-out infinite reverse;
    z-index: 0;
    max-width: 88vw;
    max-height: 88vw;
}

@keyframes coronaPulse {
    0%, 100% { opacity: 0.6; transform: scale(1); }
    50%       { opacity: 1;   transform: scale(1.08); }
}

/* Logo */
.logo {
    width: 480px;
    max-width: 75vw;
    display: block;
    position: relative;
    z-index: 2;
    animation: floatLogo 5s ease-in-out infinite;
    filter:
        brightness(1.5)
        drop-shadow(0 0 8px rgba(255,255,255,0.95))
        drop-shadow(0 0 25px rgba(0,191,255,1))
        drop-shadow(0 0 60px rgba(0,191,255,0.8))
        drop-shadow(0 0 120px rgba(0,191,255,0.45));
}

@keyframes floatLogo {
    0%   { transform: translateY(0px); }
    50%  { transform: translateY(-14px); }
    100% { transform: translateY(0px); }
}

/* Glitch Headline */
.glitch-wrap {
    position: relative;
    display: inline-block;
    margin-bottom: 10px;
}

.hero-headline {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(2.2rem, 5vw, 4rem);
    font-weight: 900;
    color: #ffffff;
    letter-spacing: 3px;
    text-transform: uppercase;
    line-height: 1.1;
    text-shadow:
        0 0 20px rgba(0,191,255,0.8),
        0 0 40px rgba(0,191,255,0.4);
    animation: glitch 4s infinite;
    display: block;
    text-align: center;
}

@keyframes glitch {
    0%, 94%, 100% {
        text-shadow: 0 0 20px rgba(0,191,255,0.8), 0 0 40px rgba(0,191,255,0.4);
        transform: translate(0);
    }
    95% {
        text-shadow: -3px 0 #ff003c, 3px 0 #00BFFF;
        transform: translate(-2px, 1px);
    }
    96% {
        text-shadow: 3px 0 #ff003c, -3px 0 #00BFFF;
        transform: translate(2px, -1px);
    }
    97% {
        text-shadow: -2px 0 #ff003c, 2px 0 #00BFFF;
        transform: translate(0px, 1px);
    }
}

/* Typewriter sub-headline — looping type → hold → erase → hold → repeat */
.typewriter-line {
    font-family: 'Share Tech Mono', monospace;
    font-size: clamp(0.85rem, 2vw, 1.1rem);
    color: #00BFFF;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 18px auto 0;
    display: inline-block;
    text-align: center;
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #00BFFF;
    /* Total loop: 3s type + 1s hold + 2s erase + 0.5s pause = 6.5s */
    animation:
        typeLoop 6.5s steps(44, end) infinite,
        blink-cursor 0.65s step-end infinite;
}

@keyframes typeLoop {
    /*  0% → 46%  : type out  (3s of 6.5s) */
    0%   { width: 0; }
    46%  { width: 100%; }
    /* 46% → 61.5% : hold full (1s) */
    61.5%{ width: 100%; }
    /* 61.5% → 92% : erase     (2s) */
    92%  { width: 0; }
    /* 92% → 100%  : hold empty pause (0.5s) */
    100% { width: 0; }
}

@keyframes blink-cursor {
    from, to { border-color: transparent; }
    50%       { border-color: #00BFFF; }
}

/* Hero paragraph */
.hero-sub {
    font-size: clamp(0.95rem, 1.8vw, 1.15rem);
    color: rgba(180,210,255,0.75);
    max-width: 680px;
    margin: 30px auto 0;
    line-height: 1.8;
    text-align: center;
}

/* Stat bar */
.stat-row {
    display: flex;
    justify-content: center;
    gap: 28px;
    margin: 50px auto 0;
    flex-wrap: wrap;
    max-width: 960px;
}

.stat-item {
    text-align: center;
}

.stat-num {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.8rem;
    font-weight: 900;
    color: #00BFFF;
    text-shadow: 0 0 15px rgba(0,191,255,0.7);
}

.stat-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 2px;
    color: rgba(180,210,255,0.5);
    text-transform: uppercase;
    margin-top: 4px;
}

/* CTA Button */
.cta-wrap { margin-top: 50px; text-align: center; }

.button {
    display: inline-block;
    padding: 16px 40px;
    background: linear-gradient(135deg, #00BFFF 0%, #0057ff 100%);
    color: #ffffff !important;
    border-radius: 6px;
    text-decoration: none !important;
    font-family: 'Orbitron', sans-serif;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    box-shadow:
        0 0 30px rgba(0,191,255,0.5),
        inset 0 1px 0 rgba(255,255,255,0.15);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.button::before {
    content: "";
    position: absolute;
    top: -50%; left: -75%;
    width: 50%; height: 200%;
    background: rgba(255,255,255,0.15);
    transform: skewX(-20deg);
    transition: left 0.5s ease;
}

.button:hover::before { left: 150%; }

.button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 50px rgba(0,191,255,0.85), inset 0 1px 0 rgba(255,255,255,0.2);
}

.button-outline {
    display: inline-block;
    padding: 14px 36px;
    background: transparent;
    color: #00BFFF !important;
    border: 1px solid rgba(0,191,255,0.6);
    border-radius: 6px;
    text-decoration: none !important;
    font-family: 'Orbitron', sans-serif;
    font-weight: 700;
    font-size: 0.8rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-left: 16px;
    transition: all 0.3s ease;
}
.button-outline:hover {
    background: rgba(0,191,255,0.08);
    border-color: #00BFFF;
    box-shadow: 0 0 25px rgba(0,191,255,0.3);
    transform: translateY(-3px);
}

/* ============================
   SECTION BASE
============================ */
.section {
    padding: 100px 40px;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
    box-sizing: border-box;
}

.section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 4px;
    color: #00BFFF;
    text-transform: uppercase;
    margin-bottom: 12px;
    display: block;
    text-align: center;
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(1.6rem, 3.5vw, 2.6rem);
    font-weight: 900;
    color: #ffffff;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 16px;
    text-align: center;
    text-shadow: 0 0 30px rgba(0,191,255,0.3);
}

.section-sub {
    font-size: 1rem;
    color: rgba(180,210,255,0.6);
    max-width: 600px;
    margin: 0 auto 60px;
    line-height: 1.8;
    text-align: center;
}

/* Divider */
.neon-divider {
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #00BFFF, transparent);
    margin: 0 auto 20px;
    border: none;
    box-shadow: 0 0 10px rgba(0,191,255,0.6);
}

/* ============================
   TECH STACK GRID
============================ */
.tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin-top: 40px;
}

/* ============================
   CARD
============================ */
.card {
    position: relative;
    background: linear-gradient(135deg, rgba(10,20,45,0.95), rgba(5,12,28,0.98));
    padding: 36px 30px;
    border-radius: 12px;
    border: 1px solid rgba(0,191,255,0.15);
    overflow: hidden;
    transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
    text-align: center;
}

.card::before {
    content: "";
    position: absolute;
    top: 0; left: -100%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,191,255,0.06), transparent);
    animation: cardSweep 4s ease-in-out infinite;
}

@keyframes cardSweep {
    0%   { left: -100%; }
    50%  { left: 150%; }
    100% { left: -100%; }
}

.card::after {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, #00BFFF, transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.card:hover::after { opacity: 1; }
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 60px rgba(0,191,255,0.2), 0 0 30px rgba(0,191,255,0.1);
    border-color: rgba(0,191,255,0.4);
}

.card-icon {
    font-size: 2.5rem;
    margin-bottom: 16px;
    display: block;
    filter: drop-shadow(0 0 8px rgba(0,191,255,0.5));
}

.card h3 {
    font-family: 'Orbitron', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #ffffff;
    margin-bottom: 12px;
    text-align: center;
}

.card p {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.82rem;
    color: rgba(150,200,255,0.7);
    line-height: 1.7;
    letter-spacing: 0.5px;
    text-align: center;
    margin: 0 auto;
}

/* Tag chips inside cards */
.tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    justify-content: center;
    margin-top: 14px;
}

.tag {
    background: rgba(0,191,255,0.08);
    border: 1px solid rgba(0,191,255,0.25);
    border-radius: 4px;
    padding: 3px 10px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    color: #00BFFF;
    letter-spacing: 1px;
}

/* ============================
   TERMINAL ABOUT BLOCK
============================ */
.terminal {
    background: #020c18;
    border: 1px solid rgba(0,191,255,0.2);
    border-radius: 12px;
    padding: 0;
    max-width: 860px;
    margin: 40px auto 0;
    overflow: hidden;
    box-shadow: 0 0 60px rgba(0,191,255,0.08);
    text-align: left;
}

.terminal-bar {
    background: rgba(0,191,255,0.06);
    padding: 12px 18px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid rgba(0,191,255,0.1);
}

.t-dot { width: 12px; height: 12px; border-radius: 50%; }
.t-red   { background: #ff5f57; }
.t-yellow{ background: #febc2e; }
.t-green { background: #28c840; }

.terminal-title {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: rgba(180,210,255,0.4);
    letter-spacing: 2px;
    margin-left: 10px;
}

.terminal-body {
    padding: 28px 30px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.85rem;
    line-height: 2;
    color: rgba(180,215,255,0.75);
}

.terminal-body .prompt { color: #00ff88; }
.terminal-body .cmd    { color: #00BFFF; }
.terminal-body .output { color: rgba(180,215,255,0.65); padding-left: 18px; display: block; }
.terminal-body .comment{ color: rgba(100,160,255,0.4); }

/* ============================
   SERVICES GRID
============================ */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-top: 40px;
}

.service-card {
    position: relative;
    background: linear-gradient(135deg, rgba(10,20,45,0.95), rgba(5,12,28,0.98));
    padding: 40px 30px;
    border-radius: 12px;
    border: 1px solid rgba(0,191,255,0.12);
    overflow: hidden;
    transition: all 0.35s ease;
    text-align: center;
}

.service-card::before {
    content: "";
    position: absolute;
    bottom: 0; left: 0;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, #00BFFF, transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.service-card:hover::before { opacity: 1; }
.service-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 60px rgba(0,191,255,0.15);
    border-color: rgba(0,191,255,0.35);
}

.service-icon {
    font-size: 2.8rem;
    display: block;
    margin-bottom: 20px;
    filter: drop-shadow(0 0 10px rgba(0,191,255,0.5));
}

.service-card h3 {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #ffffff;
    margin-bottom: 12px;
    text-align: center;
}

.service-card p {
    font-size: 0.88rem;
    color: rgba(150,200,255,0.65);
    line-height: 1.8;
    text-align: center;
    margin: 0 auto;
}

/* ============================
   FOOTER CTA
============================ */
.footer-cta {
    padding: 120px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.footer-cta::before {
    content: "";
    position: absolute;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(0,191,255,0.12), transparent 70%);
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    filter: blur(60px);
    pointer-events: none;
}

.footer-cta > * { position: relative; z-index: 2; }

.footer-bar {
    background: rgba(0,191,255,0.04);
    border-top: 1px solid rgba(0,191,255,0.1);
    padding: 30px 20px;
    text-align: center;
}

.footer-copy {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: rgba(180,210,255,0.3);
    letter-spacing: 2px;
    text-transform: uppercase;
    text-align: center;
}

/* ============================
   CYBER INTEL SECTION
============================ */

/* Scrolling news ticker */
.ticker-wrap {
    width: 100%;
    background: rgba(0,191,255,0.04);
    border-top: 1px solid rgba(0,191,255,0.15);
    border-bottom: 1px solid rgba(0,191,255,0.15);
    padding: 12px 0;
    overflow: hidden;
    position: relative;
    margin-bottom: 50px;
}

.ticker-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.68rem;
    color: #00BFFF;
    letter-spacing: 3px;
    text-transform: uppercase;
    background: rgba(0,191,255,0.12);
    border-right: 1px solid rgba(0,191,255,0.3);
    padding: 0 14px;
    position: absolute;
    left: 0; top: 0; bottom: 0;
    display: flex;
    align-items: center;
    z-index: 2;
}

.ticker-track {
    display: flex;
    white-space: nowrap;
    animation: tickerScroll 40s linear infinite;
    padding-left: 140px;
}

.ticker-track:hover { animation-play-state: paused; }

@keyframes tickerScroll {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

.ticker-item {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.78rem;
    color: rgba(180,215,255,0.8);
    padding: 0 40px 0 0;
    letter-spacing: 0.5px;
}

.ticker-item::before {
    content: "▶";
    color: #00BFFF;
    margin-right: 10px;
    font-size: 0.6rem;
}

.ticker-item a {
    color: rgba(180,215,255,0.8);
    text-decoration: none;
}

.ticker-item a:hover { color: #00BFFF; }

/* CVE Cards */
.cve-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
    margin-top: 30px;
    text-align: left;
}

.cve-card {
    background: linear-gradient(135deg, rgba(10,20,45,0.95), rgba(5,12,28,0.98));
    border: 1px solid rgba(0,191,255,0.12);
    border-radius: 10px;
    padding: 20px 22px;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s ease, border-color 0.3s ease;
    text-align: left;
}

.cve-card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,191,255,0.35);
}

.cve-id {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: #00BFFF;
    letter-spacing: 2px;
    margin-bottom: 8px;
    display: block;
}

.cve-desc {
    font-size: 0.82rem;
    color: rgba(180,210,255,0.65);
    line-height: 1.6;
    margin-bottom: 12px;
}

.cve-score {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 1px;
    font-weight: 700;
}

.sev-CRITICAL { background: rgba(220,20,60,0.2);  color: #ff4466; border: 1px solid rgba(220,20,60,0.4); }
.sev-HIGH     { background: rgba(255,100,0,0.15); color: #ff7733; border: 1px solid rgba(255,100,0,0.35); }
.sev-MEDIUM   { background: rgba(255,200,0,0.1);  color: #ffcc00; border: 1px solid rgba(255,200,0,0.3); }
.sev-LOW      { background: rgba(0,191,255,0.08); color: #00BFFF; border: 1px solid rgba(0,191,255,0.2); }
.sev-UNKNOWN  { background: rgba(120,120,140,0.1);color: #888;    border: 1px solid rgba(120,120,140,0.2); }
.sev-NA       { background: rgba(120,120,140,0.1);color: #888;    border: 1px solid rgba(120,120,140,0.2); }

/* News Cards */
.news-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 14px;
    margin-top: 20px;
}

.news-card {
    background: linear-gradient(135deg, rgba(10,20,45,0.9), rgba(5,12,28,0.95));
    border: 1px solid rgba(0,191,255,0.1);
    border-radius: 8px;
    padding: 16px 18px;
    transition: all 0.3s ease;
    text-decoration: none;
    display: block;
    text-align: left;
}

.news-card:hover {
    border-color: rgba(0,191,255,0.35);
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,191,255,0.1);
}

.news-card-title {
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    color: rgba(220,235,255,0.9);
    line-height: 1.5;
    margin-bottom: 6px;
}

.news-card-date {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.68rem;
    color: rgba(0,191,255,0.5);
    letter-spacing: 1px;
}

[data-testid="column"] > div {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

/* Comprehensive stMarkdown centering */
.stMarkdown { text-align: center !important; width: 100% !important; }
.stMarkdown > div { width: 100% !important; }
.stMarkdown p { text-align: center !important; max-width: 100% !important; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { text-align: center !important; }

/* Force all content sections to full width */
.content-wrapper, .hero, .section, .footer-cta, .footer-bar {
    width: 100% !important;
    box-sizing: border-box !important;
}

</style>

<!-- Matrix rain canvas -->
<canvas id="matrix-canvas"></canvas>
<div class="scanlines"></div>

<script>
(function() {
    const canvas = document.getElementById('matrix-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
    const chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノ';
    const fontSize = 13;
    const cols = Math.floor(canvas.width / fontSize);
    const drops = Array(cols).fill(1);
    function draw() {
        ctx.fillStyle = 'rgba(2,7,18,0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#00BFFF';
        ctx.font = fontSize + 'px Share Tech Mono, monospace';
        for (let i = 0; i < drops.length; i++) {
            const text = chars[Math.floor(Math.random() * chars.length)];
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 45);
})();
</script>
""", unsafe_allow_html=True)


# =============================================
# HERO
# =============================================
logo_img = f'<img src="data:image/png;base64,{logo_base64}" class="logo" alt="Sky Tech Enterprise Logo">' if logo_base64 else ""
logo_html = f'<div class="logo-wrap">{logo_img}</div>' if logo_img else ""

st.markdown(f"""
<div class="content-wrapper">
<div class="hero">
    <div class="status-badge">
        <span class="status-dot"></span>
        Systems Online &nbsp;•&nbsp; 24/7 Support Active
    </div>
    {logo_html}
    <div class="glitch-wrap">
        <span class="hero-headline">Secure. Scalable.<br>Future-Ready.</span>
    </div>
    <span class="typewriter-line">ENTERPRISE IT INFRASTRUCTURE // POWERED UP</span>
    <p class="hero-sub">
        Next-generation IT infrastructure engineered for peak performance,
        ironclad protection, and infinite scalability. We keep your systems
        alive — always.
    </p>
    <div class="stat-row">
        <div class="stat-item">
            <div class="stat-num">99.9%</div>
            <div class="stat-label">Uptime SLA</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">24/7</div>
            <div class="stat-label">NOC Monitoring</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">0-DAY</div>
            <div class="stat-label">Threat Response</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">ISO</div>
            <div class="stat-label">Compliant Stack</div>
        </div>
        <div class="stat-item">
            <div class="stat-num" style="font-size:1.4rem;">{zar_display}</div>
            <div class="stat-label">ZAR / USD</div>
        </div>
        <div class="stat-item">
            <div class="stat-num" style="font-size:1.3rem;">&#8383; {btc_zar}</div>
            <div class="stat-label">BTC in ZAR</div>
        </div>
        <div class="stat-item">
            <div class="stat-num" style="font-size:1.4rem;">{et_time}</div>
            <div class="stat-label">&#127482;&#127480; USA (ET)</div>
        </div>
        <div class="stat-item">
            <div class="stat-num" style="font-size:1.4rem;">{il_time}</div>
            <div class="stat-label">&#127470;&#127473; Israel (IST)</div>
        </div>
        <div class="stat-item">
            <div class="stat-num" style="font-size:1.3rem;">{threats_display}</div>
            <div class="stat-label">&#128737; Threats Blocked</div>
        </div>
        <div class="stat-item">
            <div class="stat-num" style="font-size:1.3rem;">&#926; {eth_zar}</div>
            <div class="stat-label">ETH in ZAR</div>
        </div>
    </div>
    <div class="cta-wrap">
        <a href="mailto:info@skytechenterprise.co.za" class="button">&#9889; Engage Now</a>
        <a href="#services" class="button-outline">View Services</a>
    </div>
</div>
</div>
""", unsafe_allow_html=True)


# =============================================
# CYBER INTELLIGENCE FEED
# =============================================

# Build ticker HTML (doubled for seamless infinite scroll)
_ticker_items = "".join(
    f'<span class="ticker-item"><a href="{n["link"]}" target="_blank">{n["title"]}</a></span>'
    for n in cyber_news
) if cyber_news else '<span class="ticker-item">Loading threat intelligence...</span>'
_ticker_html = _ticker_items + _ticker_items

# Build CVE cards
def _sev_class(s):
    s = str(s).upper()
    return f"sev-{s}" if s in ("CRITICAL","HIGH","MEDIUM","LOW") else "sev-UNKNOWN"

_cve_cards = ""
for c in cves:
    _cve_cards += f"""
    <div class="cve-card">
        <span class="cve-id">{c['id']}</span>
        <p class="cve-desc">{c['desc']}</p>
        <span class="cve-score {_sev_class(c['severity'])}">
            CVSS {c['score']} &nbsp;|&nbsp; {c['severity']}
        </span>
    </div>"""

if not _cve_cards:
    _cve_cards = '<div class="cve-card"><span class="cve-id">LOADING...</span><p class="cve-desc">CVE data fetching from NIST NVD...</p></div>'

# Build news cards
_news_cards = ""
for n in cyber_news:
    _news_cards += f"""
    <a class="news-card" href="{n['link']}" target="_blank" rel="noopener">
        <div class="news-card-title">{n['title']}</div>
        <div class="news-card-date">{n['date']}</div>
    </a>"""

if not _news_cards:
    _news_cards = '<div class="news-card"><div class="news-card-title">Fetching latest cyber news...</div></div>'

_cyber_html = """
<div class="content-wrapper">

<div class="ticker-wrap">
    <span class="ticker-label">&#128308; LIVE INTEL</span>
    <div class="ticker-track">
        TICKER_PLACEHOLDER
    </div>
</div>

<div class="section">
    <span class="section-label">// Threat Intelligence</span>
    <h2 class="section-title">Live Cyber Intelligence</h2>
    <hr class="neon-divider">
    <p class="section-sub">Real-time vulnerability disclosures and breaking cybersecurity news &mdash; powered by NIST NVD &amp; The Hacker News.</p>

    <span class="section-label" style="margin-top:10px;">&#9888; Latest CVEs &mdash; NIST NVD</span>
    <div class="cve-grid">
        CVE_PLACEHOLDER
    </div>

    <span class="section-label" style="margin-top:50px; display:block;">&#128240; Cybersecurity Headlines</span>
    <div class="news-grid">
        NEWS_PLACEHOLDER
    </div>
</div>
</div>
""".replace("TICKER_PLACEHOLDER", _ticker_html)\
   .replace("CVE_PLACEHOLDER", _cve_cards)\
   .replace("NEWS_PLACEHOLDER", _news_cards)

st.markdown(_cyber_html, unsafe_allow_html=True)


# =============================================
# TECHNOLOGY STACK
# =============================================

st.markdown("""
<div class="content-wrapper">
<div class="section">
    <span class="section-label">// Core Infrastructure</span>
    <h2 class="section-title">Technology Stack</h2>
    <hr class="neon-divider">
    <p class="section-sub">Battle-tested enterprise technologies deployed at scale — chosen for reliability, security, and raw performance.</p>
    <div class="tech-grid">
        <div class="card">
            <span class="card-icon">🖥️</span>
            <h3>Virtualization</h3>
            <p>Enterprise hypervisors and virtual infrastructure management for maximum resource efficiency.</p>
            <div class="tag-row">
                <span class="tag">VMware</span>
                <span class="tag">Proxmox</span>
                <span class="tag">ESXi</span>
                <span class="tag">vSAN</span>
            </div>
        </div>
        <div class="card">
            <span class="card-icon">🌐</span>
            <h3>Networking</h3>
            <p>Enterprise-grade routing, switching, and VLAN architecture built for mission-critical uptime.</p>
            <div class="tag-row">
                <span class="tag">Cisco</span>
                <span class="tag">MikroTik</span>
                <span class="tag">VLAN</span>
                <span class="tag">VPN</span>
            </div>
        </div>
        <div class="card">
            <span class="card-icon">🔐</span>
            <h3>Security &amp; Backup</h3>
            <p>Zero-trust perimeter security combined with enterprise-grade backup and disaster recovery.</p>
            <div class="tag-row">
                <span class="tag">Palo Alto</span>
                <span class="tag">Veeam</span>
                <span class="tag">Zero-Trust</span>
            </div>
        </div>
        <div class="card">
            <span class="card-icon">☁️</span>
            <h3>Hybrid Cloud</h3>
            <p>Seamless on-premise to cloud migration strategies with full infrastructure automation.</p>
            <div class="tag-row">
                <span class="tag">AWS</span>
                <span class="tag">Azure</span>
                <span class="tag">Terraform</span>
            </div>
        </div>
        <div class="card">
            <span class="card-icon">🐧</span>
            <h3>Linux Systems</h3>
            <p>Hardened Debian / Ubuntu server deployments, scripting, and system automation at scale.</p>
            <div class="tag-row">
                <span class="tag">Debian 12</span>
                <span class="tag">Ubuntu</span>
                <span class="tag">Bash</span>
                <span class="tag">Ansible</span>
            </div>
        </div>
        <div class="card">
            <span class="card-icon">📊</span>
            <h3>Monitoring</h3>
            <p>Real-time infrastructure observability — proactive alerting before problems reach your users.</p>
            <div class="tag-row">
                <span class="tag">Zabbix</span>
                <span class="tag">Grafana</span>
                <span class="tag">Prometheus</span>
            </div>
        </div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)


# =============================================
# ABOUT — TERMINAL BLOCK
# =============================================
st.markdown("""
<div class="content-wrapper">
<div class="section">
    <span class="section-label">// Who We Are</span>
    <h2 class="section-title">About Sky Tech Enterprise</h2>
    <hr class="neon-divider">
    <div class="terminal">
        <div class="terminal-bar">
            <span class="t-dot t-red"></span>
            <span class="t-dot t-yellow"></span>
            <span class="t-dot t-green"></span>
            <span class="terminal-title">root@skytech:~# about --verbose</span>
        </div>
        <div class="terminal-body">
            <span><span class="prompt">root@skytech</span>:<span class="cmd">~</span>$ cat mission.txt</span>
            <span class="output">Sky Tech Enterprise delivers secure and scalable enterprise IT infrastructure.</span>
            <span class="output">We specialize in VMware and Proxmox virtualization, Veeam backup strategies,</span>
            <span class="output">Cisco and MikroTik networking, Palo Alto firewall security, and enterprise VPN.</span>
            <br>
            <span><span class="prompt">root@skytech</span>:<span class="cmd">~</span>$ cat approach.txt</span>
            <span class="output">Our structured approach targets: performance, resilience, long-term risk reduction.</span>
            <span class="output">From virtualization clusters to hardened security infrastructure — we build</span>
            <span class="output">reliable systems that let businesses operate confidently and grow securely.</span>
            <br>
            <span class="comment"># Status: OPERATIONAL | Uptime: 99.99% | Threats Blocked: 14,382 | Last Audit: PASSED</span>
        </div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)


# =============================================
# CORE SERVICES
# =============================================
st.markdown("""
<div class="content-wrapper">
<div class="section" id="services">
    <span class="section-label">// What We Do</span>
    <h2 class="section-title">Core Services</h2>
    <hr class="neon-divider">
    <p class="section-sub">End-to-end IT solutions — from securing your perimeter to rebuilding your entire infrastructure stack.</p>
    <div class="services-grid">
        <div class="service-card">
            <span class="service-icon">🛡️</span>
            <h3>Cyber Security</h3>
            <p>Next-gen firewall deployment, real-time threat monitoring, zero-trust architecture, and hardened infrastructure design.</p>
        </div>
        <div class="service-card">
            <span class="service-icon">🌐</span>
            <h3>Networking</h3>
            <p>Enterprise routing and switching, VLAN segmentation, BGP/OSPF design, SD-WAN, and site-to-site VPN solutions.</p>
        </div>
        <div class="service-card">
            <span class="service-icon">🖥️</span>
            <h3>Virtualization</h3>
            <p>VMware and Proxmox infrastructure design, vSAN implementation, live migration, and hypervisor optimization.</p>
        </div>
        <div class="service-card">
            <span class="service-icon">💾</span>
            <h3>Backup &amp; Recovery</h3>
            <p>Veeam enterprise backup, offsite replication, automated DR failover, and RTO/RPO-compliant recovery testing.</p>
        </div>
        <div class="service-card">
            <span class="service-icon">🔧</span>
            <h3>IT Consulting</h3>
            <p>Infrastructure audits, capacity planning, technology roadmaps, and vendor-agnostic architecture recommendations.</p>
        </div>
        <div class="service-card">
            <span class="service-icon">📡</span>
            <h3>NOC Support</h3>
            <p>24/7 Network Operations Center monitoring, incident response, SLA-backed escalation, and proactive alerting.</p>
        </div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)


# =============================================
# FOOTER CTA
# =============================================
st.markdown("""
<div class="content-wrapper">
<div class="footer-cta">
    <span class="section-label">// Let's Build Together</span>
    <h2 class="section-title">Ready to Secure Your Infrastructure?</h2>
    <hr class="neon-divider">
    <p class="hero-sub">
        Partner with Sky Tech Enterprise for enterprise-grade virtualization,
        military-strength cybersecurity, and hyper-scalable networking solutions.
        Your infrastructure deserves nothing less.
    </p>
    <div class="cta-wrap" style="margin-top: 40px;">
        <a href="mailto:info@skytechenterprise.co.za" class="button">⚡ Get in Touch</a>
    </div>
</div>
<div class="footer-bar">
    <p class="footer-copy">© 2026 Sky Tech Enterprise (PTY) LTD &nbsp;•&nbsp; All Rights Reserved &nbsp;•&nbsp; Engineered in South Africa 🇿🇦</p>
</div>
</div>
""", unsafe_allow_html=True)
