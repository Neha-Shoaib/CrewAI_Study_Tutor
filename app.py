import os
import streamlit as st
from tutor_crew import run_study_tutor

st.set_page_config(page_title="AI Study Tutor", page_icon="🎓", layout="centered")

st.title("🎓 AI Study Tutor Agent")
st.caption("Powered by CrewAI & Groq")

# Sidebar: API Key Configuration
st.sidebar.header("Configuration")
groq_api_key = st.sidebar.text_input(
    "Groq API Key", 
    value=os.environ.get("GROQ_API_KEY", ""), 
    type="password",
    help="Get a key at console.groq.com"
)

if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# Initialize conversational memory in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! What topic or problem would you like to study today?"}
    ]

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input handling
if prompt := st.chat_input("Ask a question, formula, or concept..."):
    if not groq_api_key:
        st.warning("Please add your GROQ API key in the sidebar or environment variables.")
        st.stop()

    # Append user prompt to state & display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Format memory string for the agent
    history_lines = []
    for item in st.session_state.messages[-6:]:  # Keep recent context window
        history_lines.append(f"{item['role'].capitalize()}: {item['content']}")
    history_context = "\n".join(history_lines)

    # Generate response via CrewAI
    with st.chat_message("assistant"):
        with st.spinner("Tutor is thinking and preparing steps..."):
            try:
                response = run_study_tutor(
                    user_query=prompt,
                    history_context=history_context,
                    api_key=groq_api_key
                )
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {e}")
