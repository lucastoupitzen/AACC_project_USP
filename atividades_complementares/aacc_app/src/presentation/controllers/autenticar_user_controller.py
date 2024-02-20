from ....src.presentation.http_types.http_request import HttpRequest
from ....src.presentation.http_types.http_response import HttpResponse
from ....src.presentation.interfaces.controller_interface import ControllerInterface
from ....src.domain.use_cases.user.autenticar_user import AutenticarUserInterface

class AutenticarUserController(ControllerInterface):

    def __init__(self, use_case: AutenticarUserInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        username : str = http_request.query_params["username"]
        password : str = http_request.query_params["password"]

        response = self.__use_case.autenticar(
            username= username,
            password= password
        )

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    