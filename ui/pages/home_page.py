import streamlit as st

from ui import manager, menu


def display_item_card(item):
    item_card_container = st.container(border=True)
    with item_card_container:
        st.header(item["title"])
        photo = st.container()
        image_url = manager.get_image(item["s3_url"])
        photo.image(image_url)
        info_container = st.container(border=True)
        user_info = manager.get_user_info_by_id(item["owner_id"])
        with info_container:
            if len(item["description"]) != 0:
                st.write(item["description"])
                price_and_user_container = st.container(border=True)
                with price_and_user_container:
                    st.write(f"price: {item['price']}")
                    col1, col2 = st.columns(2)
                    col1.write(f"owner: {user_info['name']}")
                    col2.write(f"contacts: {user_info['email']}")
            else:
                st.write(f"price: {item['price']} rub/day")
                col1, col2 = st.columns(2)
                col1.write(f"owner: {user_info['name']}")
                col2.write(f"contacts: {user_info['email']}")


def display_cards():
    container = st.container()
    with container:
        st.header("Available Gadgets")
        items = manager.get_items()
        if items is not None:
            for card in items:
                ct = st.container()
                with ct:
                    display_item_card(card)
        else:
            st.write("There are no devices available for rental")


def display():
    display_cards()
    menu.display()


display()
