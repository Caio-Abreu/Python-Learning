# POO MRO - method resolution order

# Method resolution order (Resolução de ordem de metodo), é a ordem de execução dos metodos (quem sera executado primeiro).

# Em Python a gente pode conferir a ordem de execução dos metodos (MRO) de 3 formas:
# - Via propriedade da classe __mro__
# - Via metodo mro()
# - Via help
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
tux = Pinguim('tux')
print(tux.cumprimentar())