
arquivo = open('Leitura_de_arquivos/texto.txt')
print(arquivo.read())
print(arquivo.read() +'Vazio')

# seek() -> É utilizada para movimentar o cursor pelo arquivo. O parametro indica onde iremos colocar o cursor 
# Movimentando o cursor peplo arquivo com a função seek() pois apos a primeira leitura o cursor vai pro final do arquivo
arquivo.seek(19)
print(arquivo.read())

print('--------------------------------------------------')

arquivo.seek(0)

# readline() -> função que lê arquivo linha a linha
print(arquivo.readline())
ret = arquivo.readline()
print(type(ret)) # é transforma em string

print('--------------------------------------------------')

arquivo.seek(0)
# redlines() -> diferente da readline() separa as linhas do arquivo .txt em uma lista
linhas = arquivo.readlines()
print(len(linhas))
print(linhas)

print('--------------------------------------------------')

arquivo.seek(0)
# OBS: quando abrimos um arquivo com a função open() é criada uma conexao entre o arquivo no disco do computadore o nosso programa
# essa conexao de streaming ao finalizar os trabalhos com o arquivo devemos fechar essa conexao. Para isso utilizamos a função close()

# 1 - Abrir o arquivo:
# 2 - Trabalhar o arquivo:
# 3 - Fechar o arquivo

# 1:
print(arquivo)
# 2:
print(arquivo.read(50)) # O parametro passado limita o numero de caracteres mostrado 
print(arquivo.closed) # False
# 3:
arquivo.close()
print(arquivo.closed) # True
