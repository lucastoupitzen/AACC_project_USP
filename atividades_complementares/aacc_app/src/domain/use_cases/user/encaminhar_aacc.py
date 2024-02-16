from abc import ABC, abstractmethod

class EncaminharAaccInterface(ABC):

    @abstractmethod
    def encaminhar_aacc(self, aacc: str, avaliador: str) -> None: pass
