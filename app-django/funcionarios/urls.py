from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('cadastro/', views.cadastro),
    path('remover/<int:id_funcionario>', views.remover),
    path('atualizar/<int:id_funcionario>', views.atualizar_cadastro),
    path('detalhes/<int:id_funcionario>/', views.detalhes)
]