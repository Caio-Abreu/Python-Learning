print('Geek university')

def quadrado(numero):
    return numero ** 2

def exponencial(numero,potencia=2): # Quando informado o valor da pontencia é opcional passar um novo valor para o parametro  
    return numero ** potencia

print(exponencial(2,3))
print(exponencial(3,2))

print(exponencial(3)) # Por padrao eleve ao quadrado
print(exponencial(3,4)) # Eleva a potencia informada pelo usuario 

# Erro pois o parametro a direita precisa receber um valor por padrão
# def teste(num=2,potencia):
#     return num ** potencia

# print(teste(6))

# Exemplo mais complexo
def mostra_informacao(nome='Geek',instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome =='Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Ola {nome} !!!'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Caio'))

# Por quê utilizar parametros com valor default ?
# - Nos perimte ser maisss flexiveis nas funções
# - Evita erros com parametros incorretos
# - Nos permite trabalhar com exemplos mais legiveiss do codigo

# Exemplos

def soma(num1,num2):
    return num1+num2

def subtracao(num1,num2):
    return num1 - num2

def mat(num1,num2,fun=soma):
    return fun(num1,num2)


print(mat(2,3)) 
print(mat(2,3,subtracao)) 

# varivaeis globais e locais

instrutor = 'caio abreu' # Variavel global

def diz_oi():
    instrutor = 'Python'# Variavel local
    erro= 'Error'
    return f'oi {instrutor}'
print(diz_oi())
#print(erro) NameError
# Variavel local > global

total = 1

def incrementa():
    global total #Sem o global a variavel global total nao podera ser incrementada
    total += 1
    return total
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções e tambem tem uma forma especial de esscopo de variavel
def fora():
    contador = 0 
    def dentro():
        nonlocal contador
        return contador + 1
    return dentro()

print(fora())
