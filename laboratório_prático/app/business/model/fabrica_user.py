from ..model.user import User
from ..model.data import Data

class FabricaUser:
    def criaUser(self, login, password, dataNascimento):
        return User(login, password, dataNascimento) 