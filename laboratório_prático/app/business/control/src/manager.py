from typing import AbstractSet
from business.model.fabrica_user import FabricaUser
from business.model.empreendimento import Empreendimento
from ..exceptions.BirthException import BirthException
from ..exceptions.LoginException import LoginException
from ..exceptions.PasswordException import PasswordException
from ..exceptions.DeleteException import DeleteException
from infra.src.fabrica_persistence import FabricaPersistence
import re
import datetime
from abc import ABC, abstractmethod

class UserManager:
    def __init__(self, users = None):
        fabrica_persistence = FabricaPersistence()                      #fabrica user_persistence
        self.persistence = fabrica_persistence.criarPersistence("data/users")    

        if users == None:
            self.users = {}
        else:
            self.users = self.persistence.load()

    def add(self, login, password, dataNascimento): #Adiciona usuário
        error =  False

        if(re.search("\d", login)):
            error = True
            raise LoginException("Campo login não pode ter números")
       
    
        if(login in self.users):
            error = True
            raise LoginException("Usuário Existente")

        if(len(login) <= 0):
            error = True
            raise LoginException("Campo login não pode ser vazio")


        if(len(login) > 20):
            error = True
            raise LoginException("Campo login suporta no máximo 20 caracteres")

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

        try:
            datetime.datetime.strptime(dataNascimento, "%d/%m/%Y")
        except:
            error = True
            raise BirthException("Formato de data incorreto. Por favor, insira dd/mm/aaaa")

        if error == False:
            fabrica_user = FabricaUser()                        #fabrica User
            self.users[login] = fabrica_user.criaUser(login, password, dataNascimento)      
            self.persistence.save(self.users)
        
        return error

    def update(self,login, update, new):   #atualizar

        try:

            if update == 'senha':

                if(len(new) < 8):
                    raise PasswordException("Campo de senha deve ter no mínimo 8 caracteres")

                if(len(new) > 12):
                    raise PasswordException("Campo de senha deve ter no máximo 12 caracteres")

                self.users[login].setPassword(new)

            elif update == 'dataNascimento':

                self.users[login].setDataNascimento(new)

                
        except Exception as e:

            print(e)


    def remove(self, login):  #remover

        try:

            del self.users[login]

        except DeleteException as e:
            print(e)

        self.persistence.save(self.users)        

    @abstractmethod
    def list_by_alphabet(self):
        pass
    

    @abstractmethod
    def list_by_birth(self):
        pass


