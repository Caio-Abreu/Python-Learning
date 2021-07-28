# Geradores(Generators) são Iterators(Iteradores):
# Diferença entre funções e generator function (função geradora)

# |Funções                                   |Generator function
# |utiliza return                              |utiliza yield
# |retorna uma vez                             |podem utilizar yield multiplas vezes
# |Quando executada, retorna um valor          |quando executada, retorna um generator


# Exemplo Generator function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1
# OBS uma generator function não é um Generator. Ele gera um generator. ok ?
gen = conta_ate(5)

for num in gen:
    print(num)

gen = list(conta_ate(5))
print(gen)


