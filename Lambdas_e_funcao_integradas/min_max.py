# max() -> Retorna o mais valor de um interavel ou o mair de dois ou mais elementos

# Ex:
lista = [1,2,4,6,8,20,23]
print(max(lista))

tupla = (1,2,4,6,8,20,23)
print(max(tupla))

conj = {1,2,4,6,8,20,23}
print(max(conj))

dic = {'a':1,'b':2,'c':4,'e':6,'f':8,'g':20,'h':23}
print(max(dic.values()))

# Faça um programa que receba dois valores do usuario e mostre o maior
# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))

# print(max(val1,val2))

print(min(4,67,54))
print(min('a','b','c','d'))
print(min('Caio abreu'))

# min() -> Retorna o menor valor de um interavel ou o menor de dois ou mais elementos

lista = [1,2,4,6,8,20,23]
print(min(lista))

tupla = (1,2,4,6,8,20,23)
print(min(tupla))

conj = {1,2,4,6,8,20,23}
print(min(conj))

dic = {'a':1,'b':2,'c':4,'e':6,'f':8,'g':20,'h':23}
print(min(dic.values()))

# Faça um programa que receba dois valores do usuario e mostre o menor
# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))

# print(min(val1,val2))

print(min(4,67,54))
print(min('a','b','c','d'))
print(min('Caio abreu')) # O menor caractere é o espaço entre as strings

# Outros exemplos

nomes = ['Caio','Ana','Zeus','Adão','Bruno','Dani','Bia']
print(max(nomes))
print(min(nomes))

print(max(nomes, key= lambda nome: len(nome))) # Nome com mais letras
print(min(nomes, key= lambda nome: len(nome))) # Nome com menos letras, devolve o primeiro encontrado

musicas =[
    {"titulo":"Thunderstruck", "Tocou":3},
    {"titulo":"Dead skin mask", "Tocou":2},
    {"titulo":"Back in Black", "Tocou":4},    
    {"titulo":"When we were young", "Tocou":32}    
]
print(max(musicas,key=lambda musica: musica['Tocou']))
print(min(musicas,key=lambda musica: musica['Tocou']))

# Desafio Imprima somente o titulo da musica
print(max(musicas,key=lambda musica: musica['Tocou'])['titulo'])
print(min(musicas,key=lambda musica: musica['Tocou'])['titulo'])

# Como achar a musica mais tocada e menos tocada sem usar max() e min()
max = 0
for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']
        
for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['titulo'])

min = 9999
for musica in musicas:
    if musica['Tocou'] < min:
        min = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(musica['titulo'])
