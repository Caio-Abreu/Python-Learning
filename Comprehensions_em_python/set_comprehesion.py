# Exemplos 
numeros = {num for num in range(1,7)}
print(numeros)

# Outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# OBS: Faça uma alteração na estrutura acima para gerar um dicionario ao inves de set
numeros = {x:(x ** 2) for x in range(10)}
print(numeros)

# Pra finalizar
letras = {letra for letra in 'Caio abreu'} # não vai ordenado e nem receber valores repetidos
print(letras)
