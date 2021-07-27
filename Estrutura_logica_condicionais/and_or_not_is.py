ativo = True
logado = False

if ativo and logado:
    print('Bem vindo usuario(And)')
elif ativo or logado:
    print('Bem vindo usuario(Or)')
else:
    print('Voce precisa ativar sua conta.\nPor favor, cheque seu email')

# Not inverte o valor do booleano, True vira False e False vira True
if not logado:
    print('Bem vindo usuario')
else:
    print('Voce precisa ativar sua conta.\nPor favor, cheque seu email')

# Is
print(ativo is False)
print(logado is False)
nome = 'Caio Abreu'
print(nome.isupper())
print(nome.istitle())