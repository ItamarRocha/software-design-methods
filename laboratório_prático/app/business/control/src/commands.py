from abc import ABC, abstractmethod
from business.model.user import User
from business.model.empreendimento import Empreendimento
from ..exceptions.SaveException import SaveException
from ..exceptions.LoadException import LoadException
import time

class Command(ABC):
    @abstractmethod
    def executar(self, user, empreendimento) -> None:
        pass

class AddEmpreendimento(Command):     #ConcreteCommand
    def __init__(self, user, empreendimento, dicts):
        super().__init__()
        self.__user = user
        self.__empreendimento = empreendimento
        self.__dict = dicts
    def executar(self):
        self.__user.setEmpreendimento(self.__empreendimento.getNome(),
                                      self.__empreendimento.getDescricao(),
                                      self.__empreendimento.getLocal(),
                                      self.__empreendimento.getCategoria(), 
                                      self.__empreendimento.getLink_ig(),
                                      self.__empreendimento.getLink_whats(),
                                      self.__empreendimento.getLink_fbk())
        
        self.__dict[self.__user.getLogin()] = self.__user.getEmpreendimento
        
        path = "data/empreendimentos"
        encoding = "utf-8"
        try:
            with open(path,"wb") as f:
                for login, empreendimento in self.__dict.items():
                    f.write(login.encode(encoding))
                    f.write("\t".encode(encoding))

                    f.write(empreendimento.getNome().encode(encoding))
                    f.write("\t".encode(encoding))

                    f.write(empreendimento.getDescricao().encode(encoding))
                    f.write("\t".encode(encoding))

                    f.write(empreendimento.getLocal().encode(encoding))
                    f.write("\t".encode(encoding))

                    f.write(empreendimento.getCategoria().encode(encoding))
                    f.write("\t".encode(encoding))

                    f.write(empreendimento.getLink_ig().encode(encoding))
                    f.write("\t".encode(encoding))

                    f.write(empreendimento.getLink_whats().encode(encoding))
                    f.write("\t".encode(encoding))

                    f.write(empreendimento.getLink_fbk().encode(encoding))
                    f.write("\n".encode(encoding))

        except:

            raise SaveException('Erro: Não conseguiu salvar a lista de empreendimentos')

class AttEmpreendimento(Command):     #ConcreteCommand
    def __init__(self, user, empreendimento, dicts):
        super().__init__()
        self.__user = User(user)
        self.__empreendimento = Empreendimento(empreendimento)
        self.__dict = dicts
    def executar(self):
        #deletar
        coma = AddEmpreendimento(self.__user, self.__empreendimento, self.__dict)
        coma.executar()
        

class SearchEmpreendimento(Command):     #ConcreteCommand
    def __init__(self, user, empreendimento):
        super().__init__()
        self.__user = user
        self.__empreendimento = empreendimento
    def executar(self):
        empree = {}
        path = "data/empreendimentos"
        encoding = "utf-8"
        try:
            with open(path, "rb") as f:
                for line in f:
                    empree_data = line.decode(encoding).split("\t")
                    empree[empree_data[0]] = Empreendimento(empree_data[1],empree_data[2],empree_data[3],empree_data[4],empree_data[5],empree_data[6], empree_data[7][:-1])     
        except:
            raise LoadException('Erro: Não conseguiu carregar a lista de empreendimentos')
        
        return empree

class Invoker:
    def __init__(self, comando):
        self.__comando = comando
    '''
    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command
    '''
    def execute(self):
        return self.__comando.executar()

class Client:
    def __init__(self, user, empreendimento):    
        self.__user = user
        self.__empreendimento = empreendimento
        self.__dict = Invoker(SearchEmpreendimento(self.__user, self.__empreendimento)).execute()

    def setDict(self, dicts):
        self.__dict = dicts

    def getDict(self):
        return self.__dict
        
    def pesquisarEmpreendimentos(self):
        invoker = Invoker(SearchEmpreendimento(self.__user, self.__empreendimento))   #invoker = Invoker(command)
        self.__dict = invoker.execute()
        return self.__dict

    def adicionarEmpreendimentos(self):
        invoker = Invoker(AddEmpreendimento(self.__user, self.__empreendimento, self.__dict)) #invoker = Invoker(command)
        invoker.execute()


    
