# Teste de String em Python
nome = 'Caio abreu'

# Tudo maiusculo
print(nome.upper())

# Tudo minusculo 
print(nome.lower())

# Slice de uma string
print(nome[0:4])
print(nome[5:10])

# Separar em uma lista e pecorrer ela
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])

# Inverter uma string inteira
print(nome[::-1])

# Substituir uma letra por outra
print(nome.replace('a','i'))
print(type(nome))