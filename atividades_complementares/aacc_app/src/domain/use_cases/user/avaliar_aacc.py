from abc import ABC, abstractmethod

class AvaliarAaccInterface(ABC):

    @abstractmethod
    def avaliar_aacc(self, aacc: str, comentarios: str, status: int) -> None: pass
