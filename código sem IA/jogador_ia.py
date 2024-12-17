# -*- coding: utf-8 -*-
from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro


class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):

         # R1.1: Ganhar, se possível
        jogada = self.ganhar()
        if jogada:
            return jogada
        
        # R1.2: Bloquear o oponente se ele tiver duas marcas consecutivas.
        jogada = self.bloquear_vence_ponente()
        if jogada:
            return jogada

        # R2: Criar uma jogada que crie duas sequências de duas marcas.
        jogada = self.criarDuplaSequencia()
        if jogada:
            return jogada

        # R3: Se o quadrado central estiver livre, marque-o.
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Se seu oponente tiver marcado um dos cantos, marque o canto oposto.
        jogada = self.marcarCantoOposto()
        if jogada:
            return jogada

        # R5: Se houver um canto vazio, marque-o.
        jogada = self.marcarCantoVazio()
        if jogada:
            return jogada

        # R6: Marque arbitrariamente um quadrado vazio.
        return self.marcarAleatorio()
    
    def ganhar(self):
        """ Verifica se a IA tem uma jogada para ganhar. """
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Simula a jogada da IA
                    self.matriz[l][c] = self.tipo
                    if self.tabuleiro.tem_campeao() == self.tipo:
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
        return None

    def bloquear_vence_ponente(self):
        """ Verifica se o oponente está prestes a vencer e bloqueia a jogada. """
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Simula a jogada do oponente
                    self.matriz[l][c] = self.adversario()
                    if self.tabuleiro.tem_campeao() == self.adversario(): 
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
        return None

    def adversario(self):
        """ Retorna o tipo do jogador adversário. """
        return Tabuleiro.JOGADOR_0 if self.tipo == Tabuleiro.JOGADOR_X else Tabuleiro.JOGADOR_X

    def checarDuplaSequencia(self):
        """ Verifica se há duas marcas consecutivas (do jogador ou do oponente) em linha e retorna a jogada. """
        for l in range(3):
            for c in range(3):
                # Verifica linha
                if self.matriz[l][0] == self.matriz[l][1] == self.tipo and self.matriz[l][2] == Tabuleiro.DESCONHECIDO:
                    return (l, 2)
                if self.matriz[l][1] == self.matriz[l][2] == self.tipo and self.matriz[l][0] == Tabuleiro.DESCONHECIDO:
                    return (l, 0)
                if self.matriz[l][0] == self.matriz[l][2] == self.tipo and self.matriz[l][1] == Tabuleiro.DESCONHECIDO:
                    return (l, 1)

                # Verifica coluna
                if self.matriz[0][c] == self.matriz[1][c] == self.tipo and self.matriz[2][c] == Tabuleiro.DESCONHECIDO:
                    return (2, c)
                if self.matriz[1][c] == self.matriz[2][c] == self.tipo and self.matriz[0][c] == Tabuleiro.DESCONHECIDO:
                    return (0, c)
                if self.matriz[0][c] == self.matriz[2][c] == self.tipo and self.matriz[1][c] == Tabuleiro.DESCONHECIDO:
                    return (1, c)

        # Verifica as diagonais
        if self.matriz[0][0] == self.matriz[1][1] == self.tipo and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        if self.matriz[1][1] == self.matriz[2][2] == self.tipo and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        if self.matriz[0][2] == self.matriz[1][1] == self.tipo and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        if self.matriz[1][1] == self.matriz[2][0] == self.tipo and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)

        return None

    def criarDuplaSequencia(self):
        """ Verifica se há uma jogada que cria duas duplas de marcas consecutivas. """
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Tenta colocar a marca nesse espaço
                    self.matriz[l][c] = self.tipo
                    if self.checarDuplaSequencia():
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
        return None

    def marcarCantoOposto(self):
        """ Verifica se o oponente marcou um dos cantos e marca o oposto. """
        opostos = {
            (0, 0): (2, 2),
            (0, 2): (2, 0),
            (2, 0): (0, 2),
            (2, 2): (0, 0)
        }
        
        for (l, c), (op_l, op_c) in opostos.items():
            if self.matriz[l][c] != self.tipo and self.matriz[l][c] != Tabuleiro.DESCONHECIDO:
                if self.matriz[op_l][op_c] == Tabuleiro.DESCONHECIDO:
                    return (op_l, op_c)
        return None

    def marcarCantoVazio(self):
        """ Verifica se há um canto vazio. """
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for (l, c) in cantos:
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)
        return None

    def marcarAleatorio(self):
        """ Marca arbitrariamente um quadrado vazio. """
        lista = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
        
        if len(lista) > 0:
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
            return None
