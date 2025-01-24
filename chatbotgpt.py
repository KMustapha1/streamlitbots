import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)   

 # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
            max_tokens = 200,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})    

import streamlit as st
import openai

# Ajout d'un selectbox pour choisir le modèle GPT
st.title("ChatGPT-like clone")

# Liste des modèles disponibles
model_options = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-0125"
]

# Selectbox pour choisir un modèle
selected_model = st.selectbox("Choisissez un modèle GPT :", model_options)

# Utiliser le modèle sélectionné
st.write(f"Vous avez sélectionné le modèle : {selected_model}")

import streamlit as st
import openai

# Titre de l'application
st.title("ChatGPT-like clone")

# Liste des modèles GPT
model_options = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-0125"
]

# Selectbox pour choisir le modèle GPT
selected_model = st.selectbox(
    "Choisissez un modèle GPT :", 
    model_options, 
    key="model_selectbox"  # Clé unique pour éviter les conflits
)

# Slider pour sélectionner max_tokens
max_tokens = st.slider(
    "Choisissez le nombre maximum de jetons :",
    min_value=0,
    max_value=500,
    value=100,  # Valeur par défaut
    step=1,
    key="max_tokens_slider"  # Clé unique pour éviter les conflits
)

st.write(f"Modèle sélectionné : {selected_model}")
st.write(f"Nombre maximum de jetons sélectionné : {max_tokens}")  