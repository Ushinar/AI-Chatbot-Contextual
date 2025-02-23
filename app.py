# Import necessary modules
import streamlit as st
import time
from langchain_ollama import OllamaLLM




# Initializing the OllamaLLM model with "llama3.2:1b"
llm = OllamaLLM(model="ushinar:1b")

# Configure Streamlit App
st.set_page_config(layout="wide")
st.title('My ChatBot')

# Button to start a new chat; resets chat messages and history
if st.button('Start New Chat', type='primary'):  # Create a "Start New Chat" button
    for key in list(st.session_state.keys()):  # Iterate over all keys in session state
            del st.session_state[key]  # Delete the session state key if the condition is met
    st.rerun()

# Initialize Session State
st.session_state.setdefault('messages', [])  # Initialize 'messages' as an empty list
st.session_state.setdefault('chat_history', [])  # Initialize 'chat_history' as an empty list
st.session_state.setdefault('primary_context', "This is a friendly and helpful AI chatbot.")  # Initialize file uploader key
st.session_state.setdefault('input_disabled', False)  # Initialize 'chat_disabled' as False

# Text input for setting the primary context for the chatbot
primary_context_input = st.text_input("Primary context for chatbot:", st.session_state.primary_context)
st.session_state.update(primary_context=primary_context_input)  # Updating the primary context in session state


# Loop to display chat messages from session state
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Chat input field for user to type messages
prompt = st.chat_input('Welcome! Start typing...', 
                       disabled=st.session_state.input_disabled, 
                       on_submit=lambda: st.session_state.update(input_disabled=True))
if prompt:  # If user has entered a message
    st.chat_message('user').markdown(prompt)  # Displaying user's message
    st.session_state.messages.append({'role': 'user', 'content': prompt})  # Adding user's message to session state
    st.session_state.chat_history.append({'role': 'user', 'content': prompt})  # Adding user's message to chat history
    # Creating the full prompt by combining primary context, chat history, and current user input
    prev_context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history[:-1]])
    full_prompt = f"""
*Primary context:
{primary_context_input}

*Chat history (ignore if blank):
{prev_context}

*Current user input:
{prompt}"""
    # Printing the input to the language model for debugging purposes
    print("\n\n**INPUT TO LLM**\n", full_prompt)
    response = ""  # Initializing the response variable
    placeholder = st.empty()  # Creating an empty placeholder for the assistant's response
    # Streaming the response from the language model
    for chunk in llm.stream(input=full_prompt):
        response += chunk  # Appending chunks of the response
        placeholder.chat_message('assistant').markdown(response)  # Displaying the assistant's response
        time.sleep(0.005)  # Adding a slight delay for streaming effect
    # Adding the assistant's response to session state
    st.session_state.messages.append({'role': 'assistant', 'content': response})
    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
    # Printing the response from the chatbot for debugging purposes
    print("\n\n**RESPONSE FROM CHATBOT**\n", response)
    st.session_state.update(input_disabled=False)  # Reset chat_disabled
    st.rerun()  # Rerun the app
     

# Disabling input if the number of messages reaches 10
if len(st.session_state.messages) == 10:
    st.session_state.input_disabled = True
# Displaying a warning if the number of messages reaches 12
if len(st.session_state.messages) == 12:
    st.warning("You have reached the limit of 6 chats. Please refresh your browser to continue.")
