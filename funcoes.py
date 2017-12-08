import random
from dados import *

'''===================='''
''' Funções: '''

'''
mover_cobra: Cobra -> Cobra
Produz a próxima cobra (ou seja, fazer ela andar).
'''


def mover_cobra(cobra):
    if cobra.x < PAREDE_ESQUERDA or cobra.x > PAREDE_DIREITA or cobra.y < PAREDE_CIMA or cobra.y > PAREDE_BAIXO:
        return "Erro: Cobra Inválida."
    else:
        cobra.x = cobra.x + cobra.dx
        cobra.y = cobra.y + cobra.dy

    if cobra.x > PAREDE_DIREITA:
        cobra.x = PAREDE_DIREITA
    elif cobra.x < PAREDE_ESQUERDA:
        cobra.x = PAREDE_ESQUERDA
    elif cobra.y < PAREDE_CIMA:
        cobra.y = PAREDE_CIMA
    elif cobra.y > PAREDE_BAIXO:
        cobra.y = PAREDE_BAIXO

    return cobra


'''
mover_maca: Maca -> Maca
Move a maça no eixo x e y.
'''


def mover_maca(maca):
    if maca.x < PAREDE_ESQUERDA or maca.x > PAREDE_DIREITA or maca.y < PAREDE_CIMA or maca.y > PAREDE_BAIXO:
        return "Erro: Maça Inválida."
    else:
        maca.x = round(random.randrange(0, LARGURA - maca.blocom))
        maca.y = round(random.randrange(0, ALTURA - maca.blocom))

    if maca.x > PAREDE_DIREITA:
        maca.x = PAREDE_DIREITA
    elif maca.x < PAREDE_ESQUERDA:
        maca.x = PAREDE_ESQUERDA
    elif maca.y < PAREDE_CIMA:
        maca.y = PAREDE_CIMA
    elif maca.y > PAREDE_BAIXO:
        maca.y = PAREDE_BAIXO
        
    return maca.x, maca.y


'''
mover_maca2: Maca2 -> Maca2
Move a maça no eixo x e y.
'''


def mover_maca2(maca2):
    if maca2.x < PAREDE_ESQUERDA or maca2.x > PAREDE_DIREITA or maca2.y < PAREDE_CIMA or maca2.y > PAREDE_BAIXO:
        return "Erro: Maça Inválida."
    else:
        maca2.x = round(random.randrange(0, LARGURA - maca2.blocom))
        maca2.y = round(random.randrange(0, ALTURA - maca2.blocom))

    if maca2.x > PAREDE_DIREITA:
        maca2.x = PAREDE_DIREITA
    elif maca2.x < PAREDE_ESQUERDA:
        maca2.x = PAREDE_ESQUERDA
    elif maca2.y < PAREDE_CIMA:
        maca2.y = PAREDE_CIMA
    elif maca2.y > PAREDE_BAIXO:
        maca2.y = PAREDE_BAIXO
        
    return maca2.x, maca2.y


'''
colidirem_cm: Cobra, Maca -> Boolean
Verifica se a cobra e a maça colidiram.
'''


def colidirem_cm(cobra, maca):
    if maca.x < cobra.x < maca.x + maca.blocom or maca.x < cobra.x + cobra.bloco < maca.x + maca.blocom:
        if maca.y < cobra.y < maca.y + maca.blocom:
            maca.x, maca.y = mover_maca(maca)
            return True
    else:
        return False
    
'''
colidirem_cm2: Cobra, Maca2 -> Boolean
Verifica se a cobra e a maça2 colidiram.
'''


def colidirem_cm2(cobra, maca2):
    if maca2.x < cobra.x < maca2.x + maca2.blocom or maca2.x < cobra.x + cobra.bloco < maca2.x + maca2.blocom:
        if maca2.y < cobra.y < maca2.y + maca2.blocom:
            maca2.x, maca2.y = mover_maca2(maca2)
            return True
    else:
        return False
    


'''
colidirem_pa: Cobra, PAREDES -> Boolean
Verifica se a cobra colidiu com a parede.
'''


def colidirem_pa(cobra):
    if (cobra.x >= PAREDE_DIREITA) or (cobra.x <= PAREDE_ESQUERDA) or (cobra.y <= PAREDE_CIMA) or (
            cobra.y >= PAREDE_BAIXO):
        return True
    else:
        return False


