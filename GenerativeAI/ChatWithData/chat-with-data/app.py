import streamlit as st

from pages.AddText import *
from pages.Browse import *
from pages.Chat import *

# Configure page
st.set_page_config(
    page_title="Chat with Your Data",
    page_icon="💬",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("📚 Chat with Your Data")
page = st.sidebar.selectbox("Choose a page:", ["Add Text", "Browse Documents", "Chat"])

# Main content
if page == "Add Text":
    # AddText page content is imported and will run automatically
    pass
elif page == "Browse Documents":
    # Browse page content is imported and will run automatically
    pass
elif page == "Chat":
    # Chat page content is imported and will run automatically
    pass