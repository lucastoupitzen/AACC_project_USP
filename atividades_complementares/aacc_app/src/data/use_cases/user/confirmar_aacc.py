from .....src.data.interfaces.aacc_repository import AaccRepositoryInterface
from .....src.domain.use_cases.user.confirmar_aacc import ConfirmarAaccInterface

class ConfirmarAacc(ConfirmarAaccInterface):

    def __init__(self, aacc_repository: AaccRepositoryInterface) -> None:
        
        self.__aacc_repository = aacc_repository

    def confirmar_aacc(self, aacc: str) -> None:
        
        response = self.__aacc_repository.update_status_aacc(
            id_aacc=aacc, status=3)

        return response
    