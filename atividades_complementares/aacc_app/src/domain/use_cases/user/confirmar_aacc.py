from abc import ABC, abstractmethod

class ConfirmarAaccInterface(ABC):

    @abstractmethod
    def confirmar_aacc(self, aacc: str) -> None: pass
