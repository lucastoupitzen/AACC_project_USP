from ....src.presentation.http_types.http_request import HttpRequest
from ....src.presentation.http_types.http_response import HttpResponse
from ....src.presentation.interfaces.controller_interface import ControllerInterface
from ....src.domain.use_cases.user.cadastrar_user import CadastrarUserInterface

class CadastrarUserController(ControllerInterface):

    def __init__(self, use_case: CadastrarUserInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        username : str = http_request.query_params["username"]
        email : str = http_request.query_params["email"]
        first_name : str = http_request.query_params["first_name"]
        last_name : str = http_request.query_params["last_name"]
        password : str = http_request.query_params["password"]

        response = self.__use_case.cadastrar(
            username= username,
            email= email,
            first_name= first_name,
            last_name= last_name,
            password= password
        )

        return HttpResponse (
            status_code= 200,
            body= {
                "data": response
            }
        )
    