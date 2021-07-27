# Ou tuple comprehension

nomes= ['Caio','Carlos','Carla','Cassiano','Cristina','Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# List comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator Express
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)