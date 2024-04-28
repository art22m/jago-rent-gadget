import streamlit as st

import menu
from pages import welcome_page


def start_app():
    print(st.session_state)
    welcome_page.display()
    menu.display()


start_app()
