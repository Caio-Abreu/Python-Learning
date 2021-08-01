# POO - Herança (inheritance)

# A ideia de herança é a de reaproveitar codigo.Tambem extender nossas classes

# OBS com a herança, a partir de uma classe existente, nos extendemos outra classe que passa a herdar atributos e metodos de classe herdada

# Sem herança
# (----------------------------------------------------------------------)

# class Cliente:
#     def __init__(self,nome,sobrenome,cpf,renda):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__renda = renda

#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'

# class Funcionario:
#     def __init__(self,nome,sobrenome,cpf,matricula):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__matricula = matricula
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'

# cliente1 = Cliente('Caio','abreu','123.455.677-9',5000)
# funcionario1 = Funcionario('bruno','abreu','992.312.321-9',1234)

# print(cliente1.nome_completo())
# print(funcionario1.nome_completo())

# (----------------------------------------------------------------------)

# Utilizando super()
# (----------------------------------------------------------------------)

# variveis se repetindo nas duas classes,como melhorar isso
# Refatorando:

# class Pessoa:
#     def __init__(self,nome,sobrenome,cpf):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'


# class Cliente(Pessoa):
#     """Cliente herda de pessoa"""
#     def __init__(self,nome,sobrenome,cpf,renda):
#         super().__init__(nome,sobrenome,cpf)
#         self.__renda = renda

# class Funcionario(Pessoa):
#     """Funcionario herda de pessoa"""
#     def __init__(self,nome,sobrenome,cpf,matricula):
#         super().__init__(nome,sobrenome,cpf)
#         self.__matricula = matricula

# OBS: Quando uma classe herda de outra classe, ela herda todos os atributos e metodos da classe herdada

# cliente1 = Cliente('Caio','abreu','123.455.677-9',5000)
# funcionario1 = Funcionario('bruno','abreu','992.312.321-9',1234)

# print(cliente1.nome_completo())
# print(funcionario1.nome_completo())
# print(funcionario1.__dict__)
# print(cliente1.__dict__)

# (----------------------------------------------------------------------)

# Sobreescrevendo metodos(funções)
# (----------------------------------------------------------------------)

# Sobrescrita de metodos(funções) é chamado de OverRiding
# Sobrescrita de metodo ocorre quando reescrevemos um metodo presente na super classe em classes filhas

class Pessoa:
    def __init__(self,nome,sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    def get_nome(self):
        return self.__nome


class Cliente(Pessoa):
    """Cliente herda de pessoa"""
    def __init__(self,nome,sobrenome,cpf,renda):
        super().__init__(nome,sobrenome,cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""
    def __init__(self,nome,sobrenome,cpf,matricula):
        super().__init__(nome,sobrenome,cpf)
        self.__matricula = matricula
    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionario: {self.__matricula} Nome: {super().get_nome()}'


cliente1 = Cliente('Caio','abreu','123.455.677-9',5000)
funcionario1 = Funcionario('bruno','abreu','992.312.321-9',1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print(funcionario1.__dict__)
print(cliente1.__dict__)
