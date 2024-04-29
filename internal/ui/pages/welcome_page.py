import streamlit as st

from internal.ui import manager


def display():
    st.set_page_config(page_title="RentGadget", page_icon=" 📱")

    # Welcome message
    st.title("Welcome to RentGadget!")
    st.write(
        "RentGadget is your one-stop platform for renting all kinds of"
        " gadgets, from smartphones to laptops and more."
    )
    st.write(
        "Browse through our collection of high-quality gadgets and rent them"
        " for your needs."
    )
    image = manager.get_image_full_url("cbb09b7f-b399-4e6d-9c1e-d486fd951e82")
    st.image(image)
