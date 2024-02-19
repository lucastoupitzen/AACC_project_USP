from ....src.presentation.http_types.http_request import HttpRequest
from ....src.presentation.http_types.http_response import HttpResponse
from ....src.presentation.interfaces.controller_interface import ControllerInterface
from ....src.domain.use_cases.user.encaminhar_aacc import EncaminharAaccInterface


class EncaminharAaccController(ControllerInterface):

    def __init__(self, use_case: EncaminharAaccInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        aacc : str = http_request.query_params["id_aacc"]
        avaliador : str = http_request.query_params["id_avaliador"]

        response = self.__use_case.encaminhar_aacc(
            aacc= aacc,
            avaliador= avaliador
        )

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    