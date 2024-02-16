from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nao_encaminhadas", views.nao_encaminhadas, name="nao_encaminhadas")
]
