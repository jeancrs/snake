from constantes import *

''' ##### Inicio das definições de dados ##### '''


from namedlist import namedlist
Cobra = namedlist("Cobra", "x, dx, y, dy")
'''
Cobra pode ser criada como: Cobra(Int[LARGURA/2, ALTURA/2], Int)
interp.: representa a posicao x e y da cobra, e o deslocamento
a cada tick no eixo x e y.
Exemplos:
'''
cobra_inicial = Cobra(LARGURA/2, 5,ALTURA/2,0)
''''
Template para funções que recebem Cobra:
def fn_para_cobra(c):
    if cobra.x colidir com  as paredes:
        return "Game Over"

'''
Maca = ("Maca", "x, y")
'''
Maca pode ser criada como: Cobra(Int[LARGURA/3, ALTURA/3], Int)
interp.: representa a posicao x e y da maca.
Exemplos:
'''
maca_inicial = (x_maca, y_maca)

''''
Template para funções que recebem Maca:
def fn_para_maca(m):
    if maca.x <0 or maca.x > LARGURA:
        return "Maca invalida"

'''
