# raise -> Lança exeções
# Nao é uma função e sim uma palavra reservada assim como def
# Criamos a nossa mensagem de erro raise TipoDeErro('Mensagem de erro')

# Exemplos:
# def colore(texto,cor):
#     if type(texto) is not str:
#         raise TypeError('texto precisa ser uma string')
#     if type(cor) is not str:
#         raise TypeError('cor precisa ser uma string')
#     print(f'O texto {texto} sera impresso na cor {cor}')

# colore(True,'azul')

def colore(texto,cor):
    cores = 'verde','amarelo','azul','branco'
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma dessas: {cores}')
    print(f'O texto {texto} sera impresso na cor {cor}')

colore('Geek','aa')

# O raise finaliza a função assim como o return, nada sera executado apos ele ser lido
