import streamlit as st

from database.db_manager import get_text_count, init_db, insert_text

# Initialize database
init_db()

st.title("📥 Add Text Data")

# Show current text count
text_count = get_text_count()
st.info(f"📊 Currently stored: {text_count} text entries")

# Create form for input
with st.form("add_text_form"):
    st.subheader("📝 Document Information")
    
    # Input fields
    title = st.text_input("📖 Title:", placeholder="Enter document title...")
    
    genre = st.selectbox("📚 Genre:", ["Article", "Book", "Other"])
    
    author = st.text_input("✍️ Author:", placeholder="Enter author name...")
    
    content = st.text_area("📄 Content:", height=300, placeholder="Type or paste your text content here...")
    
    # Submit button
    submitted = st.form_submit_button("💾 Save Document", type="primary")
    
    if submitted:
        if title.strip() and author.strip() and content.strip():
            insert_text(title.strip(), genre, author.strip(), content.strip())
            st.success("✅ Document saved to database!")
            st.rerun()  # Refresh to show updated count
        else:
            st.warning("⚠️ Please fill in all required fields (Title, Author, and Content).")

# Show recent entries info
if text_count > 0:
    st.subheader("📋 Recent Entries")
    st.info("Your documents have been successfully stored and will be available for chat queries.")
