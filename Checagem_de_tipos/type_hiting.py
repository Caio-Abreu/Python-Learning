# (nome:str), será o tipo de dado esperado pela função
# -> str, será o tipo de dado esperado pelo retorno da função

def cuprimentar(nome: str ) -> str:
    return f'Ola, {nome}'

# print(cuprimentar(1)) mas nao bloqueia outros tipos de dados
print(cuprimentar('Caio'))

def cabecalho(texto: str,alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()} \n {'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50,'#')


print(cabecalho('geek university'))
print(cabecalho('geek university',alinhamento=False))