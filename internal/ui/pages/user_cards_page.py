import streamlit as st
from internal.ui import menu, manager


def display_user_cards():
    email = st.session_state["user_info"]["email"]
    user_info = manager.get_user_id_by_email(email)
    st.write(user_info)


def display():
    menu.display()
    if "user_info" in st.session_state:
        display_user_cards()
    else:
        st.warning('You should be logged in to service.', icon="⚠️")
        go_to_log_in = st.button("Go to log in page ↗️")
        if go_to_log_in:
            st.switch_page("pages/auth_page.py")


display()
