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

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1c;
    color: white;
}

/* Hide Streamlit header */
header {visibility: hidden;}
footer {visibility: hidden;}

/* HERO BACKGROUND EFFECT */
.hero {
    position: relative;
    text-align: center;
    padding: 120px 20px;
    overflow: hidden;
}

/* Soft animated gradient glow */
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

/* Subtle animated grid overlay */
.hero::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
    z-index: 0;
}

/* Animation */
@keyframes pulse {
    0% { transform: translateX(-50%) scale(1); opacity: 0.6; }
    50% { transform: translateX(-50%) scale(1.1); opacity: 0.9; }
    100% { transform: translateX(-50%) scale(1); opacity: 0.6; }
}

.hero > * {
    position: relative;
    z-index: 2;
}

.logo-wrapper {
    position: relative;
    display: inline-block;
}

.logo-wrapper::before {
    content: "";
    position: absolute;
    width: 650px;
    height: 650px;
    background: radial-gradient(circle, rgba(0,191,255,0.35) 0%, rgba(0,123,255,0.2) 40%, transparent 70%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    filter: blur(140px);
    z-index: -1;
    animation: pulseGlow 8s ease-in-out infinite;
}

.logo {
    width: 480px;
    margin-bottom: 60px;
    filter: drop-shadow(0 0 20px rgba(0,191,255,0.8))
            drop-shadow(0 0 40px rgba(0,123,255,0.6))
            drop-shadow(0 0 80px rgba(0,191,255,0.5));
    animation: floatLogo 6s ease-in-out infinite;
}

@keyframes floatLogo {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

@keyframes pulseGlow {
    0% { opacity: 0.6; }
    50% { opacity: 1; }
    100% { opacity: 0.6; }
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

# --- HERO ---
st.markdown(f"""
<div class="hero">
    <div class="logo-wrapper">
    <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
    <h1>Secure. Scalable. Future Ready.</h1>
    <p>Enterprise IT infrastructure engineered for performance, protection, and reliability.</p>
    <a href="mailto:info@skytechenterprise.co.za" class="button">Contact Us</a>
</div>
""", unsafe_allow_html=True)

# --- ROLLING TEXT ---
st.markdown("""
<div class="marquee">
    <div class="track">
        VMWARE • PROXMOX • VEEAM BACKUPS • PALO ALTO FIREWALLS • CISCO NETWORKING • MIKROTIK ROUTING • ENTERPRISE VPN SOLUTIONS • CYBER SECURITY • NETWORK ARCHITECTURE • CLOUD VIRTUALIZATION • VMWARE • PROXMOX • VEEAM BACKUPS • NGINX • HOME NETWORKS • COMPUTERS • SERVERS • ESXI •
    </div>
</div>
""", unsafe_allow_html=True)

# --- ABOUT ---
st.markdown("""
<div class="section">
<h2>About Sky Tech Enterprise</h2>

<p>
Sky Tech Enterprise Pty Ltd is a technology focused IT solutions company dedicated to designing, securing, and optimizing enterprise infrastructure for modern businesses. We specialize in cybersecurity, virtualization, advanced networking, and managed IT services that support operational stability and long term growth.
</p>

<p>
We architect environments using VMware and Proxmox virtualization platforms to deliver scalable, high availability infrastructure. Backup and disaster recovery strategies are implemented using Veeam to ensure critical data remains protected and recoverable.
</p>

<p>
Network architecture is engineered using Cisco and MikroTik technologies to provide structured VLAN segmentation, secure WAN connectivity, and enterprise VPN solutions.
</p>

<p>
Security is integrated at every layer. We deploy and manage Palo Alto firewall platforms to enforce traffic inspection, threat prevention, and perimeter defense aligned with ISC2 cybersecurity principles.
</p>

<p>
From virtualization clusters to hardened firewalls and secure remote access, Sky Tech Enterprise builds resilient systems that allow businesses to operate with confidence and scale with certainty.
</p>

</div>
""", unsafe_allow_html=True)

# --- SERVICES ---
st.markdown('<div class="section"><h2>Core Services</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>Cyber Security</h3><p>Palo Alto deployment, threat monitoring, secure architecture.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Networking</h3><p>Cisco switching, MikroTik routing, VLAN segmentation, VPNs.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Virtualization</h3><p>VMware and Proxmox infrastructure design and optimization.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Backup & Recovery</h3><p>Veeam backup solutions and disaster recovery planning.</p></div>', unsafe_allow_html=True)

# --- CONTACT SECTION ---
st.markdown("""
<div class="section">
    <div class="contact-box">
        <h2>Contact Us</h2>
        <p>For enterprise IT solutions and cybersecurity services:</p>
        <a href="mailto:info@skytechenterprise.co.za" class="contact-email">
            info@skytechenterprise.co.za
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("© 2026 Sky Tech Enterprise Pty Ltd")
