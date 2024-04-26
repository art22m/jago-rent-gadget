import streamlit as st
from pages import auth_page, home_page, user_page


def check_authorization():
    return 'user_info' in st.session_state


class MultiApp:

    @staticmethod
    def run():
        menu = st.sidebar.selectbox('Меню', ['Авторизация', 'Главная', 'Профиль'])

        if menu == 'Авторизация':
            auth_page.display_auth_page()

        elif menu == 'Главная':
            if check_authorization():
                home_page.display_cards()
            else:
                st.write('Пожалуйста, авторизуйтесь.')

        elif menu == 'Профиль':
            if check_authorization():
                user_page.display_user_info(st.session_state['user_id'])
            else:
                st.write('Пожалуйста, авторизуйтесь.')


MultiApp.run()
