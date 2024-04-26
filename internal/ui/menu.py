import streamlit as st


def check_authorization():
    return 'user_info' in st.session_state


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("pages/home_page.py", label="Available Gadgets🖥")
    st.sidebar.page_link("pages/user_page.py", label="User Info👤")
    st.sidebar.page_link("app.py", label="About")


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("pages/auth_page.py", label="Log in")
    st.sidebar.page_link("pages/home_page.py", label="Available Gadgets")
    st.sidebar.page_link("app.py", label="About")


def menu():
    if not check_authorization():
        unauthenticated_menu()
        return
    authenticated_menu()
