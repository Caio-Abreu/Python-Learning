# zip() -> Cria um interavel (zip object) que agrega elemento de cada um dos iteraveis passados como entrada em pares

# Ex:
from typing import final


lista1 = [1,2,3]
lista2 = [5,6,7]

zip1 = zip(lista1,lista2,'abc')
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla,set ou dicionario

print(list(zip1))

zip1 = zip(lista1,lista2,'abc')
print(tuple(zip1))

zip1 = zip(lista1,lista2,'abc')
print(set(zip1))

zip1 = zip(lista1,lista2)
print(dict(zip1))

# O zip() trabalha com o menor interavel, logo ele ira se basear no tamanho do menor interavel 
lista3 = [7,8,9,10,11]

zip1 = zip(lista1,lista2,lista3)
print(tuple(zip1))

# Podemos usar diferentes interaveis com zip
tupla = 1,2,3,4,5
lista = [6,7,8,9,10]
dicionario = {'a':11,'b':12,'c':13,'d':14,'e':15}

zt = zip(tupla,lista,dicionario)
print(list(zt))

# Lista de tuplas

dados =[(0,1),(1,2),(2,3),(3,4),(4,5)]
print(list(zip(*dados)))

# Exemplo mais complexos
prova1 = [80,91,78]
prova2 = [80,91,78]
alunos = ['maria','pedro','carla']

final = {dado[0]:max(dado[1],dado[2]) for dado in zip(alunos,prova1,prova2)}
print(final)

# Podemos utilizar o map
final1 = zip(alunos, map(lambda nota:max(nota),zip(prova1,prova2)))

print(dict(final1))