# Para ler ou escrever dados em arquivo do sistema operacional o software precisa ter permissão
# - Permissao de leitura -> para ler o arquivo
# - Permissao de escrita -> para escrever o arquivo

# StringIO -> Utilizando para ter e criar arquivos em memoria

# Primeiro fazemos o import
from io import StringIO
mensagem = 'Mensagem comum'


# Podemos criar um arquivo em memoria ja com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt','w')

# Agora tendo o arquivo, podemos utilizar tudo que ja sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('\nOutro texto')
# Movendo o cursor pro inicio e lendo de novo
arquivo.seek(0)
print(arquivo.read())