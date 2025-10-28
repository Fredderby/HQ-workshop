import streamlit as st
from feedback import hq_feedback
from connect import cred

# Set page configuration
st.set_page_config(page_title="Workshop App", page_icon="✍️", layout="centered")

with st.container(border=True):  
# Header and section selector
    st.image('./media/workshop.jpg')
 
    # Section selection
    # sections = st.selectbox("**SECTION OPTIONS**", ["Post Mission's], key="sect12")
    # Main function based on selection
   
    hq_feedback()
    
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}  # Hide the hamburger menu
    footer {visibility: hidden;}  # Hide the footer
    header {visibility: hidden;}  # Hide the header
    </style>
    """,
    unsafe_allow_html=True
)