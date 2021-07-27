# Fazemos mapeamento de valores para função

import math

def area(r):
    return math.pi *(r**2)

print(area(2))

raios = [2,5,7.1,0.3,10,44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parametros: O primeiro a função, o segundo um interavel
areas = map(area,raios)
print(areas)
print(list(areas))
# print(tuple(areas))

# Forma 3 - map com lambda
print(list(map(lambda r: math.pi*(r**2),raios))) 

# Obs: apos utilizar o map() depois da primeira utilização do resultado, ele zera

# Mais um exemplo 

cidades = [('Berlim',29),('RJ',34),('SP',22),('RS',32),('MG',11),('GO',19)]

c_para_f = lambda dado: (dado[0],(9/5)*dado[1]+32)
print(list(map(c_para_f,cidades)))