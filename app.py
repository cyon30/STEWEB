import streamlit as st

st.set_page_config(page_title="Sky Tech Enterprise", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1c;
    color: white;
}

.hero {
    text-align: center;
    padding: 120px 20px;
}

.hero h1 {
    font-size: 60px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    opacity: 0.8;
}

.button {
    display: inline-block;
    margin-top: 30px;
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
    font-size: 36px;
    font-weight: 600;
    padding: 20px 0;
}

.track {
    display: inline-block;
    padding-left: 100%;
    animation: scroll 20s linear infinite;
}

@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

.section {
    padding: 80px 0;
    max-width: 1000px;
    margin: auto;
    line-height: 1.8;
    font-size: 18px;
}

.card {
    background: #11182b;
    padding: 30px;
    border-radius: 12px;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
    <h1>Secure. Scalable. Future Ready.</h1>
    <p>Enterprise IT infrastructure built for performance and protection.</p>
    <a href="#" class="button">Talk to Us</a>
</div>
""", unsafe_allow_html=True)

# --- ROLLING TEXT ---
st.markdown("""
<div class="marquee">
    <div class="track">
        CYBER SECURITY • CLOUD INFRASTRUCTURE • NETWORK ENGINEERING • MANAGED IT SERVICES • CYBER SECURITY • CLOUD INFRASTRUCTURE •
    </div>
</div>
""", unsafe_allow_html=True)

# --- ABOUT SECTION ---
st.markdown("""
<div class="section">
<h2>About Sky Tech Enterprise</h2>
<p>
Sky Tech Enterprise Pty Ltd is a technology driven IT solutions company focused on building secure, scalable, and future ready infrastructure for modern businesses. We specialize in cybersecurity, enterprise networking, cloud virtualization, and managed IT services that keep organizations running without disruption.
</p>
<p>
Our approach is direct and disciplined. We analyze your environment, identify risk, design resilient architecture, and implement with precision. Security is built into every layer of the network to ensure performance, protection, and long term stability.
</p>
</div>
""", unsafe_allow_html=True)

# --- SERVICES ---
st.markdown('<div class="section"><h2>Our Services</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>Cyber Security</h3><p>Firewall deployment, monitoring, endpoint protection, and risk control.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Networking</h3><p>Enterprise routing, switching, VLAN design, secure connectivity.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Cloud & Virtualization</h3><p>VMware environments, hybrid cloud, infrastructure optimization.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Managed IT Services</h3><p>Proactive monitoring and business continuity planning.</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("© 2026 Sky Tech Enterprise Pty Ltd")
