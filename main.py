from funcoes import *

'''==========================================================================================='''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
    ''' inicie o mundo com main(JOGO_INICIAL) '''

def main(inic):
    big_bang(inic,
             tela=TELA,
             frequencia=30,
             quando_tick=mover_jogo,
             desenhar=desenha_jogo,
             quando_tecla=trata_tecla,
             modo_debug = True,
             fonte_debug=15)
main(JOGO_INICIAL)
