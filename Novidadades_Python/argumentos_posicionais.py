# Argumentos somente posicionais

valor = '67.3'
print(float(valor))

def cumprimenta_v1(nome):
    return f'Ola {nome}'

print(cumprimenta_v1('caio'))
print(cumprimenta_v1(nome='bruno'))

print('----------------------------------------------------------------------')

def cumprimenta_v2(nome, /):
    return f'Ola {nome}'

print(cumprimenta_v2('caio'))
#print(cumprimenta_v2(nome='bruno')) # Não ira funcionar

print('----------------------------------------------------------------------')

def cumprimenta_v3(*,nome):
    return f'Ola {nome}'
# print(cumprimenta_v3('caio')) Nao vai funcionar pois nao esta identificando o parametro
print(cumprimenta_v3(nome='bruno'))