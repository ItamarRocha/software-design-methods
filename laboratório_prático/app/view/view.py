import streamlit as st
from PIL import Image
from business.control.src.manager import Manager
from business.model.user import User
import time

class View:
    def __init__(self):
        self.manager = Manager(users=1)
        self.options = ["Landing", "Login", "Register"]


    def landing_page(self):

        st.markdown(r"""
                        ### Bem-vindx!
                        Bem-vindx à nossa aplicação para a disciplina métodos de projeto de software.

                        Nessa aplicação fizemos uma breve implementação do trabalho passado pelo professor Raoni, com o intuito de podermos integrar nosso projeto com uma interface. Você pode se Registrar clicando na aba ao lado. Obrigado pelo seu tempo!
                        """)

        st.subheader("Metodologia")
        # Texto com Metodologia utilizada no trabalho
        st.markdown("""
        Para o desenvolvimento deste trabalho, escolhemos a linguagem Python, devido à sua praticidade. Além disso, utilizamos a biblioteca Streamlit para realizar essa demonstração, a fim de documentar nosso trabalho de maneira clara e com uma linguagem bastante visual.
        """)

        st.subheader("Contato")
        st.markdown("""
        Sinta-se livre para nos contactar via email ou issues no github. Mais informações sobre contato estão no tópico autores.
        """)
        st.subheader("Autores")

        author_1, author_2, author_3, author_4, author_5, author_6 = st.beta_columns(6)

        jp = Image.open('assets/jp.png')
        jw = Image.open('assets/wallace.png')
        ita = Image.open('assets/itamar.png')
        caio = Image.open('assets/caio.jpeg')
        sarah = Image.open('assets/sarah.jpeg')
        claudio = Image.open('assets/claudio.png')


        with author_1:
            st.markdown('**[Itamar Filho](https://linkedin.com/in/itamarrocha)**')
            st.image(ita, use_column_width=True)
            st.markdown('Github: **[ItamarRocha](https://github.com/ItamarRocha)**')
        
        with author_2:
            st.markdown('**[João Pedro](https://www.linkedin.com/in/jpvt/)**')
            st.image(jp, use_column_width=True)
            st.markdown('Github: **[jpvt](https://github.com/jpvt)**')

        with author_3:
            st.markdown('**[João Wallace](https://www.linkedin.com/in/jo%C3%A3o-wallace-b821bb1b0/)**')
            st.image(jw, use_column_width=True)
            st.markdown('Github: **[joallace](https://github.com/joallace)**')
        
        with author_4:
            st.markdown('**[Caio Victor](https://www.linkedin.com/in/caio-victor-do-amaral-cunha-sarmento-9779a21b0/)**')
            st.image(caio, use_column_width=True)
            st.markdown('Github: **[caiovictors](https://github.com/caiovictors)**')
        
        with author_5:
            st.markdown('**Claudio Brito**')
            st.image(claudio, use_column_width=True)
            st.markdown('Github: **[claudiosouza\nbrito](https://github.com/claudiosouzabrito)**')

        with author_6:
            st.markdown('**[Sarah Toscano](https://www.linkedin.com/in/sarah-andrade-toscano-de-carvalho-910835187/)**')
            st.image(sarah, use_column_width=True)
            st.markdown('Github: **[SarahToscano](https://github.com/SarahToscano)**')

    def login_page(self):
        placeholder = st.empty()
        self.logged = False
        with placeholder.beta_container():
            st.subheader("Login Section")

            user = st.text_input("User Name")
            password = st.text_input("Password",type='password')
            
            if st.button("Login"):

                try:

                    if (self.manager.users[user].getPassword() == password) and (self.manager.users[user].getLogin() == user):
                        
                        self.user = user

                        st.success("Logado com sucesso")
                        st.balloons()
                        time.sleep(1)
                        
                        self.logged = True

                        placeholder.empty()

                    else:
                        st.warning("Senha ou usuários incorretos")

                except Exception as e:
                    st.warning(f"{e}: Usuário não existente")

        if self.logged:
            st.write(self.user)
            self.logged_page()
            st.write("opa")

    def register_page(self):

        st.subheader("Register")

        user = st.text_input("Digite seu nome de usuário")
        password = st.text_input("Digite sua senha", type="password")
        password2 = st.text_input("Confirme sua senha", type="password")
        
        if st.button("Me registre!"):
            if password != password2:
                st.warning("As duas senhas fornecidas não são idênticas")
            
            else:

                try:
                    error = self.manager.add(user, password)

                except Exception as e:
                    error = True
                    st.warning(e)

                    
                if error == False:
                    st.success("Você criou sua conta!")

    def logged_page(self):
        st.subheader("Você está logado!")

        st.write(f"Bem vinde {self.user}. Você deseja deletar sua conta?")

        if st.button("SIM, Quero deletar minha conta!!"):
            self.manager.remove(self.user)


    def main_menu(self):
        st.title("Trabalho 1 MPS")

        choice = st.sidebar.selectbox("Menu", self.options)

        if choice == "Landing":

            self.landing_page()

        elif choice == "Login":

            self.login_page()

        elif choice == "Register":
            
            self.register_page()