# Exemplo

numeros = [6,8,2,20,12]
print(numeros)
print(sorted(numeros)) # Sempre retorna uma lista independente se é tupla ou outro interavel
print(numeros)

# Adicionando parametros

print(sorted(numeros,reverse=True)) # Oderna na ordem decrescente 

# Podemos utilizar o sorted() para coisas mais complexas

user = [
    {"username": "samuel","tweets": ["Eu adoro bolos","Eu adoro pizzas"]},
    {"username": "carla","tweets": ["Eu adoro bolos"],"cor":"amarelo"},
    {"username": "jeff","tweets": [],"cor":"preto"},
    {"username": "bob","tweets":["Eu adoro doce","Eu adoro bolo"]}
]

print(user)
# Ordenando em ordem alfabetica
print(sorted(user,key=lambda usuario: usuario["username"]))

musicas =[
    {"titulo":"Thunderstruck", "Tocou":3},
    {"titulo":"Dead skin mask", "Tocou":2},
    {"titulo":"Back in Black", "Tocou":4},    
    {"titulo":"When we were young", "Tocou":32}    
]

# Musica que menos tocou pra que mais tocou
print(sorted(musicas,key=lambda musica:musica['Tocou']))

# Musica que mais tocou pra que menos tocou
print(sorted(musicas,key=lambda musica:musica['Tocou'],reverse=True))