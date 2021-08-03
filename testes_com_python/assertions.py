# Assertions (checagens/questionamentos)

def soma_numeros_positivos(a,b):
    assert a >0 and b >0, 'Ambos numeros precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2,4)
print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'eu estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# Alerta: cuidado ao utilizar 'assert'
# Não utilize como um if ou algo do tipo, pois pode ser burlado facilmente