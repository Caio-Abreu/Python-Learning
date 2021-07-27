numeros = [1,2,3]

ret_pop = numeros.pop()

print(f'retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'retorno de print: {ret_pr}')

# Exemplo função
def quadrado_de_7():
    return 7*7
    
ret = quadrado_de_7()

print(f'Retorno {ret}')
# OU
print(f'Retorno {quadrado_de_7()}')

# Retaforando a primeira função
def diz_oi():
    return 'Oi'

print(diz_oi())

alguem ='Pedro'
print(diz_oi()+alguem)

def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return'b'
print(nova_funcao())

def num_funcao():
    return 2,3,4,5

print(num_funcao())

# Vamos criar uma função para jogar moeda
from random import random

def joga_moeda():
    # random() gera um numero entre 0 e 1
    valor = random()
    if valor > 0.5:
        return'Cara'
    return'Coroa'
print(joga_moeda())
 
# Erros comuns em utilização de erro

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    # else: else desnecessario
    return False
    
print(eh_impar())