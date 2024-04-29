import streamlit as st

from internal.ui import manager, menu


def create_item_card(card):
    item_card_container = st.container(border=True)
    with item_card_container:
        header = st.container()
        header.header(card["title"])
        photo = st.container()
        image_url = manager.get_image_full_url(card["s3_url"])
        photo.image(image_url)
        info_container = st.container(border=True)
        with info_container:
            if len(card["description"]) != 0:
                st.write(f"Description: {card['description']}")
            st.write(f"Price: {card['price']}")
            delete_button = st.button("Delete")
            if delete_button:
                st.write("ok")


def display_cards(items):
    container = st.container()
    with container:
        if items is not None:
            for card in items:
                ct = st.container()
                with ct:
                    create_item_card(card)


def display_user_cards():
    user_id = st.session_state.user_info["id"],
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
        st.warning('You should be logged in to service.', icon="⚠️")
        go_to_log_in = st.button("Go to log in page ↗️")
        if go_to_log_in:
            st.switch_page("pages/auth_page.py")


display()
