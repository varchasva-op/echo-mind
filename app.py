# ============================================
# 🧠 OFFLINE MENTAL HEALTH CHATBOT – STABLE VERSION
# Fixes StreamlitAPIException for user_input clearing
# ============================================

import os
import streamlit as st
from gpt4all import GPT4All

# ----------- Model Path -----------
MODEL_PATH = r"C:\Users\alank\AppData\Local\nomic.ai\GPT4All\mistral-7b-instruct-v0.1.Q4_0.gguf"

# Check model path
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model not found at {MODEL_PATH}")

# Load GPT4All model (first time takes a minute)
model = GPT4All(MODEL_PATH)

# ----------- Streamlit Setup -----------
st.set_page_config(page_title="EcHo Mind: Mental Health Chatbot 💬", layout="centered")
st.title("🧠 Mental Health Chatbot ")
st.caption("Powered by Team Axion💻")

# ----------- Session Setup -----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------- Input UI -----------
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("How are you feeling today?", key="input_box")
    submitted = st.form_submit_button("Send")

# ----------- When user sends message -----------
if submitted and user_input:
    with st.spinner("Thinking..."):
        with model.chat_session():
            response = model.generate(user_input, max_tokens=250)

    # Save messages
    st.session_state.chat_history.append(("🧍 You", user_input))
    st.session_state.chat_history.append(("🤖 Bot", response))

# ----------- Display Chat History -----------
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
