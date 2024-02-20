import os
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from .decorators import *
#use_cases
from .src.data.use_cases.aacc.list_pendentes import AaccListaPendentes
from .src.data.use_cases.user.encaminhar_aacc import EncaminharAacc
from .src.data.use_cases.user.avaliar_aacc import AvaliarAacc
from .src.data.use_cases.user.confirmar_aacc import ConfirmarAacc
from .src.data.use_cases.user.cadastrar_user import CadastrarUser
from .src.data.use_cases.user.autenticar_user import AutenticarUser
#repositórios
from .src.infra.db.repositories.aacc_avaliacao_repository import AaccParaAvaliacaoRepository
from .src.infra.db.repositories.aacc_repository import AaccRepository
from .src.infra.db.repositories.user_repository import UserRepository
#controllers
from .src.presentation.controllers.nao_encaminhadas_controller import NaoEncaminhadasController
from .src.presentation.controllers.nao_avaliadas_controller import NaoAvaliadasController
from .src.presentation.controllers.nao_confirmadas_controller import NaoConfirmadasController
from .src.presentation.controllers.encaminhar_aacc_controller import EncaminharAaccController
from .src.presentation.controllers.avaliar_aacc_controller import AvaliarAaccController
from .src.presentation.controllers.confirmar_aacc_controller import ConfirmarAaccController
from .src.presentation.controllers.cadastrar_user_controller import CadastrarUserController
from .src.presentation.controllers.autenticar_user_controller import AutenticarUserController
#adapters
from .src.presentation.adapters.request_adapter import request_adapter
#presenters
from .src.presentation.presenters.json_response import json_response

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/login")
@allowed_users(["coordenador"])
def home_page(request):
    return render(request, 'home.html')

@login_required(login_url="/login")
def avaliar_page(request):
    return render(request, "avaliacao.html")

@login_required(login_url="/login")
@allowed_users(["coordenador"])
def encaminhamentos_page(request):
    return render(request, 'encaminhamentos.html')

@login_required(login_url="/login")
@allowed_users(["coordenador"])
def confirmar_page(request):
    return render(request, "confirmar.html")

@unauthenticated_user 
def login(request):

    if request.method == 'GET': return render(request, "login.html")
    
    if request.method == 'POST':

        user_repository = UserRepository()
        use_case = AutenticarUser(user_repository= user_repository)
        controller = AutenticarUserController(use_case= use_case)
        http_response = request_adapter(request=request, controller= controller)

        response = http_response.body["data"]

        if response:
            login_django(request, response)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == "coordenador":
                    return redirect("home")
                
            return redirect("avaliar_page")
        
        return HttpResponse("Login inválido")
        
    
    return HttpResponse("error: Invalid request method")

def logout(request):
    logout_django(request)
    return redirect('login')

@unauthenticated_user
def cadastro(request):

    if request.method == 'GET': return render(request, "cadastro.html")
    
    if request.method == 'POST':

        user_repository = UserRepository()
        use_case = CadastrarUser(user_repository= user_repository)
        controller = CadastrarUserController(use_case= use_case)
        request_adapter(request=request, controller= controller)


        return HttpResponse("Usuário cadastrado com sucesso!")
    
    return HttpResponse("error: Invalid request method")

@login_required(login_url="/login")
@allowed_users(["coordenador"])
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
@allowed_users(["coordenador"])
def confirmar(request):

    if request.method == 'POST':

        aacc_repository = AaccRepository()

        use_case = ConfirmarAacc(aacc_repository= aacc_repository)
        controller = ConfirmarAaccController(use_case = use_case)

        http_response = request_adapter(request=request, controller= controller)

        response = http_response.body["data"]

        return HttpResponse(response)
    
    return HttpResponse("error: Invalid request method")

@allowed_users(["coordenador"])
def nao_encaminhadas(request):

    if request.method == 'GET':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = AaccListaPendentes(aacc_repository= aacc_repository,
                                    aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = NaoEncaminhadasController(use_case = use_case)

        http_response = request_adapter(request=request, controller= controller)

        response = json_response(http_response.body["data"])

        return JsonResponse(json.dumps(response, cls=DjangoJSONEncoder), safe=False)

    
    return HttpResponse("error: Invalid request method")

@login_required(login_url="/login")
def nao_avaliadas(request):

    if request.method == 'GET':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = AaccListaPendentes(aacc_repository= aacc_repository,
                                    aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = NaoAvaliadasController(use_case= use_case)

        http_response = request_adapter(request= request, controller= controller)

        response = json_response(http_response.body["data"])

        return JsonResponse(json.dumps(response, cls=DjangoJSONEncoder), safe=False)

    return HttpResponse("error: Invalid request method")

@login_required(login_url="/login")
@allowed_users(["coordenador"])
def nao_confirmadas(request):

    if request.method == 'GET':

        aacc_repository = AaccRepository()
        aacc_avaliacao_repository = AaccParaAvaliacaoRepository()
        use_case = AaccListaPendentes(aacc_repository= aacc_repository,
                                    aacc_avaliacao_repository= aacc_avaliacao_repository)
        controller = NaoConfirmadasController(use_case= use_case)

        http_response = request_adapter(request= request, controller= controller)

        response = json_response(http_response.body["data"])

        return JsonResponse(json.dumps(response, cls=DjangoJSONEncoder), safe=False)

    return HttpResponse("error: Invalid request method")

#utilitarios
@login_required(login_url="/login")
def visualizar_documento(request, nome_arquivo):
    caminho_documento = os.path.join(
        '/home/lucas/Desktop/projetos/IC/AACC/Atividades_complementares/'
        'atividades_complementares', 
        'documentos', nome_arquivo)
    with open(caminho_documento, 'rb') as documento:
        response = HttpResponse(documento.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={nome_arquivo}'
        return response
    