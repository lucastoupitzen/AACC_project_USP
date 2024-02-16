from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user.avaliar_aacc import AvaliarAaccInterface


class AvaliarAaccController(ControllerInterface):

    def __init__(self, use_case: AvaliarAaccInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        aacc : str = http_request.query_params["id_aacc"]
        comentarios : str = http_request.query_params["comentarios"]
        status : int = http_request.query_params["status"]

        response = self.__use_case.avaliar_aacc(
            aacc= aacc,
            comentarios= comentarios,
            status= status
        )

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    