# POO - atributos
# Atributos -> representam as caracteristicas do objeto.Ou seja, pelos atributos
# nos conseguimos representar computacionalmente os estados de um objeto

# Em python dividimos os atributos em 3 grupos:
# - Atributos de instancia
# - Atributos de classe
# - Atributos de dinamicos


# Atributos de instancia
# Metodo construtor: É um metodo especial utilizado para a construção do objeto


# Em python por convenção, ficou estabelecido que, todo atributo de uma classe é publico, ou seja, pode ser acessado em todo o projeto
# Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da propria
# classe ondee esta declarado, utiliza-se __ duplo underscore no inicio de seu nome
# Isso é conhecido como Name Mangling.

class Lampada:
    def __init__(self,voltagem,cor):
        self.voltagem = voltagem 
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self,numero,limite,saldo):
        self.numero = numero 
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self,nome,descricao,valor):
        self.nome = nome 
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome 
        self.email = email
        self.senha = senha

ps4 = Produto('Play','video game',4000)

# Atributos publicos ou privados
class Acesso:
    def __init__(self,email,senha):
        self.email = email
        self.__senha = senha
    def mostra_senha(self):
        print(self.__senha)
    def mostra_email(self):
        print(self.email)

# OBS: lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos atributos sinalizados 
# como privados fora da classe

# Exemplo
user = Acesso('user@gmail.com','123456')
print(user.email)
# print(user.__senha) # AtributeError

print(user._Acesso__senha)  # Temos acesso. Mas nao deveriamos fazer este acesso (Name Mangling)
user.mostra_email()
user.mostra_senha()

# O que significa atributo de instancia ?
# Significa que ao criarmos instancia de uma classe, todas as instancias terão estes atributos

user1 = Acesso('user1@gmail.com','123456')
user2 = Acesso('user2@gmail.com','654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de classe

# Atributos de classe, são atributos, que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente ja inicializamos um valor
# e este valor é compartilhado entre todas as instancias da classe. Ou seja, ao inves de cada instancia da classe ter seus proprios valores como
# é o caso dos atributos de instancia, com os atributos de classe todas as instancias terão o mesmo valor para este atributo.

class Produto:
    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0
    def __init__(self,nome,descricao,valor):
        self.id = Produto.contador + 1
        self.nome = nome 
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Playstation 4','video game', 4000)
p2 = Produto('Xbox s','video game', 4500)

print(p1.valor) # Acesso possivel, mas incorreto de um atributo de classe
print(p2.valor) # Acesso possivel, mas incorreto de um atributo de classe

# OBS nao precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id) # 1
print(p2.id) # 2

# Atributos dinamicos -> Um atributo dee instancia que pode ser criado em tempo de execução 

# OBS o atributo dinamico sera exclusivo da instancia que o criou 

p1 = Produto('Playstation 4','Video Game', 2300)

p2 = Produto('Arroz','Mercearia',5.99)

# Criando um atributo dinamico em tempo de execução

p2.peso = '5kg' # Note que na classe Produto nao existe o atributo peso
p1.peso = '10kg'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor {p2.valor}, Peso: {p2.peso}')
print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor {p1.valor}, Peso: {p1.peso}')

# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)

del p2.peso
del p2.valor

print(p2.__dict__)