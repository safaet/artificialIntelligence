import streamlit as st

from database.db_manager import (get_all_texts, get_text_count,
                                 get_texts_by_author, get_texts_by_genre,
                                 init_db, search_texts)

# Initialize database
init_db()

st.title("📚 Browse Documents")

# Show statistics
text_count = get_text_count()
if text_count == 0:
    st.warning("📝 No documents found. Please add some documents first using the 'Add Text' page.")
    st.stop()

st.info(f"📊 Total documents: {text_count}")

# Search and filter options
col1, col2, col3 = st.columns(3)

with col1:
    search_term = st.text_input("🔍 Search:", placeholder="Search by title, author, or content...")

with col2:
    genre_filter = st.selectbox("📚 Filter by Genre:", ["All", "Article", "Book", "Other"])

with col3:
    author_filter = st.text_input("✍️ Filter by Author:", placeholder="Enter author name...")

# Get filtered documents
if search_term:
    documents = search_texts(search_term)
    st.info(f"Found {len(documents)} documents matching '{search_term}'")
elif genre_filter != "All":
    documents = get_texts_by_genre(genre_filter)
    st.info(f"Found {len(documents)} {genre_filter.lower()} documents")
elif author_filter:
    documents = get_texts_by_author(author_filter)
    st.info(f"Found {len(documents)} documents by '{author_filter}'")
else:
    documents = get_all_texts()

# Display documents
if documents:
    st.subheader("📖 Document List")
    
    for i, (title, genre, author, content) in enumerate(documents):
        with st.expander(f"📖 {title} by {author} ({genre})"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Title:** {title}")
                st.write(f"**Author:** {author}")
                st.write(f"**Genre:** {genre}")
                st.write(f"**Content:** {content}")
            
            with col2:
                st.write(f"**Length:** {len(content)} characters")
                st.write(f"**Words:** {len(content.split())} words")
else:
    st.info("No documents found matching your criteria.")
