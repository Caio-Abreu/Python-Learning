# Doctestes

# Para rodar um test do doctest:
# python -m doctest -v nome_do_modulo.py

# def soma(a,b):
#     """Soma os numeros a e b
#     >>> soma(1,2)
#     3
#     """
#     return a + b

# print(soma(3,4))
# print(soma.__doc__)

# Outro exemplo, Aplicando TDD

def duplicar(valores):
    """duplica os valores em uma lista
    >>> duplicar([1,2,3,4])
    [2,4,6,8]
    >>> duplicar([])
    []
    >>> duplicar(['a','b','c'])
    ['aa','bb','cc']
    >>> duplicar([True,None])
    TraceBack(most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

def fala_oi():
    """Fala oi
    >>> fala_oi()
    'oi'
    """
    # "oi"
    return "oi"
# OBS: Dentro do doctest, o Python nao reconhece string com aspas duplas. Precisar ser aspas simples

# Um ultimo caso estranho...

def verdade():
    """Retorna verdade
    >>> verdade()
    True
    """
    return True