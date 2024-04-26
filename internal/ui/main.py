import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from pages import auth_page, home_page, user_page

st.set_page_config(
    page_title="RentGadget",
)


#
# cred = credentials.Certificate('pondering-5ff7c-c033cfade319.json')
# firebase_admin.initialize_app(cred)


def check_authorization():
    return True
    # try:
    #     user = auth.get_user_by_email(st.session_state['email'])
    #     st.session_state['user_id'] = user.uid
    #     return True
    # except:
    #     return False


class MultiApp:

    @staticmethod
    def run():
        if 'user_id' not in st.session_state:
            st.session_state['user_id'] = None

        menu = st.sidebar.selectbox('Меню', ['Авторизация', 'Главная', 'Профиль'])

        if menu == 'Авторизация':
            if check_authorization():
                st.write('Вы уже авторизованы.')
            else:
                auth_page.auth_user()

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
