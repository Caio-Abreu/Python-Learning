# filter() -> serve para filtrar dados de uma determinada coleção
# Biblioteca para trabalhar com dados estastisticos
import statistics

valores = 1,2,3,4,5,6
media = (sum(valores))/ len(valores)
print(media)

dados =[1.2,2.7,0.8,4.1,4.3,-0.1]

# Calculando media dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# Assim como map(), filter() recebe dois parametros, uma função e um interavel

res = filter(lambda x:x>media,dados)
print(list(res))
print(tuple(res)) # Apos ser utilizado assim como map os dados sao excluidos da memoria

paises=['','Brasil','','Argentina','chile','','equador','','venezuela']
res = filter(None,paises)
print(list(res))

# Diferença entre map() e filter()
# map() sempre retorna um objeto mapeando a função para cada elemento do interavel
# filter() retorna um objeto filtrando apenas os elementos de acordo com a função

# Exemplo complexo

user = [
    {"username": "samuel","tweets": ["Eu adoro bolos","Eu adoro pizzas"]},
    {"username": "carla","tweets": ["Eu adoro bolos"]},
    {"username": "jeff","tweets": []},
    {"username": "bob","tweets":["Eu adoro doce","Eu adoro bolo"]}
]
print(user)

# Filtrar que os usuarios estão inativos no twitter

# inativos = list(filter(lambda u: len(u['tweets']) == 0,user))
inativos = list(filter(lambda u: not u['tweets'],user))
print(inativos)

# Combinar filter() e map()
nomes = ['vanessa','Ana','Maria']

# Devemos criar uma lista contento sua instrutora é + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome:f'sua instrutora é {nome}',filter(lambda nome:len(nome)<5,nomes)))
print(lista)