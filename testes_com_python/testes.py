import unittest

from atividades import comer,dormir,eh_engracada

class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudavel"""
        self.assertEqual(comer('quiabo',True),
        'Estou comendo quiabo porque quero manter a forma'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza',eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez'
        )
    
    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado apos dormir por 4 horas'
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Putz dormi muito, estou atrasado para o trabalho'
        )
    def test_eh_engracada(self):
        # self.assertEqual(eh_engracada('sergio malandro'),False)
        # self.assertFalse(eh_engracada('sergio malandro'))
        self.assertTrue(eh_engracada('jim carrey'),'Jim carrey deveria ser engraçado')

if __name__ == '__main__':
    unittest.main()