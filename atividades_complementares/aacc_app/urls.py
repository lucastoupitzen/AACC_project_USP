from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nao_encaminhadas", views.nao_encaminhadas, name="nao_encaminhadas"),
    path("nao_avaliadas", views.nao_avaliadas, name="nao_avaliadas"),
    path("nao_confirmadas", views.nao_confirmadas, name="nao_confirmadas"),
    path('encaminhar', views.encaminhar, name="encaminhar"),
    path('avaliar', views.avaliar, name="avaliar"),
    path('confirmar', views.confirmar, name="confirmar"),
]
