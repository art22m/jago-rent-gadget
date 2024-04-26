import streamlit as st
from firebase_admin import auth


def auth_user():
    email = st.text_input('Email')
    password = st.text_input('Пароль', type='password')

    if st.button('Войти'):
        try:
            user = auth.get_user_by_email(email)
            if True:
                st.write('Вы успешно вошли.')
            else:
                st.write('Неправильный пароль.')
        except:
            st.write('Пользователь не найден.')

auth_user()