from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpRequest
from .formularios import DepartamentoForm
from .models import Departamento

# Lista todos os departamentos da empresa
def index(request):
    departamentos = Departamento.objects.order_by('id')
    context = {'titulo' : 'Departamentos', 'departamentos' : departamentos}
    return HttpResponse(render(request, 'index.html', context))

# Cria um novo departamento
def criar(request):
    context = {'titulo' : 'Novo Departamento'}
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            novo_departamento = Departamento(nome = request.POST['nome'])
            novo_departamento.save()
            return redirect('/departamento/')
        return HttpResponse("Erro ao salvar o dpto")
    else:
        form = DepartamentoForm()
        context = {'form' : form}
        return HttpResponse(render(request, 'criar.html', context))

# Fecha o departamento
def remover(request, id_departamento):
    Departamento.objects.get(id=id_departamento).delete()
    return redirect('/departamento/')

# Exibe detalhes sobre um departamento
def detalhes(request, id_departamento):
    context = { 'id_dpto' : id_departamento}
    return render(request, 'teste.html', context)

# Atualiza as informações do departamento
def atualizar(request, id_departamento):
    if request.method == 'POST':
        pass
    return HttpResponse("Atualizar informações do dpto")
