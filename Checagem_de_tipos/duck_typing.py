# Objetos similares terão metodos similares

class CisneNegro:
    def __len__(self):
        return 42

livro = CisneNegro()
nome = 'Geek university'
lista = [12,34,55,48]
dicio = {'carlos':12,'vanessa':34,'joana':48}

print(len(livro))
print(len(nome))
print(len(lista))
print(len(dicio))