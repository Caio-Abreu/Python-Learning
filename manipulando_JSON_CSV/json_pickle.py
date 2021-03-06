# JSON e Pickle

# JSON -> JavaScript Object Notation
# API - São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube....) e terceiros (nós desenvolvemos)

import json
# ret = json.dumps(['produto',{'PlayStation 4':('2TB','Novo','220V',2340)}])
# print(type(ret))
# print(ret)

# class Gato():
#     def __init__(self, nome,raca):
#         self.__nome = nome
#         self.__raca = raca
#     @property
#     def nome(self):
#         return self.__nome
#     @property
#     def raca(self):
#         return self.__raca

# felix = Gato('felix','Vira-lata')
# print(felix.__dict__)
# ret = json.dumps(felix.__dict__)
# print(ret)

# Integrando JSON com o Pickle

import jsonpickle

# class Gato():
#     def __init__(self, nome,raca):
#         self.__nome = nome
#         self.__raca = raca
#     @property
#     def nome(self):
#         return self.__nome
#     @property
#     def raca(self):
#         return self.__raca

# felix = Gato('felix','Vira-lata')
# with open('manipulando_JSON_CSV/felix.json','w') as arquivo:
#     ret = jsonpickle.encode(felix)
#     arquivo.write(ret)

# Lendo arquivo jsonpickle

class Gato():
    def __init__(self, nome,raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca

felix = Gato('felix','Vira-lata')
with open('manipulando_JSON_CSV/felix.json','r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)