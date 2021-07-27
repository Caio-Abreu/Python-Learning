# Modulos integrados que já vem instalados no python

# Utilizando alias(apelidos) para modulos/funções
import random as rdm
print(rdm.random())

# Podemos utilizar o * para importar todas as funções de um modulo
from random import *
print(random())

# Importando todo o modulo
import random
print(random.random())

from random import randint as rdi,random as rdm
print(rdi(1,5))
print(rdm())

# Costumamos utilizar tuple para colocar multiplos imports de um mesmo modulo
from random import (random, 
    randint,
    shuffle,
    choice,
    uniform)

print(random())
print(randint(2,10))
print(shuffle(['Caio']))
print(choice(['Caio','pedra']))