# POO - Herança multipla
# Possibilidade de uma classe herdar de multiplas classes

# OBS: A herança multipla pode ser feita de duas maneiras:
#  - Por multiderivação direta
#  - Por multiderivação indireta

# Exemplo 1 - Multiderivação direta

# class Base1:
#     pass

# class Base2:
#     pass

# class Base3:
#     pass

# class Multiderivada(Base1,Base2,Base3):
#     pass

# # Exemplo 2 - Multiderivação Indireta

# class Base1:
#     pass

# class Base2(Base1):
#     pass

# class Base3(Base2):
#     pass

# class Multiderivada(Base3):
#     pass

# OBS: Nao importa se a derivação é direta ou indireta. A classe que realizar a herança herdara todos os atributos e metodos das super classes

# Direta
class Animal:
    def __init__(self,nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def nadar(self):
        return f'{super().nome} esta nadando'
    
    def cumprimentar(self):
        return f'Eu sou {super().nome} do mar!'
    
class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def andar(self):
        return f'{super().nome} esta andando'
    def cumprimentar(self):
        return f'Eu sou {super().nome} da terra'

class Pinguim(Terrestre,Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico('wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('tux')
print(tux.nadar())
print(tux.andar())
print(tux.cumprimentar()) # Eu sou tux da terra! /Eu sou tux do mar ! ??? Method Resolution Order - MRO

# Objeto é instancia de....
print(f'Tux é instancia de pinguim ? {isinstance(tux,Pinguim)}')
print(f'Tux é instancia de pinguim ? {isinstance(tux,Aquatico)}')
print(f'Tux é instancia de pinguim ? {isinstance(tux,Terrestre)}')
print(f'Tux é instancia de pinguim ? {isinstance(tux,Animal)}')
print(f'Tux é instancia de pinguim ? {isinstance(tux,object)}')