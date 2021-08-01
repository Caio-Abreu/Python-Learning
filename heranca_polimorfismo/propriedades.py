# POO - propriedades - properties


# Getters and setters igual ao java, para pegar atributo ou mudar o atributo
# Sempre ter cuidado com os setters

# class Conta:
#     contador = 0

#     def __init__(self, titular, saldo, limite):
#         self.__numero = Conta.contador + 1
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#         Conta.contador += 1

#     def extrato(self):
#         return f'Saldo de {self.__saldo} cliente {self.__titular}'

#     def deposito(self,valor):
#         self.__saldo += valor

#     def sacar(self,valor):
#         self.__saldo -= valor

#     def transferir(self,valor,destino):
#         self.__saldo -= valor
#         destino.__saldo += valor

#     def get_numero(self):
#         return self.__numero
    
#     def get_titular(self):
#         return self.__titular
    
#     def get_saldo(self):
#         return self.__saldo
    
#     def get_limite(self):
#         return self.__limite
    

# conta1 = Conta('Caio',3000,5000)
# conta2 = Conta('Bruno',2000,4000)

# print(conta1.extrato())
# print(conta2.extrato())

# soma = conta1.get_saldo() + conta2.get_saldo()
# print(f'A soma é {soma}')

# print(conta1.__dict__)

# Em Python utilizamos algo muito melhor do que os getters and setters do java
# Utilizando propriedade
class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # Getters se necessario
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # Utiliza como setter se necessario
    @limite.setter
    def limite(self,novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} cliente {self.__titular}'

    def deposito(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    

conta1 = Conta('Caio',3000,5000)
conta2 = Conta('Bruno',2000,4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma é {soma}')

print(conta2.__dict__)
print(conta1.__dict__)
conta1.limite = 7222
print(conta1.__dict__)

print(conta1.valor_total)
print(conta2.valor_total)