# Bloco with abre e fecha o arquivo automaticamente para você

with open('Leitura_de_arquivos/texto.txt') as arquivo:
    letras = arquivo.readlines()
    for i,letra in enumerate(letras):
        print(letra)

    

