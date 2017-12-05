from dados import *

'''===================='''
''' Funções: '''

'''
mover_cobra: Cobra -> Cobra
Produz a próxima cobra (ou seja, fazer ela andar)
'''

def mover_cobra(cobra):
    if cobra.x < PAREDE_ESQUERDA or cobra.x > PAREDE_DIREITA or cobra.y < PAREDE_CIMA or cobra.y > PAREDE_BAIXO:
        return "Erro: Cobra invalida"
    else:
        cobra.x = cobra.x + cobra.dx
        cobra.y = cobra.y + cobra.dy
    return cobra

'''
mover_maca: Maca -> Maca
Produz a próxima maca na tela
'''

def mover_maca(maca):
    if maca.x < PAREDE_ESQUERDA or maca.x > PAREDE_DIREITA or maca.y < PAREDE_CIMA or maca.y > PAREDE_BAIXO:
        return "Erro: maca invalida"
    else:
        maca.x = round(random.randrange(0,LARGURA - maca.blocom))
        maca.y = round(random.randrange(0, ALTURA - maca.blocom))
    return maca.x, maca.y

'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
'''

def mover_jogo(jogo):
    mover_cobra(jogo.cobra)
    cabeca = [jogo.cobra.x, jogo.cobra.y]
    jogo.cobra.corpo.append(cabeca)
    if (jogo.cobra.x == jogo.maca.blocom) and (jogo.cobra.x <= jogo.maca.x + jogo.maca.blocom) or (jogo.cobra.x + jogo.cobra.bloco >= jogo.maca.x) and (jogo.cobra.x + jogo.cobra.bloco <= jogo.maca.x + jogo.maca.blocom) :
        if (jogo.cobra.y >= jogo.maca.y) and (jogo.cobra.y <= jogo.maca.y + jogo.maca.blocom):
            jogo.maca.x, jogo.maca.y = mover_maca(jogo.maca)
            jogo.cobra.comprimento +=1
            jogo.pontos +=1
    if (jogo.cobra.x >= PAREDE_DIREITA) or (jogo.cobra.x <= PAREDE_ESQUERDA) or (jogo.cobra.y <= PAREDE_CIMA) or (jogo.cobra.y >= PAREDE_BAIXO):
        jogo.game_over = True
    if len(jogo.cobra.corpo) > jogo.cobra.comprimento:
        del jogo.cobra.corpo[0]
    for cont in jogo.cobra.corpo[:-1]:
        if cont == cabeca:
            jogo.game_over = True
    return jogo

'''
desenha: Cobra -> Imagem
Desenha cobra na tela
'''

def desenha_cobra(cobra):
    for cont in cobra.corpo:
     pg.draw.rect(TELA, (255,215,0), (cont[0], cont[1], cobra.bloco, cobra.bloco))
    return cobra

'''
desenha: Maca -> Imagem
Desenha a maca na tela
'''

def desenha_maca(maca):
    pg.draw.rect(TELA, (255, 0, 0),(maca.x,maca.y,maca.blocom,maca.blocom))
    return maca

'''
desenha_fundo: Background -> Imagem
Desenha o background
'''

def desenha_fundo():
    TELA.blit(IMG_BACKGROUND,
              (0,
              0))
'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''

def desenha_jogo(jogo):
    if jogo.game_over:
        fonte = pg.font.SysFont("Showcard Gothic", 72)
        fonte2 = pg.font.SysFont("Showcard Gothic", 30)
        fonte3 = pg.font.SysFont("Showcard Gothic", 10)
        ## render: String, Int, Cor
        pontos = str(jogo.pontos)
        texto = fonte.render("FIM DE JOGO", 1, (255, 0, 0))
        texto2 = fonte2.render('Recorde: {0}'.format(pontos), 0, (0,100,0))
        texto3 = fonte3.render('Aperte ESPAÇO para tentar novamente', 1, (0, 0, 0))

        ## blit: String, (Int, Int)
        TELA.blit(texto, (100, 200))
        TELA.blit(texto2, (200, 300))
        TELA.blit(texto3, (180, 350))
    else:
        desenha_fundo()
        desenha_cobra(jogo.cobra)
        desenha_maca(jogo.maca)
        pontos = str(jogo.pontos)
        fonte = pg.font.SysFont("Showcard Gothic", 25)
        texto = fonte.render('Pontos: {0}'.format(pontos), 0, (255,255,255))
        TELA.blit(texto, (30, 30))
        return jogo
    
'''
trata_tecla_cobra: Cobra, EventoTecla -> Cobra
Quando teclar as setas do teclado, guia a cobra em uma direção
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
Trata tecla geral
'''

def trata_tecla(jogo, tecla):
    if tecla == pg.K_SPACE  and jogo.game_over:
        return JOGO_INICIAL
    else:
        jogo.cobra = trata_tecla_cobra(jogo.cobra, tecla)
    return jogo
