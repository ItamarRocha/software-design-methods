

class SuperUser:

    def __init__(self, login, password, employerID):
        self.__login = login
        self.__password = password
        self.__employerID = employerID

    

    def update_user(self, user_login, updates,user_manager):

        for update in updates:
            user_manager.update(user_login, update)

    def delete_user(self, user_login, user_manager):

        user_manager.remove(user_login)



    def getLogin(self):
        return self.__login
    
    def getPassword(self):
        return self.__password

    def getDataNascimento(self):
        return self.__employerID

    def setLogin(self,login):
        self.__login = login

    def setPassword(self, password):
        self.__password = password

    def setEmployerID(self,employerID ):
        self.__employerID = employerID

    
    
    

