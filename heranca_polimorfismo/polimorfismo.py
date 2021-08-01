# POO - Polimorfismo

# Poli -> Muitos
# Morfis -> Formas

# Quando a gente reimplementa um metodo presente na classe do pai em classes filhas, estamos realizando um OverRiding
class Animal(object):
    def __init__(self,nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este metodo')

    def comer(self):
        print(f'{self.__nome} esta comendo')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala au au'

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        return f'{self._Animal__nome} fala miau miau'

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo')

# Teste

felix = Gato('Felix')
felix.comer()
felix.falar()


pluto = Cachorro('Pluto')
pluto.falar()
pluto.comer()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()