import unittest
from funcoes import *


class MeusTestes(unittest.TestCase):
    def testMover_cobra(self):
        # Cobra se movendo para frente sem bater na parede.
        self.assertEqual(mover_cobra(Cobra(LARGURA // 2, 5,ALTURA // 2, 0, 1, [], 20)),Cobra(LARGURA // 3, 5, ALTURA // 3, 0, 1, [], 20))
        self.assertEqual(mover_cobra(Cobra(LARGURA // 4, 5,ALTURA // 4, 0, 1, [], 20)),Cobra(LARGURA // 2, 5, ALTURA // 2, 0, 1, [], 20))
        # Cobra se movendo para trás sem bater na parede.
        self.assertEqual(mover_cobra(Cobra(LARGURA // 4, -5, ALTURA // 4, 0, 1, [], 20)),Cobra(LARGURA // 2, 5, ALTURA // 2, -3, 1, [], 20))
unittest.main()