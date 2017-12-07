#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import *

'''==========================================================================================='''
'''# Preparação da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_BACKGROUND = pg.image.load('img/back.jpg')
    IMG_MACA = pg.image.load('img/maca.png')
    IMG_MACA2 = pg.image.load('img/maca2.png')
except:
    IMG_BACKGROUND = pg.Surface((100, 100), pg.SRCALPHA)
    IMG_MACA = pg.Surface((100, 100), pg.SRCALPHA)
    IMG_MACA2 = pg.Surface((100, 100), pg.SRCALPHA)
    print("Erro: As imagens não foram encontradas.")

PAREDE_ESQUERDA = -5
PAREDE_DIREITA = 585

PAREDE_CIMA = -1
PAREDE_BAIXO = 385
