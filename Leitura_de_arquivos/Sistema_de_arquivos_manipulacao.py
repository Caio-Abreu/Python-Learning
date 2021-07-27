# Descobrindo se um arquivo ou diretorio existe
import os
print(os.path.exists('Leitura_de_arquivos/texto.txt')) # True

# Renomeando arquivo
try:
    os.rename('Leitura_de_arquivos/x.txt','Leitura_de_arquivos/trocado.txt') # Pode ser trocado apenas uma vez o nome, depois ira dar erro
except:
    print('Arquivo com nome já trocado, escolha outro ou mude o nome')

# Deletar arquivo
try:
    os.remove('Leitura_de_arquivos/arquivo_a_ser_apagado.txt') # Remove o arquivo
except:
    print('Arquivo ja apagado')