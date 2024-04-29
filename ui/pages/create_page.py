import streamlit as st

from ui import manager, menu


def display_add_form():
    with st.form(key="item_form"):
        col1, col2, col3 = st.columns([1, 2, 1])

        title = st.text_input(label="Title*")
        price = st.text_input(label="Price*")
        description = st.text_area(label="Description")
        picture = st.file_uploader(
            label="Upload the picture*",
            type=['png', 'jpg', 'jpeg', 'gif', 'heic'],
            accept_multiple_files=False,
        )

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Create")
        create_notification = col2.empty()
        if submit_button:
            if not title or not price or not picture:
                st.warning("Ensure all mandatory fields are filled.")
                st.stop()
            else:
                with create_notification, st.spinner(
                    "Creating advertisement..."
                ):
                    manager.create_item(title, price, description, picture)

                if "create_success" in st.session_state:
                    create_notification.success(
                        st.session_state.create_success
                    )
                    del st.session_state.create_success
                elif "create_warning" in st.session_state:
                    create_notification.warning(
                        st.session_state.create_warning
                    )
                    del st.session_state.create_warning


def display():
    menu.display()
    if "user_info" in st.session_state:
        display_add_form()
    else:
        st.warning("You should be logged in to create add.", icon="⚠️")
        go_to_log_in = st.button("Go to log in page ↗️")
        if go_to_log_in:
            st.switch_page("pages/auth_page.py")


display()
