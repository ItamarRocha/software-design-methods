from infra.src.fabrica_persistence import FabricaPersistence
from ..exceptions.LoginException import LoginException
from ..exceptions.PasswordException import PasswordException
from ..exceptions.DeleteException import DeleteException
from business.model.superuser import SuperUser


class SuperUserManager():

    def __init__(self, superusers = None):

        fabrica_persistence = FabricaPersistence()
        self.persistence = fabrica_persistence.criarPersistence("data/superusers")    

        if superusers == None:
            self.superusers = {}
        else:
            self.superusers = self.persistence.load()


    def create(self, login, password, employerID):
        error = True

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
        
        if not error:

            self.superusers[login] = SuperUser(login, password, employerID)
            self.persistence.save(self.superusers)

    def read(self, login):

        print(f'Login: {self.superusers[login].getLogin()}')
        print(f'Password: {self.superusers[login].getPassword()}')
        print(f'EmployerID: {self.superusers[login].getEmployerID()}')

    def update(self, login, update, new):

        try:
            if update == 'senha':

                if(len(new) < 8):
                    raise PasswordException("Campo de senha deve ter no mínimo 8 caracteres")

                if(len(new) > 12):
                    raise PasswordException("Campo de senha deve ter no máximo 12 caracteres")

                self.superusers[login].setPassword(new)

        except PasswordException as e:
            print(e)

    def delete(self, login):

        try:

            del self.superusers[login]

        except DeleteException as e:
            print(e)

        self.persistence.save(self.superusers)
