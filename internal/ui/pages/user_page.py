import streamlit as st

from internal.ui import auth, menu


def display_user_info():
    st.header("User information:")
    st.write(st.session_state.user_info)

    st.header("Sign out:")
    st.button(label="Sign Out", on_click=auth.sign_out, type="primary")


def display():
    if "user_info" in st.session_state:
        display_user_info()
    else:
        st.switch_page("pages/auth_page.py")
    menu.display()


display()
