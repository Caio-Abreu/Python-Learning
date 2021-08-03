# por que testar nosso codigo ?

# TDD - Test Driven Development (Desenvolvimento  guiado por testes)

# Com TDD é utilizado estagios de desenvolvimento 
# - Voce escreve seu teste primeiro;
# - Entao voce escreve o codigo minimo suficiente para fazer o teste passar (ou seja, executar com sucesso); 
# - Entao refatora o codigo para realizar a funcionalidade e testa novamente; 
# - Uma vez que o teste passe, o recurso é considerado completo;

# Estes estagios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
# - Red;
# - Green;
# - Refactor;

class Gato:
    def __init__(self,nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    def miar(self):
        print(f'{self.__nome} esta miando....')

felix = Gato('felix')
felix.miar()
print(felix.nome)