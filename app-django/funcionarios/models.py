from django.db import models
from departamentos.models import Departamento

class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255, blank=False)
    cpf = models.IntegerField(blank=False)
    rg = models.IntegerField(blank=False)
    sexo = models.CharField(max_length=10)
    data_nascimento = models.DateField(blank=False)
    possui_hailitacao = models.BooleanField()
    valor_salario = models.FloatField(blank=False)
    carga_horaria_semanal = models.IntegerField(blank=False)
    id_departamento = models.ForeignKey(Departamento.id, blank=False) # Departamento ao qual o funcionário pertence

    # Construtor da classe
    def __init__(self, nome, cpf, rg, sexo, data_nascimento, possui_habilitacao, salario, carga_horaria_semanal):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.possui_habilitacao = possui_habilitacao
        self.salario = salario
        self.carga_horaria_semanal = carga_horaria_semanal

    def altera_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_habilitacao(self):
        self.possui_habilitacao = not(self.possui_habilitacao) 

    def alterar_salario(self, novo_salario):
        self.salario = novo_salario
    
    def alterar_carga_horaria(self, nova_carga_horaria):
        self.carga_horaria_semanal = nova_carga_horaria
