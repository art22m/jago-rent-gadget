import streamlit as st

from internal.ui import menu

sample_of_message = [
    {
        "title": "Пылесос 3000Т",
        "description": "пылесос очень крутой",
        "photo": "https://www.shutterstock.com/shutterstock/photos/2151833739/display_1500/stock-photo-portrait-of-a-young-latin-woman-with-pleasant-smile-and-crossed-arms-isolated-on-grey-wall-with-2151833739.jpg",
        "contacts": "some@email.ru",
        "money": "1000руб/ч",
    },
]


def create_item_card(card):
    item_card_container = st.container(border=True)
    with item_card_container:
        header = st.container()
        header.write(card["title"])
        photo = st.container()
        photo.image(card["photo"])
        info_container = st.container(border=True)
        with info_container:
            st.write(card["description"])
            st.write(card["money"])
            st.write(card["contacts"])

    return item_card_container


def display_cards():
    container = st.container()
    with container:
        for card in sample_of_message:
            ct = st.container()
            with ct:
                item_card = create_item_card(card)


def display():
    display_cards()
    menu.display()


display()
