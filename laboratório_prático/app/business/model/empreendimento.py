class Empreendimento:
    def __init__(self, 
                nome: str = "", 
                descricao: str = "", 
                local: str = "",
                categoria: str = "", 
                link_ig: str = "",
                link_whats:str = "",
                link_fbk: str = ""
                ):
        
        self.__nome = nome
        self.__descricao = descricao
        self.__local = local
        self.__categoria = categoria
        self.__link_ig = link_ig
        self.__link_whats = link_whats
        self.__link_fbk= link_fbk
    
    def getNome(self):
        return self.__nome
    def setNome(self,nome):
        self.__nome = nome
    
    def getDescricao(self):
        return self.__descricao
    def setDescricao(self,descricao):
        self.__descricao = descricao

    def getCategoria(self):
        return self.__categoria
    def setCategoria(self,categoria):
        self.__categoria = categoria

    def getLocal(self):
        return self.__local
    def setLocal(self,local):
        self.__local = local

    def getLink_ig(self):
        return self.__link_ig
    def setLink_ig(self,link_ig):
        self.__link_ig = link_ig

    def getLink_whats(self): 
        return self.__link_whats
    def setLink_whats(self,link_whats):
        self.__link_whats = link_whats

    def getLink_fbk(self):
        return self.__link_fbk
    def setLink_fbk(self,link_fbk):
        self.__link_fbk = link_fbk