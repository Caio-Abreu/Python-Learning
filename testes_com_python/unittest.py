# Introdução ao modulo unittest
# Unittest -> testes unitarios
# O que são testes unitarios
# Teste é a forma de se testar unidades individuais de codigo fonte.
# Unidades individuais podem ser: funções, metodos,classes,modulos, etc.

# OBS: teste unitario nao é especifico da linguagem Python

# Para criar nossos testes,criamos classes que herdam de unittest.TestCase e a partir de então ganhamos todos os 'assertions' presentes no modulo
# Para rodar os testes, utilizamos unittest.main()

# TestCase -> casos de teste para sua unidade

# Conhecendo as assertions
# Metodo                    Checa que
# assertEqual(a,b)          a == b
# assertNotEqual(a,b)       a != b
# assertTrue(x)             x é verdadeiro
# assertFalse(x)            x é falso
# assertIs(a,b)             a é b
# assertIsNot(a,b)          a nao é b
# assertIfNone(x)           x é None
# assertIsNotNone(x)        x nao é None
# assertIn(a,b)             a esta em b
# assertNotIn(a,b)          a nao esta em b
# assertIsInstance(a,b)     a é instancia de b
# assertNotIsInstance(a,b)  a nao é instancia de b

# Por convenção todos os testes em um tes case, devem ter seu nome iniciado com teste_
# Para executar os testes com unittest
# python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose
# python nome_do_modulo -v

# Docstring nos testes
# Podemos acrescentar docstring nos testes (recomendado)

# Pratica - utilizando a abordagem TDD