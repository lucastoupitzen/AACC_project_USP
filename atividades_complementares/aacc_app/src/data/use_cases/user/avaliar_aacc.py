from .....src.domain.use_cases.user.avaliar_aacc import AvaliarAaccInterface
from .....src.data.interfaces.aacc_avaliacao_repository import AaccParaAvaliacaoRepositoryInterface
from .....src.data.interfaces.aacc_repository import AaccRepositoryInterface

class AvaliarAacc(AvaliarAaccInterface):

    def __init__(self, aacc_repository: AaccRepositoryInterface, 
                 aacc_avaliacao_repository: AaccParaAvaliacaoRepositoryInterface) -> None:

        self.__aacc_avaliacao_repository = aacc_avaliacao_repository
        self.__aacc_repository = aacc_repository

    def avaliar_aacc(self, aacc: str, comentarios: str, status: int) -> None:

        response = self.__aacc_avaliacao_repository.register_avaliacao(
            id_aacc=aacc, 
            comentarios=comentarios, 
            status=status
        )

        self.__aacc_repository.update_status_aacc(id_aacc= aacc, status= 2)
        
        return response
    