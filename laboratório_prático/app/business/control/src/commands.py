from abc import ABC, abstractmethod
from business.model.user import User
from business.model.empreendimento import Empreendimento
import time

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
        self._commands = {}
        self._history = {}

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        self._history.append((time.time(), command_name))
        self._commands[command_name].executar()
    
class Receiver:
    def __init__(self):
        pass
    