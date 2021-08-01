# POO - Metodos Magicos
# São todos os metodos que utilizam dunder __
# dunder init -> __init__()
# Dunder > Double Underscore
# dunder repr -> Representação do objeto

class Livro:
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memoria')
    
    def __add__(self,outro):
        return f'{self} - {outro}'

    def __mul__(self,outro):
        if isinstance(outro,int):
            msg= ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        else:
            return 'Nao consigo multiplicar'

livro1 = Livro('python rocks!','Geek university',400)
livro2 = Livro('inteligencia artificial com python','Geek university',500)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro2 * 3)
print(livro2 * '3')