from ..model.data import Data

class User:

    def __init__(self, login, password,dataNascimento):
        self.__data = Data(dataNascimento)
        self.__login = login
        self.__password = password
        self.__dataNascimento =self.__data.converteData(dataNascimento)
        
    
    def getLogin(self):
        return self.__login
    
    def getPassword(self):
        return self.__password

    def setLogin(self,login):
        self.__login = login

    def setPassword(self, password):
        self.__password = password
    
    

