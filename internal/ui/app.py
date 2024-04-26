import streamlit as st
from menu import menu
from pages import welcome_page


def start_app():
    print(st.session_state)
    welcome_page.display()
    menu()


start_app()
