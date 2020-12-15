import streamlit as st
import datetime
from business.control.src.manager import UserManager


class Proxy(UserManager):
    def __init__(self, logged, users):
        self.__logged = logged
        self.users = users

    def list_by_alphabet(self): #Ordena pelo alfabeto
        if self.__logged:
            list = []
            list= sorted(self.users.keys(), key=str.lower)
            if(len(list)):
                for i in list:
                    st.markdown(i)
            else:
                st.error("Nenhum membro encontrado")
        else:
            st.error("Logue para ver a lista de membros")

    def list_by_birth(self): #Lista pelo aniversário
        if self.__logged:
            datetime_objs = []
            logins = []
            for i in self.users.keys():
                my_datetime = datetime.datetime.strptime(self.users[i].getDataNascimento(), "%d/%m/%Y")
                datetime_objs.append(my_datetime)
                logins.append(i)
            datetime_objs.sort(reverse=True)

            lista=[]

            for i in datetime_objs:#ordenado 
                for j in logins:#array de cadastro
                    if(i==datetime.datetime.strptime(self.users[j].getDataNascimento(), "%d/%m/%Y")): #De acordo com as datas cria-se uma lista com logins
                        lista.append(j)
                        logins.remove(j)
            if(len(list)):
                for i in list:
                    st.markdown(i)
            else:
                st.error("Nenhum membro encontrado")
        else:
            st.error("Logue para ver a lista de membros")
