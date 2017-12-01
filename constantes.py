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
    print("IMAGEM NÃO CARREGADA!!!")

## CONSTANTES DE COBRA ##
verde = (0, 102, 51)
bloco = 20
comprimento = 1
corpo = []
## CONSTANTES DA MAÇA ##
vermelho = (255, 0, 0)
blocom = 30
x_maca = 300
y_maca = 300
## CONSTANTES GERAIS ##
preto = (0,0,0)
pontos = 0
PAREDE_ESQUERDA = -5
PAREDE_DIREITA = 585
PAREDE_CIMA = -1
PAREDE_BAIXO = 385
