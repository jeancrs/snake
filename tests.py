import unittest
from funcoes import *


class MeusTestes(unittest.TestCase):
    def testMover_cobra(self):
        self.assertEqual(mover_cobra(Cobra(
