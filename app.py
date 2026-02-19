import streamlit as st

# Page config
st.set_page_config(
    page_title="Sky Tech Enterprise(PTY)LTD",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS Bands
st.markdown("""
<style>
.hero {
    background-color: #0f172a;
    padding: 60px;
    border-radius: 10px;
    text-align: center;
    color: white;
}
.services {
    background-color: #f1f5f9;
    padding: 40px;
    border-radius: 10px;
}
.contact {
    background-color: #e2e8f0;
    padding: 40px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# HERO BAND
st.markdown("""
<div class="hero">
    <h1>Sky Tech Enterprise (PTY) LTD</h1>
    <h3>Smart IT Infrastructure. Secure Networks. Reliable Systems.</h3>
</div>
""", unsafe_allow_html=True)

st.write("")

# SERVICES BAND
st.markdown('<div class="services">', unsafe_allow_html=True)

st.header("Our Services")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Infrastructure")
    st.write("""
    - VMware environments  
    - Windows & Linux servers  
    - Backup and disaster recovery  
    - Virtualization design  
    """)

with col2:
    st.subheader("Networking")
    st.write("""
    - Cisco and MikroTik configuration  
    - Firewall and security hardening  
    - VLAN and routing design  
    - ISP failover solutions  
    """)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# CONTACT BAND
st.markdown('<div class="contact">', unsafe_allow_html=True)

st.header("Contact Us")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent successfully")
    else:
        st.error("Please complete all fields")

st.markdown('</div>', unsafe_allow_html=True)
