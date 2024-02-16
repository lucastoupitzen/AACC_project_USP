from typing import List
from abc import ABC, abstractmethod
from ....src.domain.models.aacc import Aacc
from ....src.domain.models.aacc_para_avaliacao import AaccParaAvaliacao

class AaccParaAvaliacaoRepositoryInterface(ABC):

    @abstractmethod
    def select_pendentes_avaliador(self, id_avaliador: str) -> List[Aacc]: pass

    @abstractmethod
    def select_aacc_para_avaliacao(self, id_aacc: str) -> AaccParaAvaliacao: pass

    @abstractmethod
    def register_aacc_para_avaliacao(self, id_aacc: str, id_avaliador: str) -> None: pass

    @abstractmethod
    def register_avaliacao(self, id_aacc: str, comentarios: str, status: int) -> None: pass
