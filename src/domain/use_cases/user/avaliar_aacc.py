from abc import ABC, abstractmethod
from src.domain.models.aacc import Aacc

class AvaliarAaccInterface(ABC):

    @abstractmethod
    def avaliar_aacc(self, aacc: Aacc, comentarios: str, status: int) -> None: pass
