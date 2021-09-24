# Generated by Django 3.2.7 on 2021-09-21 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.IntegerField()),
                ('rg', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('data_nascimento', models.DateField()),
                ('possui_hailitacao', models.BooleanField()),
                ('valor_salario', models.FloatField()),
                ('carga_horaria_semanal', models.IntegerField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento')),
            ],
        ),
    ]
