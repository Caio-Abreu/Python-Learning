# Modos de abertura de arquivo

# r -> abre para leitura - padrao.
# w -> abre para escrita - sobrescreve caso o arquivo ja existe.
# x -> abre para escrita - somente se o arquivo nao existir.
# a -> abre para escrita - adicionando o conteudo ao final do arquivo.
# + -> abre para o modo de atualização - leitura e escrita.

# Ex: 'x'
try:
    with open('Leitura_de_arquivos/x.txt','x') as arquivo:
        arquivo.write('Teste de conteudo')
except FileExistsError:
    print('Este arquivo ja existe')

# Ex: 'a'
# frutas = ['abacate','morango','maça','abacaxi','manga'] # Alguns exemplos de frutas
# with open('Leitura_de_arquivos/frutas.txt','a') as arquivo:
#     while True:
#         fruta = input('Informe uma fruta ou digite sair: ')
#         fruta = fruta.lower() # Ira colocar a palavra do usuario em minusculo para nao ter erro gramatical
#         if fruta in frutas:
#             arquivo.write(fruta)
#             arquivo.write('\n')
#         elif fruta == 'sair':
#             break
#         else:
#             print('Fruta invalida')
# OBS: abrindo no modo 'a' -> append, se o arquivo nao existir sera criado. Caso exista, o novo conteudo sera adicionado ao final

with open('Leitura_de_arquivos/novo.txt','r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Novo topo!\n')
    arquivo.write('Nova linha!\n')
    arquivo.write('Mais uma linha!\n')
