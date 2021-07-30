# POO - Metodos

# - Metodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema
# Em Python dividimos os meetodos, em 2 grupos:
# - Metodos de instancia
# - Metodos de classe

# Metodos de instancia

# O metodo dunder init __init__ é um metodo especial chamado de construtor ee sua função é contruir o objeto a partir da classe

# OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado dee dunder (Double Underline)
# Os metodos/funções dunder em Python são chamadas de metodos magicos
class Lampada:
    def __init__(self,voltagem,cor,luminosidade):
        self.__voltagem = voltagem 
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:
    contador = 4999
    def __init__(self,limite,saldo):
        self.__numero = (ContaCorrente.contador + 1)
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    contador = 0
    def __init__(self,nome,descricao,valor):
        self.__id = Produto.contador +1
        self.__nome = nome 
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    def desconto(self,porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor*(100-porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

# class Usuario:
#     def __init__(self,nome,sobrenome,email,senha):
#         self.__nome = nome 
#         self.__sobrenome = sobrenome 
#         self.__email = email
#         self.__senha = cryp.hash(senha, rounds=20000,salt_size=16)
#     # def __correr__(self, metros):
#     #     print(f'{self.__nome} esta correndo {metros}') Nunca criar funções com dunder por poder foder com o codigo e Python pensar que é outra coisa
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'
#     def checa_senha(self,senha):
#         if cryp.verify(senha, self.__senha):
#             return True
#         return False


# p1 = Produto('Ps4','video game',2300)
# print(p1.desconto(50))
# print(Produto.desconto(p1,50))

# user1 = Usuario('caio','abreu','123@gmail.com','1234')
# user2 = Usuario('bruno','abreu','123@gmail.com','4321')

# print(user1.nome_completo())
# print(user2.nome_completo())

# nome = input('Informe o nome:')
# sobrenome = input('Informe o sobrenome:')
# email = input('Informe o email:')
# senha = input('Informe a senha:')
# confirma_senha = input('Confirme a senha:')
# if senha == confirma_senha:
#     user5 = Usuario(nome,sobrenome,email,senha)
# else:
#     print('Senha nao confere...')
#     exit(1)
# print('Usuario criado com sucesso !!!')

# senha = input('Informe a senha para acesso: ')
# if user5.checa_senha(senha):
#     print('Acesso permitido')
# else:
#     print('Acesso negado')

# Metodos de Classe

class Usuario:
    contador = 0
    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuarios no sistema')
    
    @classmethod
    def ver(cls):
        print('teste')
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome 
        self.__sobrenome = sobrenome 
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000,salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    def checa_senha(self,senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    def __gera_usuario(self):
        return self.__email.split('@')[0]

user = Usuario('caio','abreu','caio96@gmail.com','123456')

Usuario.conta_usuarios() 
# Metodos de classe em Python são conhecidos como metodos estaticos em outras linguagens

# Metodo estatico

print(Usuario.contador)
print(Usuario.definicao())
