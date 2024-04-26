import streamlit as st
import math

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
            price, user_info = st.columns([4, 1])
            with price:
                st.write(card["money"])
            with user_info:
                st.write(card["contacts"])

    return item_card_container


container = st.container()

number_of_columns = 3

number_of_rows = math.ceil((len(sample_of_message) / number_of_columns))
for i in range(number_of_rows):
    ct = st.container()
    with ct:
        num_current_cl = 3  # min(number_of_columns, (i + 1) * number_of_columns - len(sample_of_message)) # TODO: check
        row_container = st.columns(num_current_cl)
        for j in range(num_current_cl):
            index = i * number_of_rows + j
            with row_container[j]:
                card = create_item_card(sample_of_message[index])


def get_cards():
    message = sample_of_message


# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")
#
# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")
#
# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")
#
