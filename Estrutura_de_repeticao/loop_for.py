nome = 'Geek University'
lista =[1,3,5,7,9]
numeros = range(1,10)

# Exemplo de for 1
for letra in nome:
    print(letra)

print('---------------------------')
# Exemplo 2
for a in lista:
    print(a)

print('---------------------------')
# Exemplo de for 3 in range
# range(valor inicial, valor final) o valor final nao é incluso 
for numero in range(1,10):
    print(numero)

print('---------------------------')

for i,v in enumerate(nome):
    print(i,v)

print('---------------------------')

# Quando nao precisamos do indice podemos descartar colocando um underline (_)
for _, letra in enumerate(nome):
    print(letra)

print('---------------------------')
for valor in enumerate(nome):
    print(valor)

soma = 0
# qtd = int(input('Quantas vezes esse loop deve rodar?'))

# for n in range(1, qtd +  1):
#     num = int(input(f'Informe o {n}/{qtd} valor:'))
#     soma = soma + num 

# print(f'A soma é {soma}')

for letra in nome:
    print(letra, end='3')


for num in range(1,11):
    print('\1' *num)