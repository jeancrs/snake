#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from universe import *

'''==========================================================================================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_BACKGROUND = pg.image.load('img/back.jpg')
except:
    IMG_BACKGROUND = pg.Surface((100, 100), pg.SRCALPHA)
    print("ERRO: As imagens não foram encontradas.")

PAREDE_ESQUERDA = -5
PAREDE_DIREITA = 585
PAREDE_CIMA = -1
PAREDE_BAIXO = 385

