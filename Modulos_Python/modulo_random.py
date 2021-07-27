# Modulo nada mais é do que outros arquivos Python
# Modulo random -> possui varias funções para geração de numeros pseudo-aleatorio.

# OBS: exisstem duas formas de se utilizar um modulo ou função deste

# Forma 1 - importando todo o modulo

import random

# Ao realizar o import de todo o modulo,todas as funções, atributos,classes e propriedades que estiverem dentro do modulo ficarao disponiveis
# random() -> gera um numero aleatorio entre 0 e 1
print(random.random())

# Nao confundir a função random() com o pacote random

# Forma 2 - importando uma função especifica do modulo

from random import choice, random, shuffle
# Estamos pegando apenas a função random() no modulo random agora

for i in range(10):
    print(random())

# uniform() -> Gerar um numero pseudo-aleatorio entre os valores estabelecidos
from random import uniform

for i in range(10):
    print(uniform(3,7))

# randint() -> Gera valores inteiros aleatorios entre os valores estabelecidos
from random import randint
# Gerador de apostas para a mega sena
for i in range(10):
    print(randint(1,61),end=', ')

# choice() -> Mostra um valor aleatorio entre um interavel
print('\n')
jogadas = ['pedra','papel','tesoura']
print(choice(jogadas))

# shuffle() -> função de embaralhar dados

cartas = ['k','j','a','2','3','4','5','6','7']
print(cartas)
shuffle(cartas)
print(cartas)
print(cartas.pop())
