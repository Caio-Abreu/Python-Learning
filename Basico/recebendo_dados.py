# Entrada de dados

# print("Qual seu nome?")
# nome = input()
nome = input("Qual seu nome?")

#print('Seja bem-vindo(a) %s' % nome)
#print('Seja bem-vindo(a) {0}'.format(nome))

print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade?")
# idade= input()

idade = int(input("Qual sua idade ?"))

# Processamento

# Saida de dados
#print('A %s tem %s anos'% (nome,idade))
#print('A {0} tem {1} anos'.format(nome,idade))
print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2021-int(idade)}')