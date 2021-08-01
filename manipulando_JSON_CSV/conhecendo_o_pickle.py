# Conhecendo o Pickle
# A função do pickle é realizar o seguinte processo:
# Objeto Python -> Binarização
# Binarização -> Objeto Python

# Este processo é chamado de serielização/deserialização
# OBS: O modulo pickle nao é seguro contra dados maliciosos e desta forma nao é recomendado trabalhar com arquivos pickle vindos
# de outras pessoas que voce nao conheça ou de fontes desconhecidas

import pickle

class Animal:
    def __init__(self,nome):
        self.__nome = nome
    def comer(self):
        print(f'{self.__nome} esta comendo...')
    @property
    def nome(self):
        return self.__nome

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def mia(self):
        print(f'{super().nome} esta miando...')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def late(self):
        print(f'{super().nome} esta latindo...')

felix = Gato('Felix')
Pluto = Cachorro('Pluto')

# Escrita em arquivos pickle
# with open('manipulando_JSON_CSV/animais.pickle','wb') as arquivo:
#     pickle.dump((felix,Pluto), arquivo)

# Leitura de dados em arquivo picle
with open('manipulando_JSON_CSV/animais.pickle','rb') as arquivo:
    gato,cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
