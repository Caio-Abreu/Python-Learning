# Diferente do *args que coloca os valores extras em uma dupla, ele exige que utilizemos parametros nomeados, e transforma em um dicionario

# Exemplo
def cores_favoritas(**kwargs):
    for pessoas, cor in kwargs.items():
        print(f'A cor favorita de {pessoas.title()} é {cor}')

cores_favoritas(marcos='verde',julia='amarelo',fernanda='azul',vanessa='branco')

# Os parametros *args e **kwars nao sao obrigatorios
cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] =='Python':
        return 'Voce recebeu um cumprimento pythonico geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Nao tenho certeza quem voce é....'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))

# Nas nossas funções, podemos ter (Nesta ordem)
# Parametros obrigatorios
# *args
# Parametros default (nao obrigatorio)
# **kwargs


def minha_funcao(idades,nome,*args,solteiro=False,**kwargs):
    print(f'{nome} tem {idades} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8,'Julia')
minha_funcao(8,'Ana',4,5,6,7,solteiro=True)
minha_funcao(8,'Felipe',eu= 'Nao',voce='Vai')
minha_funcao(8,'Luiz',4,5,6,7,python=True,java=False)

# Mas porque é importante manter a ordem dos parametros na declaração

# Ordem correta dos parametros !!!!!
def mostra_info(a,b,*args,instrutor='Geek',**kwargs):
    return [a,b,args,instrutor,kwargs]

# Errado !!!
# def mostra_info(a,b,instrutor='Geek',*args,**kwargs):
#     return [a,b,args,instrutor,kwargs]

print(mostra_info(1,2,3,sobrenome='University',cargo='Instrutor'))

# Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome':'Felicity','sobrenome':'Jones'}
# print(mostra_nomes(nomes)) Erro !!!!
print(mostra_nomes(**nomes)) # Correto !!!

def soma_multiplos_numeros(a,b,c,**kwargs):
    print(a+b+c)

lista=[1,2,3]
tupla=(1,2,3)
conjunto={1,2,3}
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1,b=2,c=3)
soma_multiplos_numeros(**dicionario) # Com dicionario é necessario dois '*'
# dicionario = dict(f=1,s=2,n=3) Ira dar erro !!!! Precisa ser igual aos parametros

soma_multiplos_numeros(**dicionario,lang = 'Python')