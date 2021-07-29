# Preservando metadatas com wraps
# Metadata -> São dados intrisecos em arquivo
# wraps -> São funções que envolvem elementos com diversas finalidades

# Problema


# def ver_log(funcao):
#     def logar(*args, **kwargs):
#         """Eu sou uma função (logar) dentro de outra"""
#         print(f'Voce esta chamando {funcao.__name__}')
#         print(f'Aqui a documentaçã: {funcao.__doc__}')
#         return funcao(*args,**kwargs)
#     return logar

# @ver_log
# def soma(a,b):
#     """Somar dois numeros"""
#     return a + b

# print(soma(10,30))
# print(soma.__name__) #soma
# print(soma.__doc__) # soma dois numeros

# Resolução do problema
from functools import wraps
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args,**kwargs)
    return logar

@ver_log
def soma(a,b):
    """Somar dois numeros"""
    return a + b

print(soma(10,30))
print(soma.__name__) # soma
print(soma.__doc__) # soma dois numeros
print(help(soma))
