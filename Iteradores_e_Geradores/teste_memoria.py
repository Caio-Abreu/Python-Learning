# Teste de memoria com generators

# Sequencia de fibonacci
# 1,1,2,3,5,8,13...

# Função teste 1 usando lista 449MB com 100.000 numeros
def fib_lista(max):
    nums = []
    a,b = 0,1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

for n in fib_lista(100):
    print(n)


# Função teste 1 usando gerador(generator) 3MB com 100.000 numeros
def fib_gen(max):
    a,b,contador = 0,1,0
    while contador < max:
        a,b = b,a+b
        yield a
        contador += 1

for n in fib_gen(100):
    print(n)

# Diferença de 449MB para apenas 3MB usando gerador