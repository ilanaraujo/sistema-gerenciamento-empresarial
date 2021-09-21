# Arquivo utilizado para melhor organização das funções adicionais necessárias

def calcula_prazo(data_atual, horas_para_concluir, horas_semanais):
    
    # Calcula o número de semanas restantes dividindo a quantidade de horas apra conclusão pela quantidade
    # de horas semanais trabalhadas no projeto. Acrescenta uma semana caso sobrem horas que não sejam 
    # suficientes para compeltar uma semana
    semanas_restantes = horas_para_concluir // horas_semanais + (horas_para_concluir%horas_semanais != 0)

    # Converte o número de semanas restantes para dias
    dias_restantes = 7*semanas_restantes

    # Retorna a data do calculo do prazo acrescida dos dias restantes para a conclusão do projeto
    return data_atual.timedelta(days = dias_restantes)
