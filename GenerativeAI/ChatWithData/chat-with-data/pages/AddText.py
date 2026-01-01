import streamlit as st

def add_text():
    st.title("Add Text")
    st.write("This page allows you to add text data.")
    
    text_input = st.text_area("Enter your text here:")
    
    if st.button("Submit"):
        if text_input:
            st.success("Text added successfully!")
        else:
            st.error("Please enter some text before submitting.")

# Call the function to display the content
add_text()