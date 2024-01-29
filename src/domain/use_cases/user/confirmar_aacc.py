from abc import ABC, abstractmethod
from src.domain.models.aacc import Aacc

class ConfirmarAaccInterface(ABC):

    @abstractmethod
    def confirmar_aacc(self, aacc: Aacc) -> None: pass
