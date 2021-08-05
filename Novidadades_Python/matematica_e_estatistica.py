import math

# math.prod - retorna o produto de um container numerico
num_v1 =[4,6,1,8]
num_v2 =(4,6,1,8)
num_v3 ={4,6,1,8}

print(math.prod(num_v1))
print(math.prod(num_v2))
print(math.prod(num_v3))

print('-----------------------------------------------------------------------')
# math.isqrt - retorna a parte inteira da raiz quadrada de um numero

print(math.sqrt(9))
print(math.isqrt(9))

print(math.sqrt(17))
print(math.isqrt(17))

print('-----------------------------------------------------------------------')
# math.dist - retorna a distancia euclidiana entre dois pontos, 3D ou 2D

# Pontos 3D
p3d1 = (12,50,40)
p3d2 = (6,7,13)

# Pontos 2D

p2d1 = [12,50]
p2d2 = [6,7]

print(math.dist(p3d1,p3d2))
print(math.dist(p2d1,p2d2))

print('-----------------------------------------------------------------------')
# math.hypot - retorna a hipotenusa, ou norma Euclidiana

print(math.hypot(*p3d1))
print(math.hypot(*p3d2))

# Estatistica
import statistics

print('-----------------------------------------------------------------------')
# statistics.fmean - Calcula a média de numeros reais

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1,6,3,89]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

print('-----------------------------------------------------------------------')
# statistics.geometric_mean - calcula a media geometrica de numeros reais

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

print('-----------------------------------------------------------------------')
# statistics.multimode - retorna o valor mais frequente em uma sequencia

seq1 = 'Caio abreu'
seq2 = [3,5,3,8,7,9,5,3]
seq3 = [1,2,3,1,2,3,4,5,6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))