import streamlit as st

# Page config
st.set_page_config(
    page_title="Sky Tech Enterprise(PTY)LTD",
    page_icon="🚀",
    layout="wide"
)

st.title("Sky Tech Enterprise (PTY) LTD")
st.subheader("Smart IT Solutions")

st.write("""
We specialize in:
- Server deployments
- Networking solutions
- Cyber security
- Virtualization
- Cloud integration
""")

st.divider()

st.header("Our Services")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Infrastructure")
    st.write("""
    - VMware environments
    - Windows & Linux servers
    - Backup solutions
    """)

with col2:
    st.subheader("Networking")
    st.write("""
    - Cisco & MikroTik
    - Firewall configuration
    - VLAN design
    """)

st.divider()

st.header("Contact Us")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully")
    else:
        st.error("Please fill in all fields")
