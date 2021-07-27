# Nao é mais uma função integrada (built in)
# Agora temos que importar e utilizar a função a partir do modulo functools

# Vamos utilizar a função reduce() para multiplicar todos o snumeros de uma lista

from functools import reduce

dados = [1,2,3,4,5,6,7,8,9,10]

# Para utilizar o reduce() precisamos de uma função que receba dois parametros
multi = lambda x,y:x*y

res = reduce(multi,dados)
print(res)

# Utilizando um loop normal, preferivel ao contrario de reduce() que é só utilizado quando necessario
res = 1
for n in dados:
    res = res*n

print(res)