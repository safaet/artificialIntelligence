import streamlit as st

def chat_interface():
    st.title("Chat with Your Data")
    st.write("Welcome to the chat interface! You can ask questions about your data here.")
    
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        if user_input:
            # Here you would typically process the user input and generate a response
            response = f"You said: {user_input}"  # Placeholder response
            st.write(f"Bot: {response}")
        else:
            st.warning("Please enter a message before sending.")

if __name__ == "__main__":
    chat_interface()