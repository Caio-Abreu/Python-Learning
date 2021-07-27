# Funções sem nome/anonimas

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão Lambda
lambda x: 3*x+1

# Como utilizar
calc = lambda x: 3*x+1

print(calc(4))

# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))

# Em funções Python podemos ter nenhuma ou varias entradas.Em lambda tambem
amar = lambda: 'Como nao amar python ?'
uma = lambda x: 3*x+1
duas = lambda x,y: (x*y)**5
tres = lambda x,y,z: 3/(1/x+1/y+1/z)
 
print(amar())
print(uma(3))
print(duas(3,2))
print(tres(3,2,3))

autores = ['Ayla Helena', 'Maria Alice Júlia', 'Luna Aurora Laura Maya', 'Beatriz', 'Ana Rebeca' ,'Maitê Isis', 'Liz Hadassa', 'Mariana', 'Lara']
autores.sort(key=lambda sobrenome:sobrenome.split(' ')[-1].lower())
print(autores)

# Função quadratica
# f(x) = a *x **2 + b *x+c

# Definindo a função

def geradora_funcao_quadratica(a,b,c):
    """Retorna a função f(x) = a *x **2 + b *x+c"""
    return lambda x:a *x **2 + b *x+c

teste = geradora_funcao_quadratica(2,3,-5)

print(teste(0))
print(teste(1))
print(teste(2))