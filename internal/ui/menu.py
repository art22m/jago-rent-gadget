import streamlit as st
import utils


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("pages/home_page.py", label="Available Gadgets 🖥")
    st.sidebar.page_link("pages/user_page.py", label="User Info 👤")
    st.sidebar.page_link("app.py", label="About 📱")


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("pages/home_page.py", label="Available Gadgets 🖥")
    st.sidebar.page_link("pages/auth_page.py", label="Log in 👤")
    st.sidebar.page_link("app.py", label="About 📱")


def display():
    if utils.is_authenticated():
        authenticated_menu()
    else:
        unauthenticated_menu()
