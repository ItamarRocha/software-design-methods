from ...model.user import User
from ..exceptions.LoginException import LoginException
from ..exceptions.PasswordException import PasswordException
from ..exceptions.DeleteException import DeleteException
from infra.src.user_persistence import UserPersistence
import re

class Manager:
    def __init__(self, users = None):

        if users == None:
            self.users = {}
        else:
            self.users = users

        self.persistence = UserPersistence("../data/users")

    def add(self, login, password):     
        try:

            if(self.users[login] != None):
                raise LoginException("Usuário Existente")
            
            if(len(login) <= 0):
                raise LoginException("Campo login não pode ser vazio")

            if(len(login) > 20):
                raise LoginException("Campo login suporta no máximo 20 caracteres")

            if(re.search("\d", login)):
                raise LoginException("Campo login não pode ter números")

            if(len(password) < 8):
                raise PasswordException("Campo de senha deve ter no mínimo 8 caracteres")

            if(len(password) > 12):
                raise PasswordException("Campo de senha deve ter no máximo 12 caracteres")
            
            count = 0
            for i in password:
                if(i.isdigit()): count += 1
            
            if(count < 2):
                raise PasswordException("Campo de senha deve conter no mínimo 2 números")
        

        except Exception as e: 
            print(e)

        self.users[login] = User(login, password)
        self.persistence.save(self.users)


    def remove(self, login):

        try:

            del self.users[login]

        except DeleteException as e:
            print(e)

        self.persistence.save(self.users)            