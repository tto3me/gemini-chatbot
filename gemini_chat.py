import streamlit as st
import google.generativeai as genai
import antigravity # L'indispensable pour l'esprit du projet !

# 1. Configurer la page
st.set_page_config(page_title="Gemini Anti-Gravity", page_icon="🚀")
st.title("🛸 Gemini en apesanteur")

# 2. Sécuriser ta clé (à mettre dans un fichier .env ou secrets)
api_key = st.sidebar.text_input("Clé API Gemini", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Initialiser l'historique dans la session Streamlit
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Afficher les messages précédents
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Logique de chat
    if prompt := st.chat_input("Envoyez un message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
