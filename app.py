import streamlit as st
import uuid

from agents import agent

st.title("CSV AI Agent")

# -----------------------
# Session State
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())



# -----------------------
# Clear Chat Button
# -----------------------
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.thread_id = str(uuid.uuid4())
    st.rerun()

config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}
# -----------------------
# Display Chat History
# -----------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------
# User Input
# -----------------------
question = st.chat_input("Ask a question")

if question:

    # Save and display user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                response = agent.invoke(
                    {
                        "messages": [
                            ("user", question)
                        ]
                    },
                    config=config
                )

                answer = response["messages"][-1].content

                # Gemini sometimes returns a list of text blocks
                if isinstance(answer, list):
                    answer = "".join(
                        block["text"]
                        for block in answer
                        if isinstance(block, dict)
                        and block.get("type") == "text"
                    )

                st.write(answer)

        # Save assistant reply
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as e:

        error = str(e)

        if "RESOURCE_EXHAUSTED" in error or "429" in error:
            st.warning(
                "🚦 Rate limit reached.\n\n"
                "The free Gemini API quota has been exceeded.\n\n"
                "Please wait about 30–60 seconds and try again."
            )
        else:
            st.error("⚠️ An unexpected error occurred.")
            st.exception(e)