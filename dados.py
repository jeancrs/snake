from constantes import *

'''==================='''
'''# Definições de dados: '''

from namedlist import namedlist

Cobra = namedlist("Cobra", "x, dx, y, dy, comprimento, corpo, bloco")

'''
Cobra pode ser criada como: Cobra(Int [LARGURA / 2, 5, ALTURA / 2, 0, 1, [], 20] Int)
interp.: representa a posição x, y, dx, dy, comprimento, corpo, e o tamanho do quadrado da cobra.
Exemplos:
'''
COBRA_INICIAL = Cobra(LARGURA / 2, 5, ALTURA / 2, 0, 1, [], 20)
COBRA_FIM = Cobra(PAREDE_DIREITA, 5, ALTURA / 2, 0, 1, [], 20)
''''
Template para função que recebe Cobra:
def fn_para_cobra(cobra):
    if cobra.x < PAREDE_ESQUERDA or cobra.x > PAREDE_DIREITA or cobra.y < PAREDE_CIMA or cobra.y > PAREDE_BAIXO:
        return "Erro: Cobra Inválida"

'''
Maca = namedlist("Maca", "x, y, bloco")
'''
Maça pode ser criada como: Maca(Int [500, 190, 30] Int)
interp.: representa a posicao x e y da maça, e tamanho da maça.
Exemplos:
'''
MACA_INICIAL = Maca(500, 190, 30)

''''
Template para funções que recebem Maca:
def fn_para_maca(maca):
   if maca.x < PAREDE_ESQUERDA or maca.x > PAREDE_DIREITA or maca.y < PAREDE_CIMA or maca.y > PAREDE_BAIXO:
        return "Erro: Maça Inválida."

'''
Maca2 = namedlist("Maca2", "x, y, bloco")
'''
Maça2 pode ser criada como: Maca2(Int [LARGURA/3, ALTURA/3, 20], Int)
interp.: representa a posicao x e y da maça2, e tamanho da maça2.
Exemplos:
'''
MACA2_INICIAL = Maca2(100, 200, 30)

''''
Template para funções que recebem Maca2:
def fn_para_maca2(maca2):
   if maca2.x < PAREDE_ESQUERDA or maca2.x > PAREDE_DIREITA or maca2.y < PAREDE_CIMA or maca2.y > PAREDE_BAIXO:
        return "Erro: Maça Inválida."

'''
Jogo = namedlist("Jogo", "cobra, maca, maca2, game_over, pontos")

''' Jogo é criado como: Jogo(cobra, maca, maca2, Boolean, pontos)
interp. Um jogo é composto por uma cobra, maça, maça2, pontos
e uma flag (game_over) que indica se o jogo está acontecendo
ou não.
Exemplos:
'''

JOGO_INICIAL = Jogo(COBRA_INICIAL, MACA_INICIAL, MACA2_INICIAL, False, 0)
JOGO_GAME_OVER = Jogo(Cobra(PAREDE_ESQUERDA, 1, 10, 5, 1, [], 20), MACA_INICIAL, MACA2_INICIAL, True, 0)

'''Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.cobra
        jogo.maca
        jogo.maca2
        jogo.game_over
        jogo.pontos
'''
