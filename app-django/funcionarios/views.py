from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Funcionario
from .formularios import FuncionarioForm
from departamentos.models import Departamento

def index(request):
    funcionarios = Funcionario.objects.order_by('nome')
    context = {'titulo' : 'Funcionários', 'funcionarios' : funcionarios}
    return HttpResponse(render(request, 'funcionarios.index.html', context))

def cadastro(request):
    context = { 'titulo' : 'Cadastrar Funcionario'}
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            novo_funcionario = Funcionario(
                nome = request.POST['nome'],
                cpf = request.POST['cpf'],
                rg = request.POST['rg'],
                sexo = request.POST['sexo'],
                possui_habilitacao = request.POST['possui_habilitacao'],
                salario = request.POST['salario'],
                carga_horaria_semanal = request.POST['carga_horaria_semanal'],
                departamento = Departamento.objects.get(id = request.POST['departamento'])
            )
            novo_funcionario.save()
            return redirect('/funcionarios/')
        else:
            return HttpResponse('Erro ao cadastrar')
    else:
        form = FuncionarioForm()
        context['form'] = form
        return HttpResponse(render(request, 'cadastrar_funcionario.html', context))

def atualizar_cadastro(request):
    return HttpResponse("Atualizar cadastro do funcionário")

def remover(request):
    return HttpResponse("Remover funcionário")

def detalhes(request):
    return HttpResponse("Detalhes de um funcionário")