from src.domain.use_cases.user.encaminhar_aacc import EncaminharAaccInterface
from src.data.interfaces.aacc_avaliacao_repository import AaccParaAvaliacaoRepositoryInterface
from src.data.interfaces.aacc_repository import AaccRepositoryInterface

class EncaminharAacc(EncaminharAaccInterface):

    def __init__(self, aacc_repository: AaccRepositoryInterface,
                  aacc_avaliacao_repository: AaccParaAvaliacaoRepositoryInterface) -> None:
        
        self.__aacc_avaliacao_repository = aacc_avaliacao_repository
        self.__aacc_repository = aacc_repository

    def encaminhar_aacc(self, aacc: str, avaliador: str) -> None:
        
        response = self.__aacc_avaliacao_repository.register_aacc_para_avaliacao(
            id_aacc= aacc,
            id_avaliador= avaliador
        )

        self.__aacc_repository.update_status_aacc(id_aacc= aacc, status= 1)

        return response
