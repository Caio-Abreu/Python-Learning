# Escrevendo em arquivos CSV

# reader() "leitor", writer() "escritor"
# writerow() -> Escreve uma linha

# from csv import writer

# with open('manipulando_JSON_CSV/filmes.csv','w') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Titulo','Genero','Duracao'])
#     while filme != 'sair':
#         filme = input('Informe o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Informe o genero: ')
#             duracao = input('Informe a duração (em minutos): ')
#             escritor_csv.writerow([filme,genero,duracao])

# DictWriter
# OBS: as chaves do dicionario devem ser as mesmas utilizadas como cabeçalho
from csv import DictWriter

with open('manipulando_JSON_CSV/filmes.csv','w') as arquivo:
    cabecalho = ['Titulo','Genero','Duracao']
    escritor_csv = DictWriter(arquivo,fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Titulo":filme,"Genero":genero,"Duracao":duracao})