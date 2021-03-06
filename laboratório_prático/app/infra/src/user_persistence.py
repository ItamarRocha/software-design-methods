from business.model.fabrica_user import FabricaUser
from ..exceptions.SaveException import SaveException
from ..exceptions.LoadException import LoadException

class UserPersistence:
    def __init__(self, path: str, encoding = "utf-8"):
        self.path = path
        self.encoding = encoding

    def save(self, users: dict):

        try:
            with open(self.path,"wb") as f:
                for login, user in users.items():
                    f.write(login.encode(self.encoding))
                    f.write("\t".encode(self.encoding))

                    f.write(user.getPassword().encode(self.encoding))
                    f.write("\t".encode(self.encoding))

                    f.write(user.getDataNascimento().encode(self.encoding))
                    f.write("\n".encode(self.encoding))

        except:

            raise SaveException('Erro: Não conseguiu salvar a lista de usuários')


    def load(self):
        users = {}

        try:
            with open(self.path, "rb") as f:
                for line in f:
                    user_data = line.decode(self.encoding).split("\t")
                    fabrica_user = FabricaUser()                        #fabrica User
                    users[user_data[0]] = fabrica_user.criaUser(user_data[0], user_data[1], user_data[2][:-1])     
        except:
            raise LoadException('Erro: Não conseguiu carregar a lista de usuários')
        
        return users