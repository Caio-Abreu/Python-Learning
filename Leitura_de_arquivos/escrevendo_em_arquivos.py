# Exemplo de escrita

with open('Leitura_de_arquivos/novo.txt','w') as arquivo:
    arquivo.write('Escrever em arquivo é muito facil.\n')
    arquivo.write('Podemos colocar varias linhas.\n')
    arquivo.write('Esta é a ultima linha.\n')
# Se for criado dois arquivos com o mesmo nome o mais novo ira excluir o antigo assim perdendo todos os dados ja feitos

with open('Leitura_de_arquivos/geek.txt','w') as arquivo:
    arquivo.write('Geek\n' * 100)

frutas = ['abacate','morango','maça','abacaxi','manga'] # Alguns exemplos de frutas

with open('Leitura_de_arquivos/frutas.txt','w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        fruta = fruta.lower() # Ira colocar a palavra do usuario em minusculo para nao ter erro gramatical
        if fruta in frutas:
            arquivo.write(fruta)
            arquivo.write('\n')
        elif fruta == 'sair':
            break
        else:
            print('Fruta invalida')
          
    