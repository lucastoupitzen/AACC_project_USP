from django.urls import path

from . import views

urlpatterns = [
    #pages
    path("", views.index, name="index"),
    path('home', views.home_page, name="home"),
    path("avaliar_page", views.avaliar_page, name="avaliar_page"),
    path("encaminhamentos", views.encaminhamentos_page, name="encaminhamentos_page"),
    path("confirmar_page", views.confirmar_page, name="confirmar_page"),
    #urls de requisição
    path("nao_encaminhadas", views.nao_encaminhadas, name="nao_encaminhadas"),
    path("nao_avaliadas", views.nao_avaliadas, name="nao_avaliadas"),
    path("nao_confirmadas", views.nao_confirmadas, name="nao_confirmadas"),
    path('encaminhar', views.encaminhar, name="encaminhar"),
    path('avaliar', views.avaliar, name="avaliar"),
    path('confirmar', views.confirmar, name="confirmar"),
    path('documentos/<str:nome_arquivo>', views.visualizar_documento, name='visualizar_documento'),
    #urls de login
    path('cadastro', views.cadastro, name="cadastro"),
    path("login", views.login, name='login'),
    path("logout", views.logout, name="logout"),
]
