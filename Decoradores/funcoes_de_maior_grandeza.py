# Funções de maior grandeza - High Order Function - HOF
# O que isso significa ?

# Quando uma linguagem de programação suporta HOF, infica que podemos ter funções que retornam outras funções como resultado ou mesmo que podemos 
# passar funções como argumentos para outras funções, e até mesmo criar variaveis do tipo de funções nos nossos programas.

# OBS na seção de funções, nos utilizamos isso

# Ex:
def somar(a,b):
    return a+b

def diminuir(a,b):
    return a-b

def multi(a,b):
    return a*b

def dividir(a,b):
    return a/b
def calcular(num1,num2,funcao):
    return funcao(num1,num2)

# Testando
print(calcular(4,5,somar))

print(calcular(4,5,multi))

print(calcular(4,5,diminuir))

print(calcular(4,5,dividir))

# Em python, as funções são cidadões de primeira classe, First Class Citizen

# Nested Functions - Funções Aninhadas
# Em python podemos ter funções dentro de funções, que são conhecidas por nested functions ou tambem inner functions(Funções internas)
# Ex:
from random import choice
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ','Suma daqui ','Gosto muito de voce '))
    return humor() + pessoa

print(cumprimento('Caio'))

# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahaa','kkkkkkkkkkkkkkkk','jajajjajajajaj'))
    return rir
# Testando
rindo = faz_me_rir()
print(rindo())

# Inner Functions (Funções internas / Nested functions) podem acessar o escopo de funções mais externas 

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaahah','lololololololol','lulululululul'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('caio')
print(rindo())