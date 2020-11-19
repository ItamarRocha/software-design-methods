class User:

    def __init__(self, login, password):

        self.__login = login
        self.__password = password

    
    def getLogin(self):

        return self.__login
    
    def getPassword(self):

        return self.__login

    def setLogin(self,login):

        self.__login = login;

    def setPassword(self, password):

        self.__password = password

