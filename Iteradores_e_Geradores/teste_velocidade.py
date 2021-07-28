# Teste de velocidade com expressões geradoras

# Generators (geradores)
def nums():
    for num in range(1, 10):
        yield num
    
ge1 = nums() # é um objeto
print(ge1)
print(next(ge1))
print(next(ge1))
print(next(ge1))
print(next(ge1))
print(next(ge1))
print(next(ge1))

# Generator expression

ge2 = (num for num in range(1,10)) # é uma expressão
print(ge2)
print(next(ge2))
print(next(ge2))

# Realizando o teste de velocidade
import time

# Generator expression
gen_inicio = time.time()
print(sum(num for num in range(100_000_000))) # 100 milhoes
gen_tempo = time.time() - gen_inicio

# List comprehesion
list_inicio = time.time()
print(sum([num for num in range(100_000_000)])) # 100 milhoes
list_tempo = time.time() - list_inicio

print(f'Generator expression levou {gen_tempo}') # 6.4 seg
print(f'List comprehesion levou {list_tempo}') # 8.2 seg 