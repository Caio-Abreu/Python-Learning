# Dica de quando e onde tratar codigo:
# TODA ENTRADA DE DADO DEVE SER TRATADA

# else -> sera executado se não ocorrer o erro
# try:    
#     num = int(input('Informe um numero: '))
# except ValueError:
#     print('Valor incorreto')
# else:
#     print(f'Voce digitou {num}')

# ----------------------------------------------------------------------------

# finally
# try:    
#     num = int(input('Informe um numero: '))
# except ValueError:
#     print('Valor incorreto')
# else:
#     print(f'Voce digitou {num}')
# finally:
#     print('Executando o finally')
# O finally sempre sera executado, dando certo ou não a aplicação
# Utilizado para fechar ou desalocar recursos

# ----------------------------------------------------------------------------

# Exemplo mais complexo Errado

# def dividir(a,b):
#     return a/b

# num1 = int(input('Informe o primeiro numero'))

# try:
#     num2 = int(input('Informe o segundo numero'))
# except ValueError:
#     print('O valor precisa ser numerico')

# try:    
#     print(dividir(num1,num2))
# except NameError:
#     print('Valor incorreto')

# ----------------------------------------------------------------------------

# Exemplo mais complexo CERTO
# def dividir(a,b):
#     try:
#         return int(a)/int(b)
#     except ValueError:
#         return 'Valor incorreto'
#     except ZeroDivisionError:
#         return 'Nao é possivel realizar uma divisão por zero'

# num1 = input('Informe o primeiro numero ')
# num2 = input('Informe o segundo numero ')
# print(dividir(num1,num2))

# ----------------------------------------------------------------------------

# Exemplo Generico
# def dividir(a,b):
#     try:
#         return int(a)/int(b)
#     except:
#         return 'Ocorreu um problema'

# num1 = input('Informe o primeiro numero ')
# num2 = input('Informe o segundo numero ')
# print(dividir(num1,num2))

# ----------------------------------------------------------------------------

# Exemplo semi-generico
def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro numero ')
num2 = input('Informe o segundo numero ')
print(dividir(num1,num2))