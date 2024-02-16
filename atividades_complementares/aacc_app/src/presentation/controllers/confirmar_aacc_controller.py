from ....src.presentation.http_types.http_request import HttpRequest
from ....src.presentation.http_types.http_response import HttpResponse
from ....src.presentation.interfaces.controller_interface import ControllerInterface
from ....src.domain.use_cases.user.confirmar_aacc import ConfirmarAaccInterface


class ConfirmarAaccController(ControllerInterface):

    def __init__(self, use_case: ConfirmarAaccInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        aacc : str = http_request.query_params["id_aacc"]

        response = self.__use_case.confirmar_aacc(
            aacc= aacc,
        )

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    