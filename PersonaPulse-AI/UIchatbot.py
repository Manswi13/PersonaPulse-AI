import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="Mood AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Custom CSS
# ---------------------------

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

h1 {
    text-align: center;
}

.mode-card {
    padding:10px;
    border-radius:10px;
    background-color:#1c1f26;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Model
# ---------------------------

model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9
)

# ---------------------------
# Sidebar
# ---------------------------

with st.sidebar:

    st.title("🎭 AI Modes")

    mode_choice = st.radio(
        "Choose your AI personality",
        (
            "😡 Angry Mode",
            "😂 Funny Mode",
            "😢 Sad Mode"
        )
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.clear()
        st.rerun()

# ---------------------------
# Mode Selection
# ---------------------------

if mode_choice == "😡 Angry Mode":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif mode_choice == "😂 Funny Mode":
    mode = "You are a very funny AI agent. You respond with humor and jokes."

else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# ---------------------------
# Initialize Messages
# ---------------------------

if (
    "messages" not in st.session_state
    or st.session_state.get("current_mode") != mode
):

    st.session_state.current_mode = mode

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# ---------------------------
# Header
# ---------------------------

st.title("🤖 Mood AI Chatbot")

st.caption(
    "Choose a personality from the sidebar and start chatting."
)

# ---------------------------
# Display Chat History
# ---------------------------

for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---------------------------
# User Input
# ---------------------------

prompt = st.chat_input("Type your message...")

if prompt:

    if prompt == "0":
        st.stop()

    # Show User Message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # AI Thinking
    with st.spinner("Thinking..."):

        response = model.invoke(
            st.session_state.messages
        )

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Show AI Response
    with st.chat_message("assistant"):
        st.write(response.content)

