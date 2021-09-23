from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('criar/', views.criar),
    path('remover/<int:id_departamento>', views.remover),
    path('detalhes/<int:id_departamento>', views.detalhes),
    path('atualizar/<int:id_departamento>', views.atualizar),
]