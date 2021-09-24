from django.urls import path

from .views import *

urlpatterns = [
    path('criar', criar),
    path('encerrar', encerrar),
    path('detalhes', detalhes),
    path('atualizar', atualizar)
]