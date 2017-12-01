from funcoes import *

'''==========================================================================================='''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com main(cobra_inicial) '''

def main(inic):
    big_bang(cobra_inicial,
             tela=TELA,
             frequencia=30,
             quando_tick=mover_jogo,
             desenhar=desenha,
             quando_tecla=trata_tecla)
main(cobra_inicial)