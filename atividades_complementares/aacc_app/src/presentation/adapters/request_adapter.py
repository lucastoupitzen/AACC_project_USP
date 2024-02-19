from django.http import request as DjangoRequest
from ....src.presentation.http_types.http_request import HttpRequest
from ....src.presentation.http_types.http_response import HttpResponse
from ....src.presentation.interfaces.controller_interface import ControllerInterface


def request_adapter(request: DjangoRequest, controller: ControllerInterface) -> HttpResponse:

    body = request.body

    if request.method == "GET": query_params = request.GET
    if request.method == "POST": query_params = request.POST

    http_request = HttpRequest(

        body= body,
        headers = request.headers,
        query_params= query_params,
        
    )

    http_response = controller.handle(http_request)
    return http_response
