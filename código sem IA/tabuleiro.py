# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [[Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                       [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                       [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
    
    def tem_campeao(self):
        
        for i in range(3):
            # Verifica linha
            if self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] and self.matriz[i][0] != Tabuleiro.DESCONHECIDO:
                return self.matriz[i][0]
            # Verifica coluna
            if self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] and self.matriz[0][i] != Tabuleiro.DESCONHECIDO:
                return self.matriz[0][i]

        # Verifica diagonais
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] and self.matriz[0][0] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][0]
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] and self.matriz[0][2] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][2]
        
        
        return Tabuleiro.DESCONHECIDO
