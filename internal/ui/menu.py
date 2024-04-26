import streamlit as st


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
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
