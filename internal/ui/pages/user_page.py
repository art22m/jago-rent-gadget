import streamlit as st
from internal.ui import auth, menu


def display_user_info():
    st.title("User Information")
    user_container = st.container(border=True)
    with user_container:
        st.write(f"Name: {st.session_state.user_info['name']}")
        st.write(f"Email: {st.session_state.user_info['email']}")
    st.header("Sign out:")
    st.button(label="Sign Out", on_click=auth.sign_out, type="primary")


def display():
    if "user_info" in st.session_state:
        display_user_info()
    else:
        st.switch_page("pages/auth_page.py")
    menu.display()


display()
