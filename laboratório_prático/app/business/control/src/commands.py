from abc import ABC, abstractmethod
from business.model.user import User
from business.model.empreendimento import Empreendimento

class Command(ABC):
    @abstractmethod
    def executar(self) -> None:
        pass

class addEmpreendimento(Command):     #ConcreteCommand
    def __init__(self, user, empreendimento):
        super().__init__()
        self.__user = user
        self.__empreendimento = Empreendimento(empreendimento)
    def executar(self):
        self.__user.setEmpreendimento(self.__empreendimento.nome,
                                      self.__empreendimento.descricao,
                                      self.__empreendimento.local,
                                      self.__empreendimento.categoria, 
                                      self.__empreendimento.link_ig,
                                      self.__empreendimento.link_whats,
                                      self.__empreendimento.link_fbk)

class attEmpreendimento(Command):     #ConcreteCommand
    def __init__(self, empreendimento):
        super().__init__()
        self.__empreendimento = empreendimento
    def executar(self, nome, descricao, local, categoria, link_ig, link_whats, link_fbk):
        self.__user.setEmpreendimento(self, nome, descricao, local, categoria, link_ig, link_whats, link_fbk)
        

class searchEmpreendimento(Command):     #ConcreteCommand
    def __init__(self, users):
        super().__init__()
        self.__users = users
    def executar(self):
        lista = []
        for i in self.__users:
            lista.append(i.Empreendimento.nome)
        return lista
    
class Client:
    def __init__(self):
        pass
    
class Invoker:
    def __init__(self):
        pass
    
class Receiver:
    def __init__(self):
        pass
    