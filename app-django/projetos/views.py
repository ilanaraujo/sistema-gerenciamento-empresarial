from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def criar(request):
    return HttpResponse("Criar projeto")

def encerrar(request):
    return HttpResponse("Encerrar o projeto")

def detalhes(request):
    return HttpResponse("Detalhes do projeto")

def atualizar(request):
    return HttpResponse("Atualizar informações do projeto")