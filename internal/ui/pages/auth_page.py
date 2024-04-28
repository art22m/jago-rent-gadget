import streamlit as st

from internal.ui import auth, menu


def display_auth_page():
    if "user_info" not in st.session_state:
        col1, col2, col3 = st.columns([1, 2, 1])

        # Authentication form layout
        do_you_have_an_account = col2.selectbox(
            label="Do you have an account?",
            options=("Yes", "No", "I forgot my password"),
        )
        auth_form = col2.form(key="Authentication form", clear_on_submit=False)
        email = auth_form.text_input(label="Email")
        username = (
            auth_form.text_input(label="Username")
            if do_you_have_an_account in {"No"}
            else auth_form.empty()
        )
        password = (
            auth_form.text_input(label="Password", type="password")
            if do_you_have_an_account in {"Yes", "No"}
            else auth_form.empty()
        )
        auth_notification = col2.empty()

        if do_you_have_an_account == "Yes" and auth_form.form_submit_button(
            label="Sign In", use_container_width=True, type="primary"
        ):
            with auth_notification, st.spinner("Signing in"):
                auth.sign_in(email, password)
        elif do_you_have_an_account == "No" and auth_form.form_submit_button(
            label="Create Account", use_container_width=True, type="primary"
        ):
            with auth_notification, st.spinner("Creating account"):
                auth.create_account(email, username, password)
        elif (
            do_you_have_an_account == "I forgot my password"
            and auth_form.form_submit_button(
                label="Send Password Reset Email",
                use_container_width=True,
                type="primary",
            )
        ):
            with auth_notification, st.spinner("Sending password reset link"):
                auth.reset_password(email)

        if "auth_success" in st.session_state:
            auth_notification.success(st.session_state.auth_success)
            del st.session_state.auth_success
        elif "auth_warning" in st.session_state:
            auth_notification.warning(st.session_state.auth_warning)
            del st.session_state.auth_warning
    else:
        st.header("User information:")
        st.write(st.session_state.user_info)

        st.header("Sign out:")
        st.button(label="Sign Out", on_click=auth.sign_out, type="primary")


def display():
    display_auth_page()
    menu.display()


display()
