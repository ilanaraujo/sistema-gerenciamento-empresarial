from django import forms
from .models import Departamento

class DepartamentoForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=255)
    
    class Meta:
        model = Departamento
        fields = ['nome']
        exclude = ['id', 'numero_funcionarios', 'numero_projetos']


