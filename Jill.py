import streamlit as st

# Set page config

st.set_page_config(page_title=“Chat App”, page_icon=“💬”)

# Initialize chat history in session state

if “messages” not in st.session_state:
st.session_state.messages = []

# App title

st.title(“💬 Chat Application”)

# Display chat messages from history

for message in st.session_state.messages:
with st.chat_message(message[“role”]):
st.markdown(message[“content”])

# Chat input

if prompt := st.chat_input(“Type your message here…”):
# Add user message to chat history
st.session_state.messages.append({“role”: “user”, “content”: prompt})

```
# Display user message
with st.chat_message("user"):
    st.markdown(prompt)

# Generate assistant response (echo back for now)
response = f"You said: {prompt}"

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})

# Display assistant response
with st.chat_message("assistant"):
    st.markdown(response)
```

# Sidebar with additional options

with st.sidebar:
st.header(“Options”)
if st.button(“Clear Chat History”):
st.session_state.messages = []
st.rerun()

```
st.markdown("---")
st.markdown("### About")
st.info("This is a simple chat application built with Streamlit. Messages are stored in session state.")
```
