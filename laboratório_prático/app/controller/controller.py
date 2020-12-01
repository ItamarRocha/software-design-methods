import streamlit as st
from view.view import View

class Controller():

    def main_menu(self):
        st.title("Trabalho 1 MPS")

        front_end_app = View()

        choice = st.sidebar.selectbox("Menu", front_end_app.options, index=0)

        if choice == "Landing":
            
            front_end_app.landing_page()

        elif choice == "Login":
            
            if front_end_app.login_page():
                st.write("Você logou com sucesso!\nVá para a barra lateral para acessar outras configurações!")

        elif choice == "Register":
            
            front_end_app.register_page()

        elif choice == "Lista de membros":

                front_end_app.member_list_page()

        elif choice == "User page":

            if front_end_app.user_page():
                st.write("Você saiu do nosso sistema!\nVá para a barra lateral para acessar outras configurações!")
