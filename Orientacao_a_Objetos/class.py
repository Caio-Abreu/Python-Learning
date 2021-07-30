# POO - Classes

# Em POO, classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente
# Imagine que voce queira fazer um sistema para automatizar o controle das lampadas da sua casa

# Classes podem conter:
# - Atributos -> representam as caracteristicas do objeto, ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto
#   No caso da lampada, iriamos querer saber se a lampada é 110 ou 220 volts, se ela é branca,amarela, vermelha ou outra cor, qual é a luminosidade
#   dela e etc.

# - Metodos (funções) -> Representam os comportamentos do objeto.Ou seja, as ações que este objeto pode reealizar no seu sistema.No caso da lampada
#   por exemplo, um comportamento comum que muito provalvemente iriamos querer representar no nosso sistema é o de ligar e desligar 

# Em python para definir uma classe utilizamos "class"
# Utilizamos a palavra "pass" em Python quando temos um bloco de codigo que ainda nao esta implementado

# OBS: Quando nomeamos uma classe em Python utilizamos por convenção o nome com inicial em maiusculo. Se o nome for completo, utiliza-se as iniciais
# de ambas as palavras em maisculo, todas juntas.


class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass

class Int:
    pass


lamp = Lampada()
print(type(lamp))