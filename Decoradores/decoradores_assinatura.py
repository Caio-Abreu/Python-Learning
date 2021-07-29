# Decorators com diferentes assinaturas

# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola eu sou o {nome}'

@gritar
def ordenar(principal,acompanhamento):
    return f'Ola eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

# Teste
print(saudacao('Anelina'))
print('\n')
# print(ordenar('Picanha','Batata Frita')) Ele esperar receber 1 parametro e estamos enviando 2, logo TypeError

# Para resolvermos utilizamos um padrão chamado decorator pattern

def gritar(funcao):
    def aumentar(*args,**kwargs):
        return funcao(*args,**kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola eu sou o {nome}'

@gritar
def ordenar(principal,acompanhamento):
    return f'Ola eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'
# Teste 
print(saudacao('Anelina'))

print('\n')

print(ordenar('Picanha','Batata Frita'))

# A assinatura de uma função é representada pelo seu retorno, nome e parametro de entrada

@gritar
def lol():
    return 'lol'
print(lol())

# OBS vale lembrar que podemos utilizar parametros nomeados
print(ordenar(acompanhamento='Batata frita', principal='Picanha'))

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! primeiro argumento precisa ser {valor}'
            return funcao(*args,**kwargs)
        return outra
    return interna
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1,num2):
    return num1 + num2

# Teste
print(soma_dez(10,12)) #22
print(soma_dez(1,12)) #22

print(comida_favorita('pizza','churrasco'))
print(comida_favorita('sanduiche','churrasco'))