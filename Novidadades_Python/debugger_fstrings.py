def multiplicar(num1: float, num2:float) -> float:
    return num1 * num2

resultado: float = multiplicar(4.2345,7.7890)

print(f'O resultado é {resultado}')
print(f'O resultado é {multiplicar(9,4):.2f}')

# Utilizando variavel walrus
print(f'{(media := 8/2)} é a metade de {media * 2}')

geek: str = 'Geek university'

print(f"geek = '{geek}'")
# Agora utilizando fstrings
print(f'{geek=}')
print(f'{geek.upper()[::-1] = }')