import streamlit as st
from menu import menu
from pages import welcome_page


def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


def start_app():
    # Initialize st.session_state.role to None
    if "role" not in st.session_state:
        st.session_state.role = None

    # Retrieve the role from Session State to initialize the widget
    st.session_state._role = st.session_state.role

    welcome_page.display()
    menu()


start_app()
