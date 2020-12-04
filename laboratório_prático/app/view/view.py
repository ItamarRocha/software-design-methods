import streamlit as st
from PIL import Image
from business.control.src.manager import UserManager
from business.control.src.commands import Client
from business.model.user import User
from business.model.fabrica_user import FabricaUser
from business.model.empreendimento import Empreendimento
import time

@st.cache(allow_output_mutation=True)
class View:
    def __init__(self):
        self.manager = UserManager(users=1)
        self.logged = False
        self.options = ["Landing", "Login", "Register", "User page", "Lista de membros"]
        self.client = Client(FabricaUser().criaUser(), Empreendimento()) # Client(user, empreendimento)

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
        
        st.subheader("Login Section")

        placeholder = st.empty()

        if not self.logged:
            with placeholder.beta_container():
                
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

                            self.client = Client(self.manager.users[user], self.manager.users[user].empreendimento)

                            placeholder.empty()

                            return True

                        else:
                            st.warning("Senha ou usuários incorretos")
                            return False

                    except Exception as e:
                        st.warning(f"{e}: Usuário não existente")
                        return False
        else:
            st.write("Você já está logado!")

    def register_page(self):

        st.subheader("Register")

        if not self.logged:
            user = st.text_input("Digite seu nome de usuário")
            dataNascimento = st.text_input("Data do nascimento")
            password = st.text_input("Digite sua senha", type="password")
            password2 = st.text_input("Confirme sua senha", type="password")
            
            if st.button("Me registre!"):
                if password != password2:
                    st.warning("As duas senhas fornecidas não são idênticas")
                
                else:

                    try:
                        error = self.manager.add(user, password,dataNascimento)

                    except Exception as e:
                        error = True
                        st.warning(e)

                        
                    if error == False:
                        st.success("Você criou sua conta!")
        else:
            st.write("Você já está logado!")

    def user_page(self):

        st.subheader("Área do usuário")

        placeholder = st.empty()

        if self.logged:
            with placeholder.beta_container():
            
                st.write(f"Bem vindo(a) {self.user}. Suas opções estão abaixo!")

                st.write(f"Deseja cadastrar um empreendimento seu?")

                #if st.button("cadastrar empreendimento"):

                nome = st.text_input("Digite o nome do negócio")
                descricao = st.text_input("Descreva seu negócio")
                local = st.text_input("Local")
                categoria = st.text_input("Categoria")
                link_ig = st.text_input("Link para contato via instagram")
                link_whats = st.text_input("Link para contato via whatsapp")
                link_fbk = st.text_input("Link para contato via facebook")

                if st.button("Cadastrar"):

                    empreendimento = Empreendimento(nome, descricao, local, categoria, link_ig, link_whats, link_fbk)
                    self.client = Client(self.manager.users[self.user], empreendimento)
                    self.client.getDict()[self.user] = empreendimento

                    try:
                        error = self.client.adicionarEmpreendimentos()

                    except Exception as e:
                        error = True
                        st.warning(e)

                        
                    if error == False:
                        st.success("Você criou seu empreendimento!")

                if st.button("Quero deslogar"):
                    
                    st.warning("Você deslogou!")
                    time.sleep(1)
                    self.user = None
                    self.logged = False
                    
                    placeholder.empty()


                    return True

                if st.button("Quero deletar minha conta!!"):

                    st.warning("Você deletou sua conta :(")
                    time.sleep(1)
                    placeholder.empty()
                    self.manager.remove(self.user)
                    self.user = None
                    self.logged = False
                    
                    return True

        else:
            st.error("Você não está logado")
            return False

        return False

    def member_list_page(self):
        st.subheader("Lista de membros e empreendimentos")

        if st.button("Ver lista de empreendimentos", 1):
            lista = self.client.pesquisarEmpreendimentos()
            if(len(lista)):
                for i in lista:
                    string = lista[i].getNome() + "\t" + lista[i].getDescricao() + "\t" + lista[i].getLocal() + "\t" + lista[i].getCategoria() + "\t" + lista[i].getDescricao() + "\t" + lista[i].getLink_ig() + "\t" + lista[i].getLink_whats() + "\t" + lista[i].getLink_fbk()
                    st.markdown(string)
            else:
                st.error("Nenhum empreendimento encontrado")

        
        if self.logged:
        
            if st.button("Por ordem alfabética", 2):
        
                list = self.manager.list_by_alphabet()
                if(len(list)):
                    for i in list:
                        st.markdown(i)
                else:
                    st.error("Nenhum membro encontrado")
        
            if st.button("Data de nascimento", 3):
                list = self.manager.list_by_birth()
                if(len(list)):
                    for i in list:
                        st.markdown(i)
                else:
                    st.error("Nenhum membro encontrado")
        
        else:

            st.error("Logue para ver a lista de membros")