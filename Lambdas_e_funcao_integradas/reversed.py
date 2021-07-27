# Exemplos

lista =[1,2,3,4,5,6]
res = reversed(lista)
print(res)

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto
# Lista 
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Em conjunto nao definimos a ordem dos elementos
# Conjunto
print(set(reversed(lista)))

# Podemos iterar sobre reversed
for letra in reversed('Caio Abreu'):
    print(letra, end='')

print('\n')
# Podemos fazer o mesmo sem for
print(''.join(list(reversed('Caio abreu'))))

# Ja vimos como fazer isso mais facil com o slice de strings
print('Caio abreu'[::-1])

# Podemos tambem usar o reversed() para fazer um loop reverso
for n in reversed(range(0,10)):
    print(n)

# Assim como conseguimos fazer sem precisar do reversed()
for n in range(9,-1,-1):
    print(n)