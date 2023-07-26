import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    message = st.chat_message("assistant")
    message.write(prompt)