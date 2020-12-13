from business.model.empreendimento import Empreendimento
from ..model.user import User
from ..model.data import Data

class FabricaUser:
    def criaUser(self, login: str = "", password: str = "", dataNascimento: str = "", empreendimento=Empreendimento()):
        return User(login, password, dataNascimento, empreendimento) 