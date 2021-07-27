# SyntaxError -> Escrever algo que o python nao reconhece como linguagem 
# Ex:
# def funcao:
    # print('Caio abreu')
# None = 1
# return

# NameError -> Ocorre quando uma variavel ou função nao foi definida
# Ex:
# print(geek)
a=18
msg= None # conserta o erro
if a < 10:
    msg = 'É maior que 10'
print(msg)

# TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado
# Ex:
# print(len(5))
# print('Geek'+[])
print('Geek'+' University')

# IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um indice invalido
# Ex:
lista = ['Geek']
# print(lista[0][10])

# ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
# Ex:
# print(int('Geek'))

# KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que nao existe
# Ex:
# dic ={'python':1}
# print(dic['geek'])

# AttributeError -> ocorre quando uma variavel nao tem um atributo/função
# Ex:
tupla = 1,2,3,4,5,6,7
# print(tupla.sort())

# IndentationError -> Ocorre quando nao respeitamos a identação do python (4 espaços)
# Ex:
# def nova():
# print('Geek')
# for i in range(10):
# i+1