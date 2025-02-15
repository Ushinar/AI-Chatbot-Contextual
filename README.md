# My ChatBot

A Streamlit-based chatbot application utilizing the `OllamaLLM` language model. This app is designed to be a friendly and helpful AI chatbot with customizable primary context.

## Note

To use the current model, you need to install `ollama` and pull the model.

## Features

- **Streamlit Integration**: Utilizes Streamlit for an interactive web interface.
- **Customizable Context**: Allows users to set a primary context for the chatbot.
- **Session Management**: Maintains chat history and context within user sessions.
- **Model Flexibility**: The language model (LLM) can be changed as per requirements.

## Installation

1. **Clone the Repository**:

2. **Install Dependencies**:
    ```sh
    pip install streamlit langchain_ollama
    ```

## Usage

1. **Run the Application**:
    ```sh
    streamlit run app.py
    ```

2. **Interacting with the ChatBot**:
    - Open the Streamlit app in your browser.
    - Set the primary context for the chatbot.
    - Start chatting!

## Code Overview

- **`app.py`**: The main application file.
    - **Imports**: Imports necessary modules and initializes the language model.
    - **Configuration**: Configures the Streamlit app layout and title.
    - **Session Management**: Initializes session state variables.
    - **Primary Context Input**: Allows the user to set a primary context for the chatbot.
    - **Chat Display**: Displays chat messages from the session state.
    - **Chat Input**: Handles user input and generates responses using the LLM.
    - **Response Streaming**: Streams the response from the language model.
    - **Input Limitation**: Limits the number of messages and warns the user when the limit is reached.

## Customization

To change the language model (LLM) as per your requirements, update the following line in `app.py`:

```python
llm = OllamaLLM(model="your_desired_model")
