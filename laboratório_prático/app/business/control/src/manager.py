from ...model.user import User
from ..exceptions.LoginException import LoginException
from ..exceptions.PasswordException import PasswordException
from ..exceptions.DeleteException import DeleteException
from infra.src.user_persistence import UserPersistence
import re

class Manager:
    def __init__(self, users = None):

        self.persistence = UserPersistence("data/users")

        if users == None:
            self.users = {}
        else:
            self.users = self.persistence.load()
            print(type(self.users))
            print(self.users)
            print(self.users['jp'].getPassword())

    def add(self, login, password):
        error =  False     

        if(self.users[login] != None):
            error = True
            raise LoginException("Usuário Existente")

        if(len(login) <= 0):
            error = True
            raise LoginException("Campo login não pode ser vazio")

        if(len(login) > 20):
            error = True
            raise LoginException("Campo login suporta no máximo 20 caracteres")

        if(re.search("\d", login)):
            error = True
            raise LoginException("Campo login não pode ter números")


        if(len(password) < 8):
            error = True
            raise PasswordException("Campo de senha deve ter no mínimo 8 caracteres")

        if(len(password) > 12):
            error = True
            raise PasswordException("Campo de senha deve ter no máximo 12 caracteres")
        
        count = 0
        for i in password:
            if(i.isdigit()): count += 1
        
        if(count < 2):
            error = True
            raise PasswordException("Campo de senha deve conter no mínimo 2 números")


        if error == False:
            self.users[login] = User(login, password)
            self.persistence.save(self.users)

        return error


    def remove(self, login):

        try:

            del self.users[login]

        except DeleteException as e:
            print(e)

        self.persistence.save(self.users)            