from typing import List
from src.domain.models.aacc import Aacc
from src.domain.use_cases.aacc.list_pendentes import AaccListaPendentesInterface
from src.data.interfaces.aacc_repository import AaccRepositoryInterface
from src.data.interfaces.aacc_avaliacao_repository import AaccParaAvaliacaoRepositoryInterface

class AaccListaPendentes(AaccListaPendentesInterface):

    def __init__(self, aacc_repository: AaccRepositoryInterface, 
                 aacc_avaliacao_repository: AaccParaAvaliacaoRepositoryInterface) -> None:

        self.__aacc_repository = aacc_repository
        self.__aacc_avaliacao_repository = aacc_avaliacao_repository

    def listar_nao_encaminhadas(self) -> List[Aacc]:
        
        nao_encaminhadas = self.__aacc_repository.select_aacc_by_status(status=0)

        if len(nao_encaminhadas) == 0: 
            raise Exception("Não foram encontradas atividades para serem encaminhadas!")
        
        return nao_encaminhadas 
    
    def listar_nao_avaliadas(self, id_avaliador: str) -> List[Aacc]:
        
        nao_avaliadas = self.__aacc_avaliacao_repository.select_pendentes_avaliador(id_avaliador)
        
        return nao_avaliadas

    def listar_nao_confirmadas(self) -> List[Aacc]:
        
        nao_confirmadas = self.__aacc_repository.select_aacc_by_status(status=2)
    
        return nao_confirmadas
    