# Exemplos 
# def soma_todos_numeros(num1,num2,num3):
#     return num1 + num2 + num3

# Entendendo o args

def soma_todos_numeros(*args):
    return sum(args) # Apenas para numeros inteiros e reais

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1,2))
print(soma_todos_numeros(1,2,3))
print(soma_todos_numeros(1,2,3,4))

numeros = [1,2,3,4,5,6,7]
# Desemcopacotador
print(soma_todos_numeros(*numeros))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem é você....'

print(verifica_info())
print(verifica_info(1,True,'University','Geek'))
print(verifica_info(1,'University',3.145))

