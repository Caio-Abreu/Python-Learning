print(len('Caio abreu'))
print(len([1,2,3,4,5,6,7]))
print(len((1,2,3,4,5,6,7)))
print(len({1,2,3,4,5,6,7}))
print(len(range(0,10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte

# Dunder len
print('Caio abreu'.__le__(0))

# abs() -> Retorna o valor absoluto(valor positivo) de um numero inteiro ou real. De forma baisca, seria o seu valor real sem o sinal

# Exemplo abs()
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# sum() -> recebe como parametro um interavle, podendo receber um valor inicial, e retorna a soma total dos elementos
# OBS: O valor inicial default = 0

# Ex:
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5],5)) # 5 sera o valor inicial de sum somando assim ao interavel
print(sum([3.14,5.678]))
print(f'Tupla {sum((1,2,3,4,5))}')
print(f'Conjunto {(sum({1,2,3,4,5}))}')
print(sum({'a':1,'b':2,'c':3,'d':4,'e':5}.values()))

# round() -> Retorna um numero arredondado para n digito de precisao apos a casa decimal. Se a precisao nao for informada retorna o inteiro mais proximo da entrada

# Ex:
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.212121212,2))
print(round(1.21999999,9))
print(round(1.21999999,))