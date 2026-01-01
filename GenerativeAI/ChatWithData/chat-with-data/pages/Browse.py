import streamlit as st
import os

def browse_documents():
    st.title("Browse Documents")
    st.write("Select a document to view its contents:")

    # Get a list of documents in a specific directory
    documents_dir = "path/to/your/documents"  # Update this path as needed
    documents = [f for f in os.listdir(documents_dir) if os.path.isfile(os.path.join(documents_dir, f))]

    # Allow user to select a document
    selected_document = st.selectbox("Choose a document:", documents)

    if selected_document:
        document_path = os.path.join(documents_dir, selected_document)
        with open(document_path, "r") as file:
            content = file.read()
            st.text_area("Document Content", content, height=300)

# Run the browse_documents function when this page is accessed
browse_documents()