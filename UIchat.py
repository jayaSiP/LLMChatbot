import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# Ensure API key is available
if not os.getenv("MISTRAL_API_KEY"):
    st.error("❌ MISTRAL_API_KEY not found. Please set it in your .env file.")
    st.stop()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# ---------------- MODEL ----------------
try:
    model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
except Exception as e:
    st.error(f"❌ Failed to initialize model: {e}")
    st.stop()

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mood Based AI Chatbot")
st.caption("Choose AI personality and start chatting | Type 0 to stop")

# ---------------- MODE SELECTION ----------------
mode_choice = st.radio(
    "Choose your AI Mode:",
    ["😐 Normal", "😊 Happy", "😡 Angry", "😂 Funny", "😢 Sad"],
    horizontal=True
)

# Map mode
if mode_choice == "😐 Normal":
    mode = "You are a helpful, neutral AI assistant. Respond clearly and professionally."
elif mode_choice == "😊 Happy":
    mode = "You are a cheerful and friendly AI assistant. Respond in a positive, encouraging, and warm tone."
elif mode_choice == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_choice == "😂 Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# ---------------- SESSION MEMORY ----------------
if "messages" not in st.session_state or st.session_state.get("current_mode") != mode:
    st.session_state.current_mode = mode
    st.session_state.messages = [SystemMessage(content=mode)]

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Say something...")

if user_input:

    if user_input == "0":
        st.warning("Conversation ended. Refresh page to start again.")
        st.stop()

    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response safely
    try:
        response = model.invoke(st.session_state.messages)
    except Exception as e:
        st.error(f"❌ API error: {e}")
        st.stop()

    # Add AI message
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)

# ---------------- CLEAR BUTTON ----------------
st.divider()
if st.button("🔄 Reset Chat"):
    st.session_state.messages = [SystemMessage(content=mode)]
    st.rerun()