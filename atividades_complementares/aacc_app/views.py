from django.http import HttpResponse
from .src.data.use_cases.aacc.list_pendentes import AaccListaPendentes
from .src.infra.db.repositories.aacc_avaliacao_repository import AaccParaAvaliacaoRepository
from .src.infra.db.repositories.aacc_repository import AaccRepository
from .src.presentation.controllers.nao_encaminhadas_controller import NaoEncaminhadasController
from .src.presentation.adapters.request_adapter import request_adapter

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def nao_encaminhadas(request):

    print(request)
    
    aacc_repository = AaccRepository()
    aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
    use_case = AaccListaPendentes(aacc_repository= aacc_repository,
                                  aacc_avaliacao_repository= aacc_avaliacao_repository)
    controller = NaoEncaminhadasController(use_case= use_case)

    http_response = request_adapter(request= request, controller= controller)

    return HttpResponse({http_response})
