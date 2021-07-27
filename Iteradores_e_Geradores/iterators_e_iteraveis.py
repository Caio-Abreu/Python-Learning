# iterator -> Objeto que pode ser iterado, um objeto que retorna um dado, sendo  um elemento por vez quando uma função next() é chamada
# iterable -> Objeto que ira retornar um iterator quando a função ite() for chamada

nome = 'Geek' # iterable mas nao um iterator
numeros = [1,2,3,4,5,6,7,8,9] # iterable mas nao um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

# Por cima dos panos é isso que acontece
for letra in nome:
    print(f'{letra}')