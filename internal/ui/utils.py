import streamlit as st


def is_authenticated():
    return "user_info" in st.session_state