'''
mover_jogo: Jogo -> Jogo
A função que é chamada a cada tick para o jogo.
'''


def mover_jogo(jogo):
    if colidirem_cm(jogo.cobra, jogo.maca):
        jogo.maca2.x, jogo.maca2.y = mover_maca(jogo.maca2)
        jogo.cobra.comprimento += 1
        jogo.pontos += 1
        return jogo

    if colidirem_cm2(jogo.cobra, jogo.maca2):
        jogo.game_over = True
        return jogo

    mover_cobra(jogo.cobra)
    
    if colidirem_pa(jogo.cobra):
        jogo.game_over = True
        return jogo

    cabeca = [jogo.cobra.x, jogo.cobra.y]
    jogo.cobra.corpo.append(cabeca)  # acrescenta

    for gomo in jogo.cobra.corpo[:-1]:  # menos o último
        if gomo == cabeca:
            jogo.game_over = True
            return jogo

    if len(jogo.cobra.corpo) > jogo.cobra.comprimento:
        del jogo.cobra.corpo[0]  # remove o índice 0

    return jogo


'''
desenha_cobra: Cobra -> Imagem
Desenha cobra na tela e as próximas.
'''


def desenha_cobra(cobra):
    for gomo in cobra.corpo:
        pg.draw.rect(TELA, (255, 215, 0), (gomo[0], gomo[1], cobra.bloco, cobra.bloco))
    return cobra


'''
desenha_maca: Maça -> Imagem
Desenha a maça na tela.
'''


def desenha_macas(maca, maca2):
    TELA.blit(IMG_MACA, (maca.x, maca.y))
    TELA.blit(IMG_MACA2, (maca2.x, maca2.y))
    return maca, maca2


'''
desenha_fundo: Background -> Imagem
Desenha o background.
'''


def desenha_fundo():
    TELA.blit(IMG_BACKGROUND, (0, 0))


'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo.
'''


def desenha_jogo(jogo):
    if jogo.game_over:
        desenha_fundo()
        fonte = pg.font.SysFont("Showcard Gothic", 72)
        fonte2 = pg.font.SysFont("Showcard Gothic", 30)
        fonte3 = pg.font.SysFont("Showcard Gothic", 10)

        # render: String, Int, Cor
        pontos = str(jogo.pontos)
        texto = fonte.render("FIM DE JOGO", 1, (255, 0, 0))
        texto2 = fonte2.render('Recorde: {0}'.format(pontos), 1, (255, 255, 255))
        texto3 = fonte3.render('Aperte ESPAÇO para tentar novamente', 1, (255, 255, 255))

        # blit: String, (Int, Int)
        TELA.blit(texto, (100, 200))
        TELA.blit(texto2, (200, 300))
        TELA.blit(texto3, (180, 350))
    else:
        desenha_fundo()
        desenha_cobra(jogo.cobra)
        desenha_macas(jogo.maca, jogo.maca2)
        pontos = str(jogo.pontos)
        fonte = pg.font.SysFont("Showcard Gothic", 25)
        texto = fonte.render('Pontos: {0}'.format(pontos), 1, (255, 255, 255))
        TELA.blit(texto, (30, 30))
        return jogo


'''
trata_tecla_cobra: Cobra, EventoTecla -> Cobra
Quando teclar as setas do teclado, guia a cobra em uma direção.
'''


def trata_tecla_cobra(cobra, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_a:
        cobra.dx = -5
        cobra.dy = 0
    if tecla == pg.K_RIGHT or tecla == pg.K_d:
        cobra.dx = 5
        cobra.dy = 0
    if tecla == pg.K_UP or tecla == pg.K_w:
        cobra.dx = 0
        cobra.dy = -5
    if tecla == pg.K_DOWN or tecla == pg.K_s:
        cobra.dx = 0
        cobra.dy = 5
    return cobra


'''
trata_tecla: Jogo, EventoTecla -> Jogo
Trata tecla geral.
'''


def trata_tecla(jogo, tecla):
    if tecla == pg.K_SPACE and jogo.game_over:
        return JOGO_INICIAL
    else:
        jogo.cobra = trata_tecla_cobra(jogo.cobra, tecla)
        return jogo
