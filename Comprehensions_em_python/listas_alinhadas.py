# Matriz em python

listas = [[1,2,3], [4,5,6],[7,8,9]] # Matriz 3x3
print(listas)
print(type(listas))

print(listas[0][1])
print(listas[2][1])

[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1,4)]for valor in range(1,4)]
print(velha)

# Gerando valor iniciais
print([['*' for i in range(1,4)] for j in range(1,4)])