# try: execução problematica
# except: o que deve ser feito em caso de problema

# Ex:
try:
    geek() # erro
except:
    print('Deu merda') # Tente executar geek() caso dê problema imprima a mensagem de erro descrita

# Tratando um erro especifico

try:
    # geek()
    len(5)
# except NameError:
except TypeError as err:
    print(f'A aplicação gerou o erro: {err}')

try:
    len(5)
except NameError as erra:
    print(f'Deu NameErro: {erra}')
except TypeError as errb:
    print(f'Deu TypeErro: {errb}')
except:
    print('Deu um erro diferente')

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return "KeyError"
    except TypeError:
        return "TypeError"

dic = {"Nome":"Geek"}

print(pega_valor(dic,"a"))
