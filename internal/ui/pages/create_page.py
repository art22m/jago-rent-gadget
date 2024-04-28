import streamlit as st
from internal.ui import manager, menu

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     description = Column(String)
#     s3_url = Column(String)
#     price = Column(Integer)
#     owner_id = Column(Integer, ForeignKey("users.id"))

def display_add_form():
    with st.form(key="item_form"):
        title = st.text_input(label="Title*")
        price = st.text_input(label="Price*")
        description = st.text_area(label="Description")
        picture = st.file_uploader(label="Upload the picture*")

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Create")
        if submit_button:
            if not title or not price or not picture:
                st.warning("Ensure all mandatory fields are filled.")
                st.stop()
            else:
                manager.create_item(title, price, description, picture)
                # st.success("Advertisement successfully created!")


def display():
    menu.display()
    if "user_info" not in st.session_state:  # TODO: inverse logic
        display_add_form()
    else:
        st.warning('You should be logged in to create add.', icon="⚠️")
        go_to_log_in = st.button("Go to log in page ↗️")
        if go_to_log_in:
            st.switch_page("pages/auth_page.py")


display()
