# Metodos de Data e hora

import datetime

# Com now podemos especificar o timezone (fuso-horario)
agora = datetime.datetime.now() # now == agora
print(agora)

hoje = datetime.datetime.today() # today == hoje
print(hoje)

print('---------------------------------------------------------------------------')

# Mudanças ocorrendo a meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now()+datetime.timedelta(days=1)) , datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

print('---------------------------------------------------------------------------')

# Encontrar o dia da semana. weekday()
# Os dias da semana do metodo weekday() começa em 0, sendo esta a segunda-feira

# 0 - segunda
# 1 - terça
# 2 - quarta
# 3 - quinta
# 4 - sexta
# 5 - sabado
# 6 - domingo

print(manutencao.weekday())

# aniversario = input('Qual a data do seu nascimento ? dd/mm/yy: ')
# aniversario = aniversario.split('/')
# aniversario = datetime.datetime(year=int(aniversario[2]),month=int(aniversario[1]),day=int(aniversario[0]))
# if aniversario.weekday() == 0:
#     print('Voce nasceu em uma segunda-feira')
# elif aniversario.weekday() == 1:
#     print('Voce nasceu em uma terça-feira')
# elif aniversario.weekday() == 2:
#     print('Voce nasceu em uma quarta-feira')
# elif aniversario.weekday() == 3:
#     print('Voce nasceu em uma quinta-feira')
# elif aniversario.weekday() == 4:
#     print('Voce nasceu em uma sexta-feira')
# elif aniversario.weekday() == 5:
#     print('Voce nasceu em uma sabado')
# else:
#     print('Voce nasceu em uma domingo')

# Formatando datas/horas com strtime() (String Format Time)
# dd/mm/yy hora:minuto

hoje = datetime.datetime.today()

print(hoje)

# hoje_formatada = hoje.strftime('%d/%m/%y')
hoje_formatada = hoje.strftime('%d de %B de %Y')

print(hoje_formatada)

from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"
print(formata_data(hoje))

nascimento = datetime.datetime.strptime('27/03/2000','%d/%m/%Y') # Ja converte direto da string para hora
print(nascimento)

# Somente hora
almoco = datetime.time(12,30,0)
print(almoco)

import timeit,functools

# Marcando tempo de execução do nosso codigo com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
print(tempo)

# List comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=1000)
print(tempo)

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma +num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste,2), number=10000))