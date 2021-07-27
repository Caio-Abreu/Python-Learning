# Debugando com PDB
# PDB -> Python Debugger

# OBS : utilizar print para debugar o codigo é ruim
# def dividir(a,b):
#     print(a,b)
#     try:
#         return int(a)/int(b)
#     except (ValueError, ZeroDivisionError) as err:
#         return f'Ocorreu um problema: {err}'

# print(dividir(4,7))

# -----------------------------------------------------------------------------------------

# Jeito correto
def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
print(dividir(4,7))

# -----------------------------------------------------------------------------------------

# Exemplo com o PDB - Python Debugger

# Comandos basicos do PDB
# l (lista onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)
# import pdb

# nome = 'Angelina'
# sobrenome = 'Jolie'
# pdb.set_trace()
# nome_completo = nome + ' ' + sobrenome
# curso = 'Programação em python: essencial'
# final = nome_completo + ' faz o curso ' + curso
# print(final)

# -----------------------------------------------------------------------------------------

# nome = 'Angelina'
# sobrenome = 'Jolie'
# import pdb; pdb.set_trace()
# nome_completo = nome + ' ' + sobrenome
# curso = 'Programação em python: essencial'
# final = nome_completo + ' faz o curso ' + curso
# print(final)
# Por quê utilizar este formato ?
# Utilizamos na linha que queremos encontrar o problema e apos isso é removido

# -----------------------------------------------------------------------------------------

# A partir da versão 3.7 do Python, nao é mais necessario importar a biblioteca pdb, pois o comando debug foi incorporado como função
# built-in (integrada) chamada breakpoint()
# Comandos basicos do PDB
# l (lista onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em python: essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: cuidado com conflitos entre nomes de variaveis e os comandos de pdb (l,n,p,c)