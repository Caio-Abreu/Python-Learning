# Literal type
# Union
# Final
# Typed dictionaries
# Protocols
# -----------------------------------------------------------------------------------------------------------------

# Literal type
from os import R_OK
from typing import Literal, Union

def pegar_status(usuario: str) -> Literal['conectado','desconectado']:
    pass

# def calcula_v1(operacao: str,num1: int,num2: int) -> None:
#     if operacao == '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif operacao == '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     else:
#         raise ValueError(f'Operação invalida {operacao!r}') # !r = coloca a variavel entre aspas
# calcula_v1('+',6,7)
# calcula_v1('-',10,2)
# calcula_v1('*',3,5)

# Se usar o mypy ele mostrara que tem erro, porem o codigo continua rodando 
def calcula_v2(operacao: Literal['+','-'],num1: int,num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação invalida {operacao!r}') # !r = coloca a variavel entre aspas
calcula_v2('+',6,7)
calcula_v2('-',10,2)
# calcula_v2('*',3,5)

# Union
from typing import Union

def soma(num1: int, num2:int) -> Union[str,int]: # Pode ser uma string ou um int o retorno
    resultado = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado

from typing import Final
NOME: Final = 'Caio'
print(NOME)

NOME = 'Abreu' #Avisa do erro mas roda do mesmo jeito
print(NOME)

from typing import final

@final
class Pessoa:
    pass

class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        print('Estou estudando....')

class Estagiario(Estudante):
    pass

    def estudar(Self): #Avisa que nao pode sobrescrever o metodo estudar de Estudante por causa de '@final', porem roda
        print('Estudando e estagiando')

# Typed Dictionaries
from typing import TypedDict

class CursoPython(TypedDict):
    versao:str
    atualizacao:int

geek = CursoPython(versao='3.8.5',atualizacao=2020)
print(geek)

# Funciona passando outros nomes, porem o mypy avisa que esta errado
outro = CursoPython(algo='vai',coisa=True)
print(outro)

# Protocols

from typing import Protocol

class Curso(Protocol):
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')

class Venda:
    titulo = 'Oi'

v1 = Venda()
# c1 = Curso
# c1.titulo = 'Curso de Python'
estudar(v1)
# estudar(c1)