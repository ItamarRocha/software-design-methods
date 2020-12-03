from abc import ABC, abstractmethod
from ..model.empreendimento import Empreendimento

class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self):
        pass

class EmpreendimentoMemento(Memento):
    def __init__(self, state: Empreendimento):
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state: Empreendimento):
        self._state = state
