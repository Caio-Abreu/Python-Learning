# Exemplos 

numeros =[1,2,3,4,5]
res = [numero *10 for numero in numeros]
print(res)

# A primeira parte: for numero in numeros
# A segunda parte: nuemro * 10

res = [numero /2 for numero in numeros]
print(res)

# List Comprehension versos Loop
# Loop
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)
print(numeros_dobrados)

# List Comprehesion
print([numero * 2 for numero in numeros]) # Sempre entre colchetes

# Outros exemplos

# 1
nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2 
amigos =['maria','julia','pedro','guilherme','vanessa']
print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1,10)])

# 4
print([bool(valor) for valor in [0,[],'',True,1,3.14]])

# 5
print([str(numero) for numero in [1,2,3,4,5]])