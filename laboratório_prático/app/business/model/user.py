from ..model.data import Data
from ..model.empreendimento import Empreendimento

class User:

    def __init__(self, login, password, dataNascimento, empreendimento=Empreendimento()):
        self.__data = Data(dataNascimento)
        self.__login = login
        self.__password = password
        self.__dataNascimento = self.__data.getDMY()
        self.__empreendimento = empreendimento
        
    def getLogin(self):
        return self.__login
    
    def getPassword(self):
        return self.__password

    def getDataNascimento(self):
        return self.__dataNascimento

    def getEmpreendimento(self):
        return self.__empreendimento

    def setLogin(self,login):
        self.__login = login

    def setPassword(self, password):
        self.__password = password

    def setDataNascimento(self,dataNascimento ):
        self.__dataNascimento = dataNascimento

    def setEmpreendimento(self, nome, descricao, local, categoria, link_ig, link_whats, link_fbk):
        self.__empreendimento = Empreendimento(nome, descricao, local, categoria, link_ig, link_whats, link_fbk)
