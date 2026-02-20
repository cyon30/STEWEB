import streamlit as st
import base64

st.set_page_config(page_title="Sky Tech Enterprise", layout="wide")

# --- LOAD LOGO ---
def get_base64_logo(path):
    try:
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()
    except Exception:
        return ""

# --- CSS ---
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1c;
    color: white;
}

header {visibility: hidden;}
footer {visibility: hidden;}

/* HERO */
.hero {
    position: relative;
    min-height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    overflow: hidden;
}

.hero-content {
    position: relative;
    z-index: 2;
}

.hero-network {
    position: absolute;
    inset: 0;
    z-index: 0;
    opacity: 0.4;
}

.network-line {
    stroke: #00BFFF;
    stroke-width: 1.2;
    stroke-dasharray: 6;
    animation: dashMove 6s linear infinite;
}

@keyframes dashMove {
    from { stroke-dashoffset: 0; }
    to { stroke-dashoffset: -100; }
}

.network-node {
    fill: #00BFFF;
    animation: nodePulse 3s ease-in-out infinite;
}

@keyframes nodePulse {
    0% { opacity: 0.4; }
    50% { opacity: 1; }
    100% { opacity: 0.4; }
}


.hero > * {
    position: relative;
    z-index: 2;
}

/* Floating Logo */
.logo {
    width: 500px;
    margin-bottom: 80px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    animation: floatLogo 5s ease-in-out infinite;
    filter:
        drop-shadow(0 0 15px rgba(255,255,255,0.6))
        drop-shadow(0 0 30px rgba(0,191,255,0.8))
        drop-shadow(0 0 60px rgba(0,191,255,0.5));
}

@keyframes floatLogo {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

/* TEXT CENTER */
h1, h2, h3 {
    text-align: center;
}

p {
    text-align: center;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}

/* SECTION */
.section {
    padding: 100px 20px;
    max-width: 1100px;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}

/* Center Streamlit columns */
[data-testid="column"] > div {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* CARD */
.card {
    position: relative;
    background: rgba(15,22,41,0.9);
    padding: 40px;
    border-radius: 16px;
    margin: 20px auto;
    max-width: 420px;
    border: 1px solid rgba(0,191,255,0.2);
    overflow: hidden;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

/* Moving glow inside card */
.card::before {
    content: "";
    position: absolute;
    top: -150%;
    left: -50%;
    width: 200%;
    height: 300%;
    background: linear-gradient(
        120deg,
        transparent 0%,
        rgba(0,191,255,0.15) 40%,
        transparent 80%
    );
    transform: rotate(25deg);
    animation: sweep 6s linear infinite;
}

@keyframes sweep {
    0% { transform: translateX(-100%) rotate(25deg); }
    100% { transform: translateX(100%) rotate(25deg); }
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 40px rgba(0,191,255,0.4);
    border-color: rgba(0,191,255,0.6);
}

.button {
    display: inline-block;
    margin-top: 40px;
    padding: 14px 32px;
    background: linear-gradient(90deg, #00BFFF, #1e90ff);
    color: #ffffff;
    border-radius: 10px;
    text-decoration: none;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-shadow: 0 1px 2px rgba(0,0,0,0.4);
    box-shadow: 0 0 25px rgba(0,191,255,0.6);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.button:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 40px rgba(0,191,255,0.9);
}

</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown(f"""
<div class="hero">

    <div class="hero-network">
        <svg viewBox="0 0 1200 600" preserveAspectRatio="none">

            <line x1="100" y1="100" x2="500" y2="200" class="network-line"/>
            <line x1="500" y1="200" x2="900" y2="120" class="network-line"/>
            <line x1="300" y1="400" x2="700" y2="300" class="network-line"/>
            <line x1="700" y1="300" x2="1100" y2="450" class="network-line"/>
            <line x1="200" y1="250" x2="600" y2="500" class="network-line"/>

            <circle cx="100" cy="100" r="6" class="network-node"/>
            <circle cx="500" cy="200" r="6" class="network-node"/>
            <circle cx="900" cy="120" r="6" class="network-node"/>
            <circle cx="300" cy="400" r="6" class="network-node"/>
            <circle cx="700" cy="300" r="6" class="network-node"/>
            <circle cx="1100" cy="450" r="6" class="network-node"/>
            <circle cx="200" cy="250" r="6" class="network-node"/>
            <circle cx="600" cy="500" r="6" class="network-node"/>

        </svg>
    </div>

    <div class="hero-content">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
        <h1>Secure. Scalable. Future-Ready.</h1>
        <p>Enterprise IT infrastructure engineered for performance, protection, and reliability.</p>
        <a href="mailto:info@skytechenterprise.co.za" class="button">Contact Us</a>
    </div>

</div>
""", unsafe_allow_html=True)

# --- TECHNOLOGY STACK ---
st.markdown('<div class="section"><h2>Technology Stack</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware • Proxmox • ESXi • vSAN</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Networking</h3><p>Cisco • MikroTik • VLAN Architecture • Enterprise VPN</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>Security & Backup</h3><p>Palo Alto • Cyber Security • Veeam Backup</p></div>', unsafe_allow_html=True)

# --- ABOUT ---
st.markdown("""
<div class="section">
<h2>About Sky Tech Enterprise</h2>
<p>
Sky Tech Enterprise delivers secure and scalable enterprise IT infrastructure. We specialize in VMware and Proxmox virtualization, Veeam backup strategies, Cisco and MikroTik networking, Palo Alto firewall security, and enterprise VPN architecture.
</p>
<p>
Our structured approach focuses on performance, resilience, and long-term risk reduction. From virtualization clusters to hardened security design, we build reliable systems that enable businesses to operate confidently and grow securely.
</p>
</div>
""", unsafe_allow_html=True)

# --- SERVICES ---
st.markdown('<div class="section"><h2>Core Services</h2></div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="card"><h3>Cyber Security</h3><p>Firewall deployment, threat monitoring, secure infrastructure design.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Networking</h3><p>Enterprise routing, switching, VLAN segmentation, VPN solutions.</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware and Proxmox infrastructure optimization.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Backup & Recovery</h3><p>Veeam backup and disaster recovery planning.</p></div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="section">
<h2>Ready to Secure Your Infrastructure?</h2> <p style="opacity:0.8;"> Partner with Sky Tech Enterprise for scalable virtualization, secure networking, and enterprise cybersecurity solutions. </p> <a href="mailto:info@skytechenterprise.co.za" class="button">Get in Touch</a> </div>
<div>
<p style="opacity:0.6;">© 2026 Sky Tech Enterprise (PTY) LTD • All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
