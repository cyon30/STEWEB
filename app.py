import streamlit as st
import base64

st.set_page_config(page_title="Sky Tech Enterprise", layout="wide")

# --- LOAD LOGO ---
def get_base64_logo(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_base64 = get_base64_logo("logo.png")

# --- CUSTOM CSS ---
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1c;
    color: white;
    text-align: center;
}

header {visibility: hidden;}
footer {visibility: hidden;}

/* HERO */
.hero {
    position: relative;
    padding: 120px 20px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.hero h1 {
    font-size: 60px;
    font-weight: 800;
    text-align: center;
}

.hero p {
    font-size: 20px;
    opacity: 0.85;
    margin-top: 20px;
    text-align: center;
    max-width: 800px;
}
.hero::before {
    content: "";
    position: absolute;
    width: 900px;
    height: 900px;
    background: radial-gradient(circle, rgba(0,123,255,0.25) 0%, rgba(0,191,255,0.15) 40%, transparent 70%);
    top: -200px;
    left: 50%;
    transform: translateX(-50%);
    filter: blur(120px);
    animation: pulse 8s ease-in-out infinite;
    z-index: 0;
}

@keyframes pulse {
    0% { transform: translateX(-50%) scale(1); opacity: 0.6; }
    50% { transform: translateX(-50%) scale(1.1); opacity: 0.9; }
    100% { transform: translateX(-50%) scale(1); opacity: 0.6; }
}

.hero > * {
    position: relative;
    z-index: 2;
}

.logo {
    width: 480px;
    margin-bottom: 60px;
    filter: drop-shadow(0 0 25px rgba(0,191,255,0.8))
            drop-shadow(0 0 60px rgba(0,123,255,0.6));
    animation: floatLogo 6s ease-in-out infinite;
}

@keyframes floatLogo {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

.hero h1 {
    font-size: 60px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    opacity: 0.85;
    margin-top: 20px;
}

.button {
    display: inline-block;
    margin-top: 40px;
    padding: 14px 30px;
    background: linear-gradient(90deg, #007BFF, #00BFFF);
    color: white;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}

/* SECTIONS */
.section {
    padding: 100px 0;
    max-width: 1000px;
    margin: auto;
    line-height: 1.9;
    font-size: 18px;
}

/* CARD STYLE WITH MOVING GLOW */
.card {
    position: relative;
    background: #0f1629;
    padding: 40px;
    border-radius: 16px;
    margin: 20px 0;
    overflow: hidden;
    border: 1px solid rgba(0,191,255,0.2);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

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
        rgba(0,191,255,0.08) 30%,
        rgba(0,191,255,0.25) 50%,
        rgba(0,191,255,0.08) 70%,
        transparent 100%
    );
    transform: rotate(25deg);
    animation: sweep 6s linear infinite;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 35px rgba(0,191,255,0.4);
    border-color: rgba(0,191,255,0.6);
}

@keyframes sweep {
    0% { transform: translateX(-100%) rotate(25deg); }
    100% { transform: translateX(100%) rotate(25deg); }
}

img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    filter: drop-shadow(0 0 40px rgba(0,191,255,0.4));
}

.footer {
    padding: 40px 0;
    opacity: 0.6;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown(f"""
<div class="hero">
    <img src="data:image/png;base64,{logo_base64}" class="logo">
    <h1>Secure. Scalable. Future-Ready.</h1>
    <p>Enterprise IT infrastructure engineered for performance, protection, and reliability.</p>
    <a href="mailto:info@skytechenterprise.co.za" class="button">Contact Us</a>
</div>
""", unsafe_allow_html=True)

# --- TECHNOLOGY STACK ---
st.markdown("""
<div class="section">
<h2>Technology Stack</h2>
<p style="opacity:0.7; margin-bottom:50px;">
Enterprise platforms and security technologies we engineer and support.
</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware • Proxmox • ESXi • vSAN</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Networking</h3><p>Cisco • MikroTik • VLAN Architecture • Enterprise VPN</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>Security & Backup</h3><p>Palo Alto • Cyber Security • Veeam Backup • Threat Prevention</p></div>', unsafe_allow_html=True)

# --- ABOUT ---
st.markdown("""
<div class="section">
<h2>About Sky Tech Enterprise</h2>
<p>
Sky Tech Enterprise Pty Ltd delivers secure and scalable enterprise IT infrastructure. We specialize in VMware and Proxmox virtualization, Veeam backup solutions, Cisco and MikroTik networking, Palo Alto firewall security, and enterprise VPN connectivity. Our structured approach focuses on performance, resilience, and risk reduction. From virtualization clusters to hardened security architecture, we build stable foundations that allow businesses to operate confidently and grow securely.
</p>
</div>
""", unsafe_allow_html=True)

# --- SERVICES ---
st.markdown('<div class="section"><h2>Core Services</h2></div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="card"><h3>Cyber Security</h3><p>Palo Alto Networks, threat monitoring, secure architecture.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Networking</h3><p>Cisco switching, MikroTik routing, VLAN segmentation, VPNs.</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware and Proxmox infrastructure design and optimization.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Backup & Recovery</h3><p>Veeam backup and disaster recovery solutions.</p></div>', unsafe_allow_html=True)

# --- AI SECTION ---
st.markdown("""
<div class="section">
<h2>Engineering the Future</h2>
<p style="opacity:0.7; max-width:700px; margin:auto;">
Strategic thinking. Intelligent infrastructure. Advanced cybersecurity.
We design systems that anticipate risk and evolve with your business.
</p>
</div>
""", unsafe_allow_html=True)

st.image("ai.png", use_container_width=True)

# --- FOOTER ---
st.markdown('<div class="footer">© 2026 Sky Tech Enterprise (PTY) LTD • All rights reserved.</div>', unsafe_allow_html=True)
