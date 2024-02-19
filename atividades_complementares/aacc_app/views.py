from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .src.data.use_cases.aacc.list_pendentes import AaccListaPendentes
from .src.data.use_cases.user.encaminhar_aacc import EncaminharAacc
from .src.data.use_cases.user.avaliar_aacc import AvaliarAacc
from .src.data.use_cases.user.confirmar_aacc import ConfirmarAacc
from .src.infra.db.repositories.aacc_avaliacao_repository import AaccParaAvaliacaoRepository
from .src.infra.db.repositories.aacc_repository import AaccRepository
from .src.presentation.controllers.nao_encaminhadas_controller import NaoEncaminhadasController
from .src.presentation.controllers.nao_avaliadas_controller import NaoAvaliadasController
from .src.presentation.controllers.nao_confirmadas_controller import NaoConfirmadasController
from .src.presentation.controllers.encaminhar_aacc_controller import EncaminharAaccController
from .src.presentation.controllers.avaliar_aacc_controller import AvaliarAaccController
from .src.presentation.controllers.confirmar_aacc_controller import ConfirmarAaccController
from .src.presentation.adapters.request_adapter import request_adapter

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

@csrf_exempt
def encaminhar(request):

    if request.method == 'POST':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = EncaminharAacc(aacc_repository= aacc_repository,
                                aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = EncaminharAaccController(use_case = use_case)

        http_response = request_adapter(request=request, controller= controller)

        response = http_response.body["data"]

        return HttpResponse(response)
    
    return HttpResponse("error: Invalid request method")

@csrf_exempt
def avaliar(request):

    if request.method == 'POST':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = AvaliarAacc(aacc_repository= aacc_repository,
                                aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = AvaliarAaccController(use_case = use_case)

        http_response = request_adapter(request=request, controller= controller)

        response = http_response.body["data"]

        return HttpResponse(response)
    
    return HttpResponse("error: Invalid request method")

@csrf_exempt
def confirmar(request):

    if request.method == 'POST':

        aacc_repository = AaccRepository()
        
        use_case = ConfirmarAacc(aacc_repository= aacc_repository)
        controller = ConfirmarAaccController(use_case = use_case)

        http_response = request_adapter(request=request, controller= controller)

        response = http_response.body["data"]

        return HttpResponse(response)
    
    return HttpResponse("error: Invalid request method")

def nao_encaminhadas(request):

    if request.method == 'GET':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = AaccListaPendentes(aacc_repository= aacc_repository,
                                    aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = NaoEncaminhadasController(use_case = use_case)

        http_response = request_adapter(request=request, controller= controller)

        response = http_response.body["data"]

        for dado in response:
            dado.doc = str(dado.doc)

        return HttpResponse(response)
    
    return HttpResponse("error: Invalid request method")

def nao_avaliadas(request):

    if request.method == 'GET':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = AaccListaPendentes(aacc_repository= aacc_repository,
                                    aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = NaoAvaliadasController(use_case= use_case)

        http_response = request_adapter(request= request, controller= controller)

        response = http_response.body["data"]

        for dado in response:
            dado.doc = str(dado.doc)

        return HttpResponse(response)

    return HttpResponse("error: Invalid request method")

def nao_confirmadas(request):

    if request.method == 'GET':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = AaccListaPendentes(aacc_repository= aacc_repository,
                                    aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = NaoConfirmadasController(use_case= use_case)

        http_response = request_adapter(request= request, controller= controller)

        response = http_response.body["data"]

        for dado in response:
            dado.doc = str(dado.doc)

        return HttpResponse(response)

    return HttpResponse("error: Invalid request method")
