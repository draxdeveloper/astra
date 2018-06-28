#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

#classe de cursor

class Cursor(object):

    janela = None
    spriteNormal = ""
    spriteInvertido = ""
    posicaoAtual = ""
    direcao = ""
    dictPosicaoCursor = {}

    def __init__(self,Janela,strSpriteNormal,strSpriteInvertido):

        self.janela = Janela
        self.spriteNormal = pygame.image.load(strSpriteNormal)
        self.spriteInvertido = pygame.image.load(strSpriteInvertido)
        self.mudaPosicao("ataque","direita")

    def adicionaPosicao(self,strTag,tuplePosicao):

        self.dictPosicaoCursor[str(strTag)] = tuplePosicao

    def mudaPosicao(self,strNovaPosicao,strDirecao="direita"):

        self.posicaoAtual = strNovaPosicao
        self.direcao = strDirecao


    def mudaDirecao(self,strDirecao):

        self.direcao = strDirecao

    def draw(self):


        if(self.direcao == "direita"):

            self.janela.blit(self.spriteNormal,self.dictPosicaoCursor[self.posicaoAtual])

        elif(self.direcao == "esquerda"):

            self.janela.blit(self.spriteInvertido,self.dictPosicaoCursor[self.posicaoAtual])

