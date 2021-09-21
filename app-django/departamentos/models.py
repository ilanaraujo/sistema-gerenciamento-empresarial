from django.db import models

# Classe de departamento
class Departamento(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255, blank=False)
    numero_projetos = models.IntegerField(default=0) # Quantidade de projetos no departamento
    numero_funcionarios = models.IntegerField(default=0) # Quantidade de funcionários do departamento

    # Construtor da classe
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome

    def adiciona_funcionario(self, id_funcionario):
        # ToDo acrescentar linha na tabela funcionario_departamento
        print(id_funcionario)
        self.numero_funcionarios += 1
        
    def remove_funcionario(self, id_funcionario):
        # ToDo acrescentar linha na tabela funcionario_departamento
        print(id_funcionario)
        self.numero_funcionarios -= 1
        

    def adiciona_projeto(self):
        self.numero_projetos += 1
    
    def remove_projeto(self):
        self.numero_projetos -= 1
