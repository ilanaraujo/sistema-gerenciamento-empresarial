from django.db import models

class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255, blank=False)
    cpf = models.IntegerField(blank=False)
    rg = models.IntegerField(blank=False)
    sexo = models.CharField(max_length=10)
    data_nascimento = models.DateField(blank=False)
    possui_hailitacao = models.BooleanField()
    salario = models.FloatField(blank=False)
    carga_horaria_semanal = models.IntegerField(blank=False)
    departamento = models.ForeignKey('departamentos.Departamento', blank=False, null=True, on_delete=models.SET_NULL) # Departamento ao qual o funcionário pertence

    def altera_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_habilitacao(self):
        self.possui_habilitacao = not(self.possui_habilitacao) 

    def alterar_salario(self, novo_salario):
        self.salario = novo_salario
    
    def alterar_carga_horaria(self, nova_carga_horaria):
        self.carga_horaria_semanal = nova_carga_horaria
