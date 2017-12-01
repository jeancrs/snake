from dados import *

'''==========================================================================================='''
''' Funções: '''

'''
mover_maca: Maca -> Maca
Produz a próxima maca na tela
'''
def mover_maca():
    x_maca = round(random.randrange(0,LARGURA - blocom))
    y_maca = round(random.randrange(0, ALTURA - blocom))
    return x_maca, y_maca

'''==========================================================================================='''
'''
desenha_fundo: Background -> Imagem
Desenha o background
'''
def desenha_fundo():
    TELA.blit(IMG_BACKGROUND,
              (0,
              0))
'''
desenha: Jogo -> Imagem, Maça e Cobra -> Imagem
Desenha a cobra e a maça na tela
'''

def desenha(jogo):
    desenha_fundo()
    for gomo in corpo:
     pg.draw.rect(TELA, verde, (gomo[0], gomo[1], bloco, bloco))
    pg.draw.rect(TELA, vermelho,(x_maca,y_maca,blocom,blocom))
    mostrar_pontos()
    return jogo
'''
gameOver: Game Over->  Tela
Desenha game over na tela
'''
def gameOver():
    Fonte = pg.font.SysFont('Showcard Gothic', 72)
    tela = Fonte.render('FIM DE JOGO!', True, vermelho)
    rect = tela.get_rect()
    rect.midtop = (300,150)
    TELA.blit(tela, rect)
    pg.display.flip()
    time.sleep(2)
    pg.quit()
    sys.exit()
'''
mostra_pontos: PONTOS->  Tela
Desenha a pontuaçao na tela
'''
def mostrar_pontos():
    Fonte = pg.font.SysFont('Showcard Gothic', 20)
    tela = Fonte.render('Pontos: {0}'.format(pontos), True, preto)
    rect = tela.get_rect()
    rect.midtop = (100, 20)
    TELA.blit(tela, rect)
    pg.display.flip()


'''==========================================================================================='''
'''
mover_cobra: Cobra -> Cobra
Produz a próxima cobra (ou seja, fazer ela andar)
'''
def mover_cobra(cobra):
    global x_maca,y_maca,pontos,corpo,comprimento
    cobra.x = cobra.x + cobra.dx
    cobra.y = cobra.y + cobra.dy
    cabeca = []
    cabeca.append(cobra.x)
    cabeca.append(cobra.y)
    corpo.append(cabeca)
    if len(corpo) > comprimento:
        del corpo[0]
    for gomo in corpo[:-1]:
        if gomo == cabeca:
            gameOver()
    if (cobra.x == blocom and cobra.x <= x_maca + blocom) or (cobra.x + bloco >= x_maca and cobra.x + bloco <= x_maca + blocom) :
        if (cobra.y >= y_maca and cobra.y <= y_maca + blocom):
            x_maca, y_maca = mover_maca()
            comprimento +=5
            pontos +=3
    if (cobra.x >= PAREDE_DIREITA) or (cobra.x <= PAREDE_ESQUERDA):
        gameOver()
    if (cobra.y <= PAREDE_CIMA) or (cobra.y >= PAREDE_BAIXO):
        gameOver()
    return cobra
'''==========================================================================================='''
'''
trata_tecla: Cobra, EventoTecla -> Cobra
Quando teclar as setas do teclado, guia a cobra em uma direção
'''
def trata_tecla(cobra, tecla):
    if tecla == pg.K_LEFT:
      cobra.dx = -5
      cobra.dy = 0
    if tecla == pg.K_RIGHT:
      cobra.dx = 5
      cobra.dy = 0
    if tecla == pg.K_UP:
      cobra.dx = 0
      cobra.dy = -5
    if tecla == pg.K_DOWN:
      cobra.dx = 0
      cobra.dy = 5
    return cobra
