from django.db import models
from datetime import date

# Import da função que calcula o prazo de conclusão do projeto
from .calculadora import calcula_prazo

class Projeto(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255, blank=False)
    departamento = models.ForeignKey('departamentos.Departamento', blank=False, on_delete=models.CASCADE)
    supervisor = models.ForeignKey('funcionarios.Funcionario', blank=False, on_delete=models.CASCADE)
    horas_supervisao = models.IntegerField() # Quantidade de horas semanais que o supervisor gasta no projeto
    horas_necessarias_para_conclusao = models.IntegerField()
    prazo_estimado = models.DateField(default = None)
    horas_trabalhadas_por_semana = models.IntegerField(default = 0) # Quantidade atual de horas semanais do projeto
    horas_realizadas = models.IntegerField() # Horas que já foram trabalhadas
    data_ultimo_calculo_prazo = models.DateField()

    def __init__(
            self, nome, id_departamento, id_supervisor, horas_supervisao,
            horas_necessarias, horas_trabalhadas_por_semana
            ):
        self.nome = nome
        self.id_departamento = id_departamento
        self.id_supervisor = id_supervisor
        self.horas_supervisao = horas_supervisao
        self.horas_necessarias = horas_necessarias
        self.prazo_estimado = calcula_prazo(date.today(), horas_necessarias, horas_trabalhadas_por_semana)
        self.horas_trabalhadas_por_semana = horas_trabalhadas_por_semana
        self.data_ultimo_calculo_prazo = date.today()
    
    def calcula_prazo_conclusao(self):
        # 
        if self.horas_trabalhadas_por_semana != 0:
           self.prazo_estimado = calcula_prazo(date.today, self.horas_necessarias, self.horas_trabalhadas_por_semana)
    
    def informa_prazo(self):

        # Caso o projeto não tenha funcionários trabalhando nele (projeto parado)
        if not self.prazo_estimado:
            return "Prazo indeterminado"
        
        # Projeto possui funcionários trabalhando nele
        else:
            return self.prazo_estimado
