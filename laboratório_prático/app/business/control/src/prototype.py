from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clonar(self):
        pass