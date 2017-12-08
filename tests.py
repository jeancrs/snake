import unittest
from funcoes import *


class MeusTestes(unittest.TestCase):
    def testMover_cobra(self):
        # Cobra se movendo para frente sem bater na parede.
        self.assertEqual(mover_cobra(Cobra(305, 5, 200, 0, 1, [], 20)), Cobra(310, 5, 200, 0, 1, [], 20))
        self.assertEqual(mover_cobra(Cobra(205, 5, 200, 0, 1, [], 20)), Cobra(210, 5, 200, 0, 1, [], 20))

        # Cobra andando para tras sem bater na parede
        self.assertEqual(mover_cobra(Cobra(205, -5, 200, 0, 1, [], 20)), Cobra(205 - 5, -5, 200, 0, 1, [], 20))

    def testTrata_tecla(self):
        self.assertEqual(trata_tecla_cobra(Cobra(50, 5, 200, 0, 1, [], 20), pg.K_LEFT),
                         Cobra(50, -5, 200, 0, 1, [], 20))
        self.assertEqual(trata_tecla_cobra(Cobra(50, 5, 200, 0, 1, [], 20), pg.K_RIGHT),
                         Cobra(50, 5, 200, 0, 1, [], 20))
        self.assertEqual(trata_tecla_cobra(Cobra(50, 0, 200, 5, 1, [], 20), pg.K_UP), Cobra(50, 0, 200, -5, 1, [], 20))
        self.assertEqual(trata_tecla_cobra(Cobra(50, 0, 200, -5, 1, [], 20), pg.K_DOWN),
                         Cobra(50, 0, 200, 5, 1, [], 20))

    def testMover_jogo(self):
        self.assertEqual(mover_jogo(
            Jogo(cobra=Cobra(100, 5, 200, 0, 1, [], 20),
                 maca=Maca(500, 190, 30),
                 maca2=Maca2(100, 200, 30),
                 game_over=False,
                 pontos=0)),
            Jogo(cobra=Cobra(100 + 5, 5, 200, 0, 1, [105, 200], 20),
                 maca=Maca(500, 190, 30),
                 maca2=Maca2(100, 200, 30),
                 game_over=False,
                 pontos=0))

        self.assertEqual(mover_jogo(
            Jogo(cobra=Cobra(100, 5, 200, 0, 1, [], 20),
                 maca=Maca(500, 190, 30),
                 maca2=Maca2(100, 200, 30),
                 game_over=False)),
            Jogo(cobra=Cobra(100 + 5, 5, 200, 0, 1, [], 20),
                 maca=Maca(500, 190, 30),
                 maca2=Maca2(100, 200, 30),
                 game_over=True,
                 pontos=0))


unittest.main()
