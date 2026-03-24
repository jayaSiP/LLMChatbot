import streamlit as st
from dotenv import load_dotenv
import os

# ---------------- LOAD ENV ----------------
load_dotenv()

# Ensure API key is available
if not os.getenv("MISTRAL_API_KEY"):
    st.error("❌ MISTRAL_API_KEY not found. Please set it in your .env file.")
    st.stop()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# ---------------- DEFAULT MODE (prevents error) ----------------
mode = "You are a helpful AI assistant."

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

st.markdown("<h1 style='text-align: center;'>🤖 Mood Based AI Chatbot</h1>", unsafe_allow_html=True)
st.caption("Choose AI personality and start chatting | Type 0 to stop")

# ---------------- MODE SELECTION ----------------
mode_choice = st.radio(
    "Choose your AI Mode:",
    ["😐 Normal", "😊 Happy", "😡 Angry", "😂 Funny", "😢 Sad"],
    horizontal=True
)

# ---------------- MODE MAPPING ----------------
if mode_choice == "😐 Normal":
    mode = "You are a helpful, neutral AI assistant. Respond clearly and professionally."
elif mode_choice == "😊 Happy":
    mode = "You are a cheerful and friendly AI assistant. Respond in a positive, warm and encouraging tone."
elif mode_choice == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_choice == "😂 Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# ---------------- UI THEME BASED ON MOOD ----------------
if "Happy" in mode_choice:
    bg_color = "#fff9c4"
elif "Angry" in mode_choice:
    bg_color = "#ffcdd2"
elif "Funny" in mode_choice:
    bg_color = "#e1bee7"
elif "Sad" in mode_choice:
    bg_color = "#bbdefb"
else:
    bg_color = "#f5f5f5"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    [data-testid="stChatMessage"] {{
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
        font-size: 16px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SESSION MEMORY ----------------
current_mode = mode

if "messages" not in st.session_state or st.session_state.get("current_mode") != current_mode:
    st.session_state.current_mode = current_mode
    st.session_state.messages = [SystemMessage(content=current_mode)]

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

    # Get AI response
    try:
        response = model.invoke(st.session_state.messages)
    except Exception as e:
        st.error(f"❌ API error: {e}")
        st.stop()

    # Modify response for happy mode
    if "Happy" in mode_choice:
        final_response = "😊 " + response.content
    else:
        final_response = response.content

    # Add AI message
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(final_response)

# ---------------- CLEAR BUTTON ----------------
st.divider()
if st.button("🔄 Reset Chat"):
    st.session_state.messages = [SystemMessage(content=current_mode)]
    st.rerun()

# ---------------- FOOTER ----------------
st.divider()

st.markdown(
    """
    <div style='text-align: center; font-size: 14px;'>
        👩‍💻 Built by <b>Jaya Singh</b><br>
        📧 Email: <a href="mailto:Jayaaworks@gmail.com">Jayaaworks@gmail.com</a><br>
        🔗 GitHub: <a href="https://github.com/jayaSiP" target="_blank">github.com/jayaSiP</a>
    </div>
    """,
    unsafe_allow_html=True
)