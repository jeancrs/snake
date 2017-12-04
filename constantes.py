#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random,time
from universe import *

''' Jogo da Cobrinha '''

'''==========================================================================================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))
try:
    IMG_BACKGROUND = pg.image.load('img/back.jpg')
except:
    IMG_BACKGROUND = pg.Surface((100, 100), pg.SRCALPHA)
    print("ERRO: Imagens nao foram carregadas.")

PAREDE_ESQUERDA = -5
PAREDE_DIREITA = 585
PAREDE_CIMA = -1
PAREDE_BAIXO = 385

