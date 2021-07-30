# POO - Objetos

# Objetos -> são instancias da classe. Ou seja, apos o mapeamento do objeto do mundo real para sua representação computacional, devemos
# poder criar quantos objetos forem necessarios. Podemos pensar nos objetos/instancias de uma classe como variaveis do tipo definido na
# classe

class Lampada:
    def __init__(self,voltagem,cor,luminosidade):
        self.__voltagem = voltagem 
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False
    def checa_lampada(self):
        return self.__ligada
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
    def diz(self):
        print(f'O cliente {self.__nome} diz oi')

class ContaCorrente:
    contador = 4999
    def __init__(self,limite,saldo,cliente):
        self.__numero = (ContaCorrente.contador + 1)
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero
    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.email = email
        self.senha = senha

# Instancias/Objeto
lamp1 = Lampada('branca',110,60)
lamp1.ligar_desligar()
lamp1.ligar_desligar()

print(f'A lampada esta ligada? {lamp1.checa_lampada()}')

user1 = Usuario('caio','abreu','caio96@gmail.com','123456')

cliente = Cliente('Caio abreu','123.456.432-8')
cc = ContaCorrente(5000,10000,cliente)

cc.mostra_cliente()
cliente.diz()