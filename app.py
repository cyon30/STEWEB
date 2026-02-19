import streamlit as st

# Page config
st.set_page_config(
    page_title="Sky Tech Enterprise",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Services", "Contact"])

# Home Page
if page == "Home":
    st.title("Sky Tech Enterprise (PTY) LTD")
    st.subheader("Smart IT Solutions")
    st.success("Server is running")

    st.write("""
    We specialize in:
    - Server deployments
    - Networking solutions
    - Cyber security
    - Virtualization
    - Cloud integration
    """)

# Services Page
elif page == "Services":
    st.title("Our Services")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Infrastructure")
        st.write("""
        - VMware environments  
        - Windows & Linux servers  
        - Backup solutions  
        """)

    with col2:
        st.header("Networking")
        st.write("""
        - Cisco & MikroTik  
        - Firewall configuration  
        - VLAN design  
        """)

# Contact Page
elif page == "Contact":
    st.title("Contact Us")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully")
        else:
            st.error("Please fill in all fields")
