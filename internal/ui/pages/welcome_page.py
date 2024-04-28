import streamlit as st


def display():
    st.set_page_config(page_title="RentGadget", page_icon=" 📱")

    # Welcome message
    st.title("Welcome to RentGadget!")
    st.write(
        "RentGadget is your one-stop platform for renting all kinds of gadgets, from smartphones to laptops and more."
    )
    st.write("Browse through our collection of high-quality gadgets and rent them for your needs.")
