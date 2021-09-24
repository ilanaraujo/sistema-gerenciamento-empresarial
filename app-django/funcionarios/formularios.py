from django import forms
from django.db.models.fields import CommaSeparatedIntegerField
from .models import Funcionario

escolhas =[('1', 'Masculino'), ('2', 'Feminino'), ('3' 'Outro')]

class FuncionarioForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=255)
    cpf = forms.IntegerField(label='cpf')
    rg = forms.IntegerField(label='rg')
    sexo = forms.RadioSelect(label='sexo', choices=escolhas)
    data_nascimento = forms.DateField(label='data_nascimento')
    possui_habilitacao = forms.BooleanField(label='possui_habilitacao')
    salario = forms.FloatField(label='salario')
    carga_horaria_semanal = forms.IntegerField(label='carga_horaria_semanal') 
    departamento = forms.IntegerField(label='departamento')
    
    class Meta:
        model = Funcionario
        fields = ['nome']
        exclude = ['id']