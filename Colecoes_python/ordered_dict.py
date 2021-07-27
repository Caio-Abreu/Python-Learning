from typing import OrderedDict


dicionario = OrderedDict({'a':1,'b':2,'c':3,'d':4,'e':5})
for chave, valor in dicionario.items():
    print(f'chave={chave} e valor={valor}')

# Entendendo a diferença entre dict e ordered dict
# Dict
dict1 = {'a':1,'b':2}
dict2 = {'b':2,'a':1}
print(dict1 == dict2)

# Ordered Dict
Ordereddict1 = OrderedDict({'a':1,'b':2})
Ordereddict2 = OrderedDict({'b':2,'a':1})
print(Ordereddict1 == Ordereddict2)