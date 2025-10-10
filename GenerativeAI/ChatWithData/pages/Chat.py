import streamlit as st

from database.db_manager import get_all_texts, get_text_count, init_db
from services.llm_service import query_llm

# Initialize database
init_db()

st.title("💬 Chat with Your Data")

# Check if API key is configured
from config.settings import GROQ_API_KEY

if not GROQ_API_KEY or GROQ_API_KEY == "your_groq_api_key_here":
    st.error("⚠️ Please configure your GROQ API key in the .env file")
    st.info("1. Copy `.env.example` to `.env`\n2. Get a free API key from https://console.groq.com/\n3. Add your key to the `.env` file")
    st.stop()

# Show data statistics
text_count = get_text_count()
if text_count == 0:
    st.warning("📝 No documents found. Please add some documents first using the 'Add Text' page.")
    st.stop()

st.info(f"📊 Chatting with {text_count} documents")

# Get all documents
documents = get_all_texts()

# Display document summary
st.subheader("📚 Available Documents")
for i, (title, genre, author, content) in enumerate(documents[:5]):  # Show first 5
    with st.expander(f"📖 {title} by {author} ({genre})"):
        st.write(f"**Author:** {author}")
        st.write(f"**Genre:** {genre}")
        st.write(f"**Content Preview:** {content[:200]}...")

if len(documents) > 5:
    st.info(f"... and {len(documents) - 5} more documents")

# Chat interface
st.subheader("💬 Ask Questions")
question = st.text_input("Ask a question about your documents:", placeholder="What would you like to know about your stored documents?")

if st.button("🤖 Ask Question", type="primary"):
    if question.strip():
        with st.spinner("🤔 Thinking..."):
            # Create context from all documents
            context_parts = []
            for title, genre, author, content in documents:
                context_parts.append(f"Title: {title}\nAuthor: {author}\nGenre: {genre}\nContent: {content}")
            
            context = "\n\n---\n\n".join(context_parts)
            
            # Create a better prompt for the LLM
            prompt = f"""You are a helpful assistant that answers questions based on the provided documents. 

Documents:
{context}

Question: {question}

Please provide a helpful answer based on the documents above. If the question cannot be answered from the provided documents, please say so and suggest what information might be needed."""

            response = query_llm(prompt)
            
        st.subheader("🤖 Response:")
        st.write(response)
        
        # Show context used
        with st.expander("📄 Documents Used"):
            st.text_area("Context:", context, height=200, disabled=True, label_visibility="collapsed")
    else:
        st.warning("⚠️ Please enter a question.")
