import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Sky Tech Enterprise", layout="wide")

# --- LOAD LOGO ---
def get_base64_logo(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_path = "logo.png"  # change if your file name differs
logo_base64 = get_base64_logo(logo_path)

# --- CUSTOM CSS ---
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1c;
    color: white;
}

header {visibility: hidden;}
footer {visibility: hidden;}

.hero {
    text-align: center;
    padding: 80px 20px 120px 20px;
}

.logo {
    width: 220px;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 60px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    opacity: 0.8;
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

.marquee {
    overflow: hidden;
    white-space: nowrap;
    background: #11182b;
    color: #00BFFF;
    font-size: 32px;
    font-weight: 600;
    padding: 25px 0;
}

.track {
    display: inline-block;
    padding-left: 100%;
    animation: scroll 25s linear infinite;
}

@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

.section {
    padding: 100px 0;
    max-width: 1000px;
    margin: auto;
    line-height: 1.9;
    font-size: 18px;
}

.section h2 {
    font-size: 42px;
    margin-bottom: 30px;
}

.card {
    background: #11182b;
    padding: 35px;
    border-radius: 14px;
    margin: 20px 0;
    transition: 0.3s;
}

.card:hover {
    background: #16203a;
}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown(f"""
<div class="hero">
    <img src="data:image/png;base64,{logo_base64}" class="logo">
    <h1>Secure. Scalable. Future Ready.</h1>
    <p>Enterprise IT infrastructure engineered for performance, protection, and reliability.</p>
    <a href="#" class="button">Contact Us</a>
</div>
""", unsafe_allow_html=True)

# --- ROLLING TECH STACK ---
st.markdown("""
<div class="marquee">
    <div class="track">
        VMWARE • PROXMOX • VEEAM BACKUPS • PALO ALTO FIREWALLS • CISCO NETWORKING • MIKROTIK ROUTING • ENTERPRISE VPN SOLUTIONS • CYBER SECURITY • NETWORK ARCHITECTURE • CLOUD VIRTUALIZATION • VMWARE • PROXMOX • VEEAM BACKUPS •
    </div>
</div>
""", unsafe_allow_html=True)

# --- ABOUT SECTION ---
st.markdown("""
<div class="section">
<h2>About Sky Tech Enterprise</h2>

<p>
Sky Tech Enterprise Pty Ltd is a technology focused IT solutions company dedicated to designing, securing, and optimizing enterprise infrastructure for modern businesses. We specialize in cybersecurity, virtualization, advanced networking, and managed IT services that support operational stability and long term growth.
</p>

<p>
We architect environments using VMware and Proxmox virtualization platforms to deliver scalable, high availability infrastructure. Whether deploying new clusters or optimizing existing environments, we focus on efficiency, uptime, and long term sustainability. Backup and disaster recovery strategies are implemented using Veeam to ensure critical data remains protected and recoverable at all times.
</p>

<p>
Network architecture is engineered using Cisco and MikroTik technologies to provide structured VLAN segmentation, secure WAN connectivity, and performance optimized routing environments. Secure remote access is delivered through enterprise VPN solutions that maintain encrypted communication between users, offices, and cloud resources.
</p>

<p>
Security is integrated at every layer. We deploy and manage Palo Alto firewall platforms to enforce traffic inspection, threat prevention, and perimeter defense. Risk mitigation strategies are aligned with industry best practices and informed by ISC2 Certified in Cybersecurity knowledge foundations.
</p>

<p>
Our process is structured and disciplined. Assess. Design. Implement. Support. From virtualization and backup infrastructure to hardened firewall deployments and secure networking, Sky Tech Enterprise builds resilient systems that allow businesses to operate with confidence and scale with certainty.
</p>

</div>
""", unsafe_allow_html=True)

# --- SERVICES SECTION ---
st.markdown('<div class="section"><h2>Core Services</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>Cyber Security</h3><p>Palo Alto firewall deployment, endpoint protection, risk mitigation, and secure access control.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Networking</h3><p>Cisco switching, MikroTik routing, VLAN segmentation, and enterprise VPN connectivity.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware and Proxmox infrastructure design, optimization, and cluster deployment.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Backup & Recovery</h3><p>Veeam backup solutions, disaster recovery planning, and business continuity strategies.</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("© 2026 Sky Tech Enterprise Pty Ltd")
