import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferencia.__annotations__)

nome: str = 'Caio abreu'
peso: float = 67.9
ativo: bool = True
print(__annotations__)