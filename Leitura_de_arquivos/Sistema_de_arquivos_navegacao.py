# os -> Operating System - Sistema operacional

import os
# getcwd() -> pega o current work directory - diretorio de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # Estamos em E:\Codes_WebModerno\Python (na minha maquina)

# Para mudar o diretorio, podemos utilizar o chdir()
# os.chdir('..')
# print(os.getcwd()) # E:\Codes_WebModerno

# os.chdir('..')
# print(os.getcwd()) # E:\

# os.chdir('..')
# print(os.getcwd()) # E:\

# Podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('E:\Codes_Webmoderno\Python'))

# OBS para usuarios windows
# Se voce estiver usando windows tera que ter cuidado ao verificar diretorios

# Podemos identificar o sistema operacional com o modulo os
print(os.name) # posix (linux e mac), nt (windows)
# print(os.uname) no windows nao tem
import sys
print(sys.platform)
print(os.getcwd())
res = os.path.join(os.getcwd(),'Basico') # o os.path.join() recebe dois parametros, sendo o primeiro o diretorio atual e o segundo o ddiretorio que sera juntado ao atual
print(res)
print(os.getcwd())

# Podemos listar os arquivos e diretorios
print(os.listdir())
print(len(os.listdir()))
print(os.listdir('E://'))

# Mais detalhes
scanner = os.scandir()
arquivos = list(os.scandir('E://'))
print('----------------------------------------------------')
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].inode()) # ???
print(arquivos[0].is_dir()) # é um diretorio ? True
print(arquivos[0].is_file()) # É um arquivo ? False
print(arquivos[0].is_symlink()) # É um link simbolico ? False
print(arquivos[0].path) # Caminho até o arquivos
print(arquivos[0].stat()) # ???

# OBS quando utilizamos a função scandir() nos precisamos fecha-la, assim quando abrimos um arquivo
scanner.close()