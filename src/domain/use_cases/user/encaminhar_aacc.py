from abc import ABC, abstractmethod
from src.domain.models.aacc import Aacc
from src.domain.models.user import User

class EncaminharAaccInterface(ABC):

    @abstractmethod
    def encaminhar_aacc(self, aacc: Aacc, avaliador: User) -> None: pass
