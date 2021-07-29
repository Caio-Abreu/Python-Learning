# Decoradores (Decorators)

# O que são decorators
# - Decoratorrs são funções
# - Decorators envolvem outras funções e aprimoram seus comportamentos 
# - Decorators tambem sao exemplos de higher order functions
# - Decorators tem uma sintaxe propria, usando "@" (Syntact sugar)


# Decorators como funções (sintaxe nao recomendada/Sem syntact sugar)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('tenha um otimo dia!')
    return sendo

def saudacao():
    print('Seja bem vindo a geek university')
# Teste 1

teste = seja_educado(saudacao)
teste()

print('-----------------------------------------------------')

# Teste 2 
def raiva():
    print('EU TE ODEIO')

raiva_educada = seja_educado(raiva)
raiva_educada()

print('-----------------------------------------------------')

# Decorators com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é pedro')

# Teste 1

apresentando()

print('-----------------------------------------------------')

# Teste 2
@seja_educado_mesmo
def dormir():
    print('Quero domir')

dormir()

# Nao confunda Decorator com Decorator function