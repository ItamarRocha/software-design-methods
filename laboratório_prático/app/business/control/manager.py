from ..model.user import User
import re

class Manager:
    def __init__(self):     #conferir
        self.Users = {}

    def add(self, login, password):     
        try:
            if(len(login) <= 0):
                raise Exception("Campo login não pode ser vazio")

            if(len(login) > 20):
                raise Exception("Campo login suporta no máximo 20 caracteres")

            if(re.search("\d", login)):
                raise Exception("Campo login não pode ter números")

            if(len(password) < 8):
                raise Exception("Campo de senha deve ter no mínimo 8 caracteres")

            if(len(password) > 12):
                raise Exception("Campo de senha deve ter no máximo 12 caracteres")
            
            count = 0
            for i in password:
                if(i.isdigit()): count += 1
            
            if(count < 2):
                raise Exception("Campo de senha deve conter no mínimo 2 números")
        

        except Exception as e: print(e)

        self.Users[login] = User(login, password)    #conferir