# Todos os arquivos ja criados são modulos customizados utilizaveis
import sys
sys.path.append('./') # acessando a pasta functions para acessar a função soma_impares
from functions import funcoes_com_parametro
print('--------------------------------------------------')
print(funcoes_com_parametro.soma_impares([1,2,3,4,5,6,7,11]))

# from ..functions.funcoes_com_parametro import soma_impares
# print(soma_impares([1,2,3,4,5,6,7,8]))