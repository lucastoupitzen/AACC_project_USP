from django.http import request as DjangoRequest
from ....src.presentation.http_types.http_request import HttpRequest
from ....src.presentation.http_types.http_response import HttpResponse
from ....src.presentation.interfaces.controller_interface import ControllerInterface


def request_adapter(request: DjangoRequest, controller: ControllerInterface) -> HttpResponse:

    http_request = HttpRequest(

        body= request.body,
        headers = request.headers,
        # query_params=request.args,
        # path_params=request.view_args,
        # url=request.full_path
    )

    http_response = controller.handle(http_request)
    return http_response
