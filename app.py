import streamlit as st
import base64

st.set_page_config(page_title="Sky Tech Enterprise", layout="wide")

# --- LOAD LOGO ---
def get_base64_logo(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_base64 = get_base64_logo("logo.png")

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

section.main > div {
    text-align: center;
}

/* HERO */
.hero {
    position: relative;
    padding: 140px 20px;
    overflow: hidden;
}

.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 30%, rgba(0,191,255,0.25), transparent 60%);
    animation: pulse 6s ease-in-out infinite;
    z-index: 0;
}

.hero::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
}

@keyframes pulse {
    0% { opacity: 0.5; }
    50% { opacity: 0.9; }
    100% { opacity: 0.5; }
}

.hero > * {
    position: relative;
    z-index: 2;
}

.logo {
    width: 420px;
    margin-bottom: 50px;
    filter: drop-shadow(0 0 25px rgba(0,191,255,0.8));
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

/* SECTION */
.section {
    padding: 100px 0;
    max-width: 1100px;
    margin: auto;
    line-height: 1.8;
    font-size: 18px;
}

/* GLOW CARDS */
.card {
    position: relative;
    background: rgba(15,22,41,0.85);
    padding: 40px;
    border-radius: 16px;
    margin: 20px 0;
    border: 1px solid rgba(0,191,255,0.2);
    backdrop-filter: blur(10px);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    overflow: hidden;
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
        rgba(0,191,255,0.15) 40%,
        transparent 80%
    );
    transform: rotate(25deg);
    animation: sweep 7s linear infinite;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 40px rgba(0,191,255,0.4);
}

@keyframes sweep {
    0% { transform: translateX(-100%) rotate(25deg); }
    100% { transform: translateX(100%) rotate(25deg); }
}

/* GRADIENT SECTION */
.tech-gradient {
    padding: 120px 20px;
    background: linear-gradient(135deg, #001f3f, #003366, #001a33);
    background-size: 400% 400%;
    animation: gradientShift 10s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* GLASS BANNER */
.glass-banner {
    margin: 100px auto;
    padding: 60px;
    max-width: 900px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(0,191,255,0.3);
}

/* FOOTER */
.footer {
    position: relative;
    padding: 80px 20px;
    background: #050a14;
}

.footer::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,191,255,0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,191,255,0.08) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: gridMove 15s linear infinite;
}

@keyframes gridMove {
    0% { background-position: 0 0; }
    100% { background-position: 40px 40px; }
}

.footer-content {
    position: relative;
    z-index: 2;
    opacity: 0.7;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# HERO
st.markdown(f"""
<div class="hero">
    <img src="data:image/png;base64,{logo_base64}" class="logo">
    <h1>Secure. Scalable. Future-Ready.</h1>
    <p>Enterprise IT infrastructure engineered for performance, protection, and reliability.</p>
    <a href="mailto:info@skytechenterprise.co.za" class="button">Contact Us</a>
</div>
""", unsafe_allow_html=True)

# TECHNOLOGY STACK
st.markdown('<div class="section"><h2>Technology Stack</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware • Proxmox • ESXi • vSAN</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Networking</h3><p>Cisco • MikroTik • VLAN Architecture • Enterprise VPN</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>Security & Backup</h3><p>Palo Alto • Cyber Security • Veeam Backup</p></div>', unsafe_allow_html=True)

# ABOUT
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

# SERVICES
st.markdown('<div class="section"><h2>Core Services</h2></div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="card"><h3>Cyber Security</h3><p>Firewall deployment, threat monitoring, secure infrastructure design.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Networking</h3><p>Enterprise routing, switching, VLAN segmentation, VPN solutions.</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware and Proxmox infrastructure optimization.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Backup & Recovery</h3><p>Veeam backup and disaster recovery planning.</p></div>', unsafe_allow_html=True)

# GRADIENT SECTION
st.markdown("""
<div class="tech-gradient">
<h2>Enterprise Infrastructure Engineered for Growth</h2>
<p style="max-width:800px; margin:auto; opacity:0.85;">
We architect resilient virtualization platforms, secure enterprise networks, and hardened security environments that enable modern businesses to operate without disruption.
</p>
</div>
""", unsafe_allow_html=True)

# GLASS CTA
st.markdown("""
<div class="glass-banner">
<h2>Ready to Secure Your Infrastructure?</h2>
<p style="opacity:0.8;">
Partner with Sky Tech Enterprise for scalable virtualization, secure networking, and enterprise cybersecurity solutions.
</p>
<a href="mailto:info@skytechenterprise.co.za" class="button">Get in Touch</a>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    <div class="footer-content">
        © 2026 Sky Tech Enterprise (PTY) LTD • All rights reserved.
    </div>
</div>
""", unsafe_allow_html=True)
