# open() -> Utilizamos apenas um parametro de entrada que no caso é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper
# e é com ele que trabalhamos então

# docs.python.org/3/library/functions.html#open
# Por padrão a função open abre o arquivo para leitura. Este arquivo deve existir senão retornara FileNotFoundError

# Ex:
arquivo = open('Leitura_de_arquivos/texto.txt')
print(arquivo)
print(type(arquivo))

print(arquivo.read()) # Lê todo o conteudo do arquivo