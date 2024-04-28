import streamlit as st

from internal.ui import auth, menu


def display_auth_page():
    col1, col2, col3 = st.columns([1, 2, 1])

    # Authentication form
    selector = col2.selectbox(
        label="Do you have an account?",
        options=("Yes", "No", "I forgot my password"),
    )
    auth_form = col2.form(key="Authentication form", clear_on_submit=False)

    # Inputs
    email = auth_form.text_input(label="Email")
    username = (
        auth_form.text_input(label="Username") if selector in {"No"} else auth_form.empty()
    )
    password = (
        auth_form.text_input(label="Password", type="password") if selector in {"Yes", "No"} else auth_form.empty()
    )

    # Buttons
    def create_account_button():
        return auth_form.form_submit_button(
            label="Create Account", use_container_width=True, type="primary"
        )

    def sign_in_button():
        return auth_form.form_submit_button(
            label="Sign In", use_container_width=True, type="primary"
        )

    def reset_button():
        return auth_form.form_submit_button(
            label="Reset Password", use_container_width=True, type="primary",
        )

    auth_notification = col2.empty()
    if selector == "Yes" and sign_in_button():
        with auth_notification, st.spinner("Signing in"):
            auth.sign_in(email, password)
    elif selector == "No" and create_account_button():
        with auth_notification, st.spinner("Creating account"):
            auth.create_account(email, username, password)
    elif selector == "I forgot my password" and reset_button():
        with auth_notification, st.spinner("Sending password reset link"):
            auth.reset_password(email)

    if "auth_success" in st.session_state:
        auth_notification.success(st.session_state.auth_success)
        del st.session_state.auth_success
    elif "auth_warning" in st.session_state:
        auth_notification.warning(st.session_state.auth_warning)
        del st.session_state.auth_warning


def display():
    if "user_info" not in st.session_state:
        display_auth_page()
    else:
        st.switch_page("pages/user_page.py")
    menu.display()


display()
