# Exemplos

numeros ={'a':1,'b':2,'c':3,'d':4,'e':5}
quadrado ={chave:valor **2 for chave,valor in numeros.items()} # Funciona tanto em dict/tuple/set
print(quadrado)

chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]:valores[i] for i in range(0,len(chaves))} # mistura ira virar um dict a partir dessa linha de codigo
print(mistura)

# Exemplo com logica condicional
numeros = [1,2,3,4,5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
