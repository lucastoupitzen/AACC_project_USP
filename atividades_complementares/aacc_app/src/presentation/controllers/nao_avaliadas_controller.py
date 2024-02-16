from typing import List
from src.domain.models.aacc import Aacc
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.aacc.list_pendentes import AaccListaPendentesInterface


class NaoAvaliadasController(ControllerInterface):

    def __init__(self, use_case: AaccListaPendentesInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        id_avaliador = http_request.query_params["id_avaliador"]

        response : List[Aacc] = self.__use_case.listar_nao_avaliadas(id_avaliador=id_avaliador)

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    