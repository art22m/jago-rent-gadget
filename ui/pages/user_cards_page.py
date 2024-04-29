import streamlit as st
import time
from ui import manager, menu


def create_item_card(item):
    item_card_container = st.container(border=True)
    with item_card_container:
        st.header(item["title"])
        photo = st.container()
        image_url = manager.get_image_full_url(item["s3_url"])
        photo.image(image_url)
        info_container = st.container(border=True)
        with info_container:
            if len(item["description"]) != 0:
                st.write(f"Description: {item['description']}")
            st.write(f"Price: {item['price']}")
            delete_button = st.button("Delete", key=item['id'])
            if delete_button:
                status = manager.delete_item(item['id'])
                if status:
                    st.success('Successfully deleted', icon="✅")
                    time.sleep(0.4)
                    st.rerun()
                else:
                    st.warning('Something went wrong(', icon="😞")


def display_cards(items):
    container = st.container()
    with container:
        if items is not None:
            for card in items:
                ct = st.container()
                with ct:
                    create_item_card(card)


def display_user_cards():
    user_id = st.session_state.user_info["id"]
    user_info = manager.get_user_info_by_id(user_id)
    if user_info is None or len(user_info["items"]) == 0:
        st.write("You don't have any gadgets available for rent yet")
        add_gadget = st.button("Add gadget")
        if add_gadget:
            st.switch_page("pages/create_page.py")
    else:
        display_cards(user_info["items"])


def display():
    st.header("Your Gadgets")
    menu.display()
    if "user_info" in st.session_state:
        display_user_cards()
    else:
        st.warning("You should be logged in to service.", icon="⚠️")
        go_to_log_in = st.button("Go to log in page ↗️")
        if go_to_log_in:
            st.switch_page("pages/auth_page.py")


display()
