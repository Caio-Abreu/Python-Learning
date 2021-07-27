# 1- Variaveis Globais
#     -São reconhecidas por todo o programa

# 2- Variaveis Locais
#     -São conhecidas apenas no bloco onde foram declaradas, limitada no bloco onde foi declarado 

# varivel global
numero = 42
# novo = 0
if numero > 10:
    # varivel local(novo)   
    novo = numero +10
    print(novo)
print(novo)