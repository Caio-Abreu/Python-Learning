# Trabalhando com deltas de data e hora
# data_inicial = dd/mm/yyy 12:55:34:00
# data_final = dd/mm/yyy 17:28:14:00
# delta = data_final - data_inicial

import datetime
# Data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2022,3,27,0)

# Calculando o Delta
tempo_para_aniversario = aniversario - data_hoje
print(tempo_para_aniversario) # Delta
print(tempo_para_aniversario.days) # Dias apenas
print(f'Faltam {tempo_para_aniversario.days} dias, {tempo_para_aniversario.seconds // 60} horas,')

print('---------------------------------------------------------------------------------')

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3) # Fornece resultado = 3 dias
print(regra_boleto)

vencimento_do_boleto = data_da_compra + regra_boleto
print(vencimento_do_boleto)