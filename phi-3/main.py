import streamlit as st
import langchain_helper 
st.title("PHI-3 BOT",)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
        st.markdown("How can I Help you")

prompt=st.chat_input("Say Something")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response=langchain_helper.generate_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
