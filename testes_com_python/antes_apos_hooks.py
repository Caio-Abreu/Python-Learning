# Unittest - Antes e apos hooks

# hooks - são testes em si. Ou seja, a execução dos testes

# setup() -> é executado antes de cada metodo de teste. É util para criarmos instancias de objetos e outros dados:
# tearDown() -> é executado ao final de cada metodo de teste. É util para excluir dados ou fechar conexoes com bancos de dados

import unittest

class ModuloTest(unittest.TestCase):
    def setUp(self):
        # Config do setUp()
        return super().setUp()
        pass
    
    def test_primeiro(self):
        # setUp vai rodar antes dos testes
        # tearDown() vai rodar apos o teste
        pass
    
    def test_segundo(self):
        # setUp vai rodar antes dos testes
        # tearDown() vai rodar apos o teste
        pass

    def tearDown(self) -> None:
        # Config do tearDown()
        return super().tearDown()
        pass