# Retaforando uma função
def quadrado(num):
    return num ** 2

print(quadrado(10))

ret = quadrado(6)
print(ret)

def soma(a,b):
    return a+b

def multiplica(num1,num2):
    return num1*num2

def outra(num1,b,msg):
    return(num1+b)*msg

print(soma(2,3))
print(multiplica(2,3))
print(outra(2,3,'Geek'))

def nome_completo(nome,sobrenome):
    return f'seu nome completo é {nome} {sobrenome}'

print(nome_completo('caio','abreu'))

# Argumentos nomeados (KeyWord Arguments)
print(nome_completo(nome='caio',sobrenome='abreu'))
print(nome_completo(sobrenome='abreu',nome='caio'))

# Erro comum em return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total+num
    return total

lista = [1,2,3,4,5,6,7,8]
print(soma_impares(lista))