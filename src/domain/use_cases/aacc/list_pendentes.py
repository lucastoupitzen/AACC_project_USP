from abc import ABC, abstractmethod
from typing import List
from src.domain.models.aacc import Aacc

class AaccListaPendentesInterface(ABC):

    @abstractmethod
    def listar_nao_encaminhadas(self) -> List[Aacc]: pass

    @abstractmethod
    def listar_nao_avaliadas(self) -> List[Aacc]: pass

    @abstractmethod
    def listar_nao_confirmadas(self) -> List[Aacc]: pass
