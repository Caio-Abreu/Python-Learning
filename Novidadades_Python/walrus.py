# O operador walrus permite fazer a atribuição e retorno de valor em uma unica expressão 
# variavel := expressão

nome = 'Caio abreu'
print(nome)

print(nome := 'Caio abreu')

# Python 3.7

# cesta = []
# fruta = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta= input('Informe a fruta: ')

# Python 3.8
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)