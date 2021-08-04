import math

def circunferencia(raio):
    # def circunferencia(raio: float) -> float:
    # type: (float) -> float
    # Porem nao podemos usar os dois ou um ou outro
    return 2 * math.pi * raio

print(circunferencia(8))

def cabecalho(texto,alinhamento= True):
    # type: (str, bool) -> str
    if alinhamento:
        return f"{texto.title()} \n {'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50,'#')
# cabecalho(texto=43,alinhamento='geek')

def cabecalho2(
        texto, #type: str
        alinhamento = True # type: bool
): #type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'
cabecalho2(texto='42',alinhamento=False)