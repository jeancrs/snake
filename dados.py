from constantes import *

'''==================='''
'''# Definições de dados: '''


from namedlist import namedlist
Cobra = namedlist("Cobra", "x, dx, y, dy,comprimento,corpo,bloco")
'''
Cobra pode ser criada como: Cobra(Int[LARGURA/2, ALTURA/2,1,10,1,[],20, Int)
interp.: representa a posição x, y, dx, dy, comprimento, corpo, e o tamanho do quadrado da cobra.
Exemplos:
'''
cobra_inicial = Cobra(LARGURA/2, 5,ALTURA/2,0,1,[],20)
''''
Template para função que recebe Cobra:
def fn_para_cobra(c):
    if cobra.x colidir com  as paredes:
        return "Fim de Jogo"

'''
Maca = namedlist("Maca", "x, y,blocom")
'''
Maça pode ser criada como: Maca(Int[LARGURA/3, ALTURA/3,20], Int)
interp.: representa a posicao x e y da maça, e tamanho da maça.
Exemplos:
'''
maca_inicial = Maca(500, 190,30)

''''
Template para funções que recebem Maca:
def fn_para_maca(m):
    if maca.x <0 or maca.x > LARGURA:
        return "Erro: Maça Inválida"

'''

Jogo = namedlist("Jogo","cobra,maca,game_over,pontos")

''' Jogo é criado como: Jogo(cobra, maca, Boolean,pontos)
interp. Um jogo é composto por uma cobra, maça, pontos
e uma flag (game_over) que indica se o jogo está acontecendo
ou não.
Exemplos:
'''

JOGO_INICIAL = Jogo(cobra_inicial,maca_inicial,False,0)
JOGO_GAME_OVER= Jogo(Cobra(PAREDE_ESQUERDA,1,10,5,1,[],20),maca_inicial,True,0)

'''Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.cobra
        jogo.maca
        jogo.game_over
'''
