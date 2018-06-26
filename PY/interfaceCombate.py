#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from classesInterface import *

import pygame
import sys
from astra import *

# from PPlay.window import *
# from PPlay.sprite import *
# from PPlay.gameimage import *
# from PPlay.animation import *

def main():

    jogador = Jogador(astIgni)

    #inicializa modulos

    pygame.init()
    pygame.display.init()
    pygame.font.init()

    #variaveis gerais

    jogando = True

    baseResolucaoLargura = 1920
    baseResolucaoAltura = 1080
    baseProporcaoLargura = 16
    baseProporcaoAltura = 9

    baseLargura = int((baseResolucaoLargura/5)*3)
    baseAltura = int((baseResolucaoAltura/5)*3)

    unidadeLargura = baseLargura/baseResolucaoLargura
    unidadeAltura = baseAltura/baseProporcaoAltura

    #enderecos
    assets = "../assets"
    sprites = assets + "/sprites"
    astras = sprites + "/astras"
    interface = sprites + "/interface"
    interfaceCombate = interface + "/combate"
    fontes = assets + "/fontes"

    #janela

    janelaLargura = baseLargura
    janelaAltura = baseAltura

    larguraBorda = 2

    janela = pygame.display.set_mode((janelaLargura,janelaAltura))

    AZUL = (0,0,255)
    PRETO = (0,0,0)
    BRANCO = (255,255,255)

    janelaNome = "astra"
    janelaCorFundo = PRETO

    pygame.display.set_caption(janelaNome)
    janela.fill(janelaCorFundo)

    #variaveis de consistencia regional
    larguraRestante = janela.get_width() #quantas unidades de largura foram usadas
    alturaRestante = janela.get_height() #quantas unidades de altura foram usadas

    #região imagem do inimigo
    regiaoImagemInimigo = pygame.image.load(interfaceCombate + "/fundoTeste.jpg")
    regiaoImagemInimigo = pygame.transform.scale(regiaoImagemInimigo,(int(unidadeAltura*6),int(unidadeAltura*6)))
    pygame.draw.rect(regiaoImagemInimigo, AZUL, (0, 0, regiaoImagemInimigo.get_width(), regiaoImagemInimigo.get_height()), larguraBorda)
    larguraRestante -= regiaoImagemInimigo.get_width()
    alturaRestante -= regiaoImagemInimigo.get_height()

    #>imagem do inimigo
    imagemInimigo = pygame.image.load(jogador.astra.sprite)

    #região nome do inimigo
    regiaoNomeInimigo = pygame.Surface((int(larguraRestante/2),int(regiaoImagemInimigo.get_height()/9)*2))
    regiaoNomeInimigo.fill(PRETO)
    pygame.draw.rect(regiaoNomeInimigo,AZUL,(0,0,regiaoNomeInimigo.get_width(),regiaoNomeInimigo.get_height()),larguraBorda)
    larguraRestante -= regiaoNomeInimigo.get_width()

    #nome do inimigo
    strFonteTextoNomeInimigo = jogador.astra.fonte
    tamanhoTextoNomeInimigo = 70
    fonteTextoNomeInimigo = pygame.font.Font(strFonteTextoNomeInimigo, tamanhoTextoNomeInimigo)
    corTextoNomeInimigo = jogador.astra.corFonte
    textoNomeInimigo = jogador.astra.nome
    nomeInimigo = fonteTextoNomeInimigo.render(textoNomeInimigo,True,corTextoNomeInimigo)

    #região icones inimigo
    regiaoIconesInimigo = pygame.Surface((regiaoNomeInimigo.get_width(),(regiaoImagemInimigo.get_height()/9)))
    regiaoIconesInimigo.fill(PRETO)
    pygame.draw.rect(regiaoIconesInimigo,AZUL,(0,0,regiaoIconesInimigo.get_width(),(regiaoIconesInimigo.get_height())),larguraBorda)

    #icone do elemento do inimigo
    iconeElementoInimigo = pygame.image.load(jogador.astra.elemento.icone)
    iconeElementoInimigo = pygame.transform.scale(iconeElementoInimigo,(regiaoIconesInimigo.get_height()-(larguraBorda*2),regiaoIconesInimigo.get_height()-(larguraBorda*2)))

    # icone do alinhamento do inimigo
    iconeAlinhamentoInimigo = pygame.image.load(jogador.astra.alinhamento.icone)
    iconeAlinhamentoInimigo = pygame.transform.scale(iconeAlinhamentoInimigo,(regiaoIconesInimigo.get_height()-(larguraBorda*2),regiaoIconesInimigo.get_height()-(larguraBorda*2)))

    # icone do emblema do inimigo
    iconeEmblemaInimigo = pygame.image.load(jogador.astra.emblema.icone)
    iconeEmblemaInimigo = pygame.transform.scale(iconeEmblemaInimigo,(regiaoIconesInimigo.get_height()-(larguraBorda*2),regiaoIconesInimigo.get_height()-(larguraBorda*2)))

    #região texto principal
    regiaoTextoPrincipal = pygame.Surface((larguraRestante,regiaoImagemInimigo.get_height()))
    regiaoTextoPrincipal.fill(PRETO)
    pygame.draw.rect(regiaoTextoPrincipal,AZUL,(0,0,regiaoTextoPrincipal.get_width(),regiaoTextoPrincipal.get_height()),larguraBorda)
    larguraRestante -= regiaoTextoPrincipal.get_width()

    #região HP do inimigo
    regiaoHPInimigo = pygame.Surface((regiaoNomeInimigo.get_width()/2,(regiaoImagemInimigo.get_height()/9)*2))
    regiaoHPInimigo.fill(PRETO)
    pygame.draw.rect(regiaoHPInimigo,AZUL,(0,0,regiaoHPInimigo.get_width(),regiaoHPInimigo.get_height()),larguraBorda)

    #HP do inimigo
    strFonteTextoHPInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoHPInimigo = 30
    fonteTextoHPInimigo = pygame.font.Font(strFonteTextoHPInimigo, tamanhoTextoHPInimigo)
    corTextoHPInimigo = (255, 255, 255)
    valorHPInimigoAtual = jogador.hpAtual
    valorHPInimigoTotal = jogador.astra.hpTotal
    textoHPInimigo1 = "HP"
    textoHPInimigo2 = str(valorHPInimigoAtual) + "/" + str(valorHPInimigoTotal)
    HPInimigo1 = fonteTextoHPInimigo.render(textoHPInimigo1, True, corTextoHPInimigo)
    HPInimigo2 = fonteTextoHPInimigo.render(textoHPInimigo2, True, corTextoHPInimigo)

    #região SP do inimigo
    regiaoSPInimigo = pygame.Surface((regiaoNomeInimigo.get_width()/2,(regiaoImagemInimigo.get_height()/9)*2))
    regiaoSPInimigo.fill(PRETO)
    pygame.draw.rect(regiaoSPInimigo,AZUL,(0,0,regiaoSPInimigo.get_width(),regiaoSPInimigo.get_height()),larguraBorda)

    #SP do inimigo
    strFonteTextoSPInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoSPInimigo = 30
    fonteTextoSPInimigo = pygame.font.Font(strFonteTextoSPInimigo, tamanhoTextoSPInimigo)
    corTextoSPInimigo = (255, 255, 255)
    valorSPInimigoAtual = jogador.spAtual
    valorSPInimigoTotal = jogador.astra.spTotal
    textoSPInimigo1 = "SP"
    textoSPInimigo2 = str(valorSPInimigoAtual) + "/" + str(valorSPInimigoTotal)
    SPInimigo1 = fonteTextoSPInimigo.render(textoSPInimigo1, True, corTextoSPInimigo)
    SPInimigo2 = fonteTextoSPInimigo.render(textoSPInimigo2, True, corTextoSPInimigo)

    #região de atributos do inimigo
    regiaoAtributosInimigo = pygame.Surface((regiaoNomeInimigo.get_width(),(regiaoImagemInimigo.get_height()/9)*4))
    regiaoAtributosInimigo.fill(PRETO)
    pygame.draw.rect(regiaoAtributosInimigo,AZUL,(0,0,regiaoAtributosInimigo.get_width(),regiaoAtributosInimigo.get_height()),larguraBorda)

    #força do inimigo
    strFonteTextoForcaInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoForcaInimigo = 40
    fonteTextoForcaInimigo = pygame.font.Font(strFonteTextoForcaInimigo, tamanhoTextoForcaInimigo)
    corTextoForcaInimigo = (255, 255, 255)
    valorForcaInimigo = jogador.astra.forca
    textoForcaInimigo = "Força: " + str(valorForcaInimigo)
    forcaInimigo = fonteTextoForcaInimigo.render(textoForcaInimigo, True, corTextoForcaInimigo)

    #vigor do inimigo
    strFonteTextoVigorInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoVigorInimigo = 40
    fonteTextoVigorInimigo = pygame.font.Font(strFonteTextoVigorInimigo, tamanhoTextoVigorInimigo)
    corTextoVigorInimigo = (255, 255, 255)
    valorVigorInimigo = jogador.astra.vigor
    textoVigorInimigo = "Vigor: " + str(valorVigorInimigo)
    vigorInimigo = fonteTextoVigorInimigo.render(textoVigorInimigo, True, corTextoVigorInimigo)

    #precisão do inimigo
    strFonteTextoPrecisaoInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoPrecisaoInimigo = 40
    fonteTextoPrecisaoInimigo = pygame.font.Font(strFonteTextoPrecisaoInimigo, tamanhoTextoPrecisaoInimigo)
    corTextoPrecisaoInimigo = (255, 255, 255)
    valorPrecisaoInimigo = jogador.astra.precisao
    textoPrecisaoInimigo = "Precisão: " + str(valorPrecisaoInimigo)
    precisaoInimigo = fonteTextoPrecisaoInimigo.render(textoPrecisaoInimigo, True, corTextoPrecisaoInimigo)

    #evasão do inimigo
    strFonteTextoEvasaoInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoEvasaoInimigo = 40
    fonteTextoEvasaoInimigo = pygame.font.Font(strFonteTextoEvasaoInimigo, tamanhoTextoEvasaoInimigo)
    corTextoEvasaoInimigo = (255, 255, 255)
    valorEvasaoInimigo = jogador.astra.evasao
    textoEvasaoInimigo = "Evasão: " + str(valorEvasaoInimigo)
    evasaoInimigo = fonteTextoEvasaoInimigo.render(textoEvasaoInimigo, True, corTextoEvasaoInimigo)

    #26 de junho
    #fazer a parte inferior da interface
    #fazer o sistema de combate, incluindo as tecnicas dos astras da sexta feira

    #game loop

    while(jogando==True):

        #eventos
        eventos = pygame.event.get()

        for evento in eventos:

            #eventos de teclado
            if (evento.type == pygame.KEYDOWN):

                if (evento.key == pygame.K_ESCAPE):

                    jogando = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()



        #game loop

        #draws e blits

        #>regioes

        janela.blit(regiaoImagemInimigo,(0, 0))
        janela.blit(regiaoNomeInimigo,(regiaoImagemInimigo.get_width(),0))
        janela.blit(regiaoIconesInimigo,(regiaoImagemInimigo.get_width(),regiaoNomeInimigo.get_height()))
        janela.blit(regiaoTextoPrincipal,((regiaoImagemInimigo.get_width()+regiaoNomeInimigo.get_width()),0))
        janela.blit(regiaoHPInimigo,(regiaoImagemInimigo.get_width(),(regiaoNomeInimigo.get_height()+regiaoIconesInimigo.get_height())))
        janela.blit(regiaoSPInimigo,((regiaoImagemInimigo.get_width()+regiaoHPInimigo.get_width()),(regiaoNomeInimigo.get_height()+regiaoIconesInimigo.get_height())))
        alturaRegiaoAtributosInimigo = regiaoNomeInimigo.get_height() + regiaoIconesInimigo.get_height() + regiaoHPInimigo.get_height()
        janela.blit(regiaoAtributosInimigo,(regiaoImagemInimigo.get_width(),alturaRegiaoAtributosInimigo))

        #>sprites
        regiaoImagemInimigo.blit(imagemInimigo,((regiaoImagemInimigo.get_width()-imagemInimigo.get_width())/2,regiaoImagemInimigo.get_height()/2))
        regiaoIconesInimigo.blit(iconeElementoInimigo,(iconeElementoInimigo.get_width(),larguraBorda))
        regiaoIconesInimigo.blit(iconeAlinhamentoInimigo,((regiaoIconesInimigo.get_width()-(iconeAlinhamentoInimigo.get_width()*2)),larguraBorda))
        regiaoIconesInimigo.blit(iconeEmblemaInimigo,((regiaoIconesInimigo.get_width()/2)-(iconeEmblemaInimigo.get_width()/2),larguraBorda))

        #textos
        regiaoNomeInimigo.blit(nomeInimigo,((regiaoNomeInimigo.get_width()/2)-(fonteTextoNomeInimigo.size(textoNomeInimigo)[0]/2),(regiaoNomeInimigo.get_height()/2)-(fonteTextoNomeInimigo.get_height()/3)))
        regiaoHPInimigo.blit(HPInimigo1,((regiaoHPInimigo.get_width()/2)-(fonteTextoHPInimigo.size(textoHPInimigo1)[0]/2),(regiaoHPInimigo.get_height()/5)-(fonteTextoHPInimigo.get_height()/4)))
        regiaoHPInimigo.blit(HPInimigo2,((regiaoHPInimigo.get_width()/2)-(fonteTextoHPInimigo.size(textoHPInimigo2)[0]/2),(regiaoHPInimigo.get_height()/2)-(fonteTextoHPInimigo.get_height()/100)))
        regiaoSPInimigo.blit(SPInimigo1,((regiaoSPInimigo.get_width()/2)-(fonteTextoSPInimigo.size(textoSPInimigo1)[0]/2),(regiaoSPInimigo.get_height()/5)-(fonteTextoSPInimigo.get_height()/4)))
        regiaoSPInimigo.blit(SPInimigo2,((regiaoSPInimigo.get_width()/2)-(fonteTextoSPInimigo.size(textoSPInimigo2)[0]/2),(regiaoSPInimigo.get_height()/2)-(fonteTextoSPInimigo.get_height()/100)))
        regiaoAtributosInimigo.blit(forcaInimigo,((regiaoAtributosInimigo.get_width()/4)-fonteTextoForcaInimigo.size(textoForcaInimigo)[0]/2,regiaoAtributosInimigo.get_height()/6))
        regiaoAtributosInimigo.blit(vigorInimigo,((regiaoAtributosInimigo.get_width()/2)+fonteTextoVigorInimigo.size(textoVigorInimigo)[0]/4,regiaoAtributosInimigo.get_height()/6))
        regiaoAtributosInimigo.blit(precisaoInimigo,((regiaoAtributosInimigo.get_width()/4)-fonteTextoPrecisaoInimigo.size(textoPrecisaoInimigo)[0]/2,(regiaoAtributosInimigo.get_height()/2)+fonteTextoForcaInimigo.get_height()/4))
        regiaoAtributosInimigo.blit(evasaoInimigo,((regiaoAtributosInimigo.get_width()/2)+fonteTextoEvasaoInimigo.size(textoEvasaoInimigo)[0]/8,(regiaoAtributosInimigo.get_height()/2)+fonteTextoForcaInimigo.get_height()/4))

        # updates
        pygame.display.update()

    # rImagemInimigo = Regiao(0,0,janela,"/combate/rImagemInimigo.png",3,3,"tela","direita","tela","abaixo","/combate/fundoTeste.jpg")
    #
    # #astra inimigo, aqui são colocadas as questão de interface do inimigo, o funcionamento fica em outro script
    #
    # inimigo = Sprite("../assets/sprites/astras/orbFogo.png")
    #
    # aninhar(inimigo, janela, rImagemInimigo,"centro","abaixo")
    #
    # #regiao nome do astra inimigo
    #
    # rNomeInimigo = Regiao(-3,0,janela,"/combate/rNomeAstraInimigo.png",3,3,rImagemInimigo,"direita","tela","abaixo")
    #
    # #nome do inimigo
    #
    # nomeInimigo = Sprite("../assets/sprites/interface/combate/nomeAstraIgni.png")
    #
    # aninhar(nomeInimigo,janela,rNomeInimigo,"centro","centro")
    #
    # # região dos simbolos do inimigo
    #
    # rSimboloInimigo = Regiao(-3,-3,janela,"/combate/rSimboloAstraInimigo.png",3,3,rImagemInimigo,"direita",rNomeInimigo,"abaixo")
    #
    # #simbolos do inimigo
    #
    # simboloElemento = Sprite("../assets/sprites/interface/combate/fogoIcone.png")
    # simboloAlinhamento = Sprite("../assets/sprites/interface/combate/solIcone.png")
    # simboloEmblema = Sprite("../assets/sprites/interface/combate/espadaIcone.png")
    #
    # aninhar(simboloElemento, janela, rSimboloInimigo,"esquerda","centro",simboloElemento.width/2)
    # aninhar(simboloAlinhamento, janela, rSimboloInimigo,"esquerda","centro",simboloElemento.width*2.5)
    # aninhar(simboloEmblema, janela, rSimboloInimigo,"esquerda","centro",simboloElemento.width*4.5)
    #
    # #região HP e SP do inimigo
    #
    # rHPInimigo = Regiao(-3,-3,janela,"/combate/rHPSP.png",3,3,rImagemInimigo,"direita",rSimboloInimigo,"abaixo")
    # rSPInimigo = Regiao(0,-3, janela, "/combate/rHPSP.png", 3, 3, rHPInimigo, "direita", rSimboloInimigo, "abaixo")
    #
    # #HP e SP do inimigo
    #
    # hpInimigo = Sprite("../assets/sprites/interface/combate/hpInimigo.png")
    # spInimigo = Sprite("../assets/sprites/interface/combate/spInimigo.png")
    #
    # aninhar(hpInimigo,janela, rHPInimigo,"centro,","centro")
    # aninhar(spInimigo, janela, rSPInimigo, "centro,", "centro")
    #
    # #região de atributos do inimigo
    #
    # rAtributosInimigo = Regiao(-3,0,janela,"/combate/rAtributosInimigo.png",3,3,rImagemInimigo,"direita",rHPInimigo,"abaixo")
    #
    # #atributos do inimigo
    #
    # forInimigo = Sprite("../assets/sprites/interface/combate/forInimigo.png")
    # evaInimigo = Sprite("../assets/sprites/interface/combate/evaInimigo.png")
    # preInimigo = Sprite("../assets/sprites/interface/combate/preInimigo.png")
    # vigInimigo = Sprite("../assets/sprites/interface/combate/vigInimigo.png")
    #
    # aninhar(forInimigo,janela, rAtributosInimigo,"esquerda","acima",10,10)
    # aninhar(evaInimigo,janela, rAtributosInimigo,"direita","abaixo",10,10)
    # aninhar(preInimigo,janela, rAtributosInimigo,"direita","acima",10,10)
    # aninhar(vigInimigo,janela, rAtributosInimigo,"esquerda","abaixo",10,10)
    #
    # #regiao do texto principal
    # rTextoPrincipal = Regiao(0,0,janela,"/combate/rTextoPrincipal.png",3,3,"tela","esquerda","tela","abaixo")
    #
    # #textoPrincipal
    #
    # #>posicionamento baseado em como ira funcionar as linhas
    #
    # totalLinhas = 2
    #
    # linha1 = Sprite("../assets/sprites/interface/combate/textoPrincipalL1.png")
    # linha2 = Sprite("../assets/sprites/interface/combate/textoPrincipalL2.png")
    #
    # aninhar(linha1,janela, rTextoPrincipal,"esquerda","abaixo",5,linha1.height * (totalLinhas - 1) + 5)
    # aninhar(linha2,janela, rTextoPrincipal,"esquerda","abaixo",5,linha1.height * (totalLinhas - 2) + 5)
    #
    # #regiao de decorcao dos 4 elementos, não está na estrutura certa, depois criar uma função para ancorar sprites numa região, não apenas uma região na outra
    # rDecoracaoSuperior1 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,"tela","direita",rImagemInimigo,"abaixo")
    # rDecoracaoSuperior2 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoSuperior1,"direita",rImagemInimigo,"abaixo")
    # rDecoracaoSuperior3 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoSuperior2,"direita",rImagemInimigo,"abaixo")
    # # rDecoracaoSuperior4 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoSuperior3,"direita",rImagemInimigo,"abaixo")
    # rDecoracaoInferior1 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,"tela","direita","tela","acima")
    # rDecoracaoInferior2 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoInferior1,"direita","tela","acima")
    # rDecoracaoInferior3 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoInferior2,"direita","tela","acima")
    # # rDecoracaoInferior4 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoInferior3,"direita","tela","acima")
    #
    # #região seleção de ataque
    # rSelecaoAtaque = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,"tela","direita",rDecoracaoSuperior1,"abaixo","",0,0,True,0)
    # # rSelecaoAtaque.moverRegiao(0,rSelecaoAtaque.getBorda().height)
    #
    # #texto seleção de ataque
    # textoAtaque = Sprite("../assets/sprites/interface/combate/textoSelecaoAtaque.png")
    # aninhar(textoAtaque,janela, rSelecaoAtaque,"centro","centro")
    #
    # #regiao seleção de tecnica
    # rSelecaoTecnica = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,"tela","direita",rDecoracaoInferior1,"acima","",0,0,True,1)
    #
    # #texto seleção tecnica
    # textoTecnica = Sprite("../assets/sprites/interface/combate/textoSelecaoTecnica.png")
    # aninhar(textoTecnica,janela, rSelecaoTecnica,"centro","centro")
    #
    # #regiao selecao tecnica elemental
    # rSelecaoElemental = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoAtaque,"direita",rDecoracaoSuperior2,"abaixo","",0,0,True,2)
    #
    # #texto tecnica elemental
    # textoElemental = Sprite("../assets/sprites/interface/combate/textoElemental.png")
    # aninhar(textoElemental,janela, rSelecaoElemental,"centro","centro")
    #
    # #regiao selecao tecnica alinhamento
    # rSelecaoAlinhamento = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoElemental,"direita",rDecoracaoSuperior3,"abaixo","",0,0,True,3)
    #
    # #texto tecnica alinhamento
    # textoAlinhamento = Sprite("../assets/sprites/interface/combate/textoAlinhamento.png")
    # aninhar(textoAlinhamento,janela, rSelecaoAlinhamento,"centro","centro")
    #
    # #regiao selecao tecnica emblema
    # rSelecaoEmblema = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoTecnica,"direita",rDecoracaoInferior2,"acima","",0,0,True,4)
    #
    # #texto tecnical emblema
    # textoEmblema = Sprite("../assets/sprites/interface/combate/textoEmblema.png")
    # aninhar(textoEmblema,janela, rSelecaoEmblema,"centro","centro")
    #
    # #regiao selecao tecnica especial
    # rSelecaoEspecial = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoEmblema,"direita",rDecoracaoInferior3,"acima","",0,0,True,5)
    #
    # #texto tecnical especial
    # textoEspecial = Sprite("../assets/sprites/interface/combate/textoEspecial.png")
    # aninhar(textoEspecial,janela, rSelecaoEspecial,"centro","centro")
    #
    # #região  do imagem do astra do jogador
    # rImagemJogador = Regiao(0,0,janela,"/combate/rImagemJogador.png",3,3,rSelecaoAlinhamento,"direita",rAtributosInimigo,"abaixo")
    #
    # #imagem astra do jogador
    # jogador = Sprite("../assets/sprites/astras/orbAgua138.png")
    # aninhar(jogador, janela, rImagemJogador,"centro","centro")
    #
    # #região icones do jogador
    # rSimboloJogador = Regiao(0,0,janela,"/combate/rSimboloAstraJogador.png",3,3,rSelecaoEspecial,"direita",rImagemJogador,"abaixo")
    #
    # #simbolos do jogador
    # simboloElementoJogador = Sprite("../assets/sprites/interface/combate/aguaIconeRedux.png")
    # simboloAlinhamentoJogador = Sprite("../assets/sprites/interface/combate/solIconeRedux.png")
    # simboloEmblemaJogador = Sprite("../assets/sprites/interface/combate/espadaIconeRedux.png")
    #
    # aninhar(simboloElementoJogador,janela, rSimboloJogador,"esquerda","centro,")
    # aninhar(simboloAlinhamentoJogador,janela, rSimboloJogador,"centro","centro",-4)
    # aninhar(simboloEmblemaJogador, janela, rSimboloJogador,"direita","centro")
    #
    # #região nome do jogador
    # rNomeJogador = Regiao(0,0,janela,"/combate/rNomeAstraJogador.png",3,3,rImagemJogador,"direita",rAtributosInimigo,"abaixo")
    #
    # #nome do jogador
    # nomeJogador = Sprite("../assets/sprites/interface/combate/nomeAstraAquaRedux.png")
    # aninhar(nomeJogador, janela, rNomeJogador,"centro","centro")
    #
    # #região HP e SP do jogador
    # rHPJogador = Regiao(0,0,janela,"/combate/rHPSPJogador.png",3,3,rImagemJogador,"direita",rNomeJogador,"abaixo")
    # rSPJogador = Regiao(0,0,janela,"/combate/rHPSPJogador.png",3,3, rHPJogador, "direita", rNomeJogador, "abaixo")
    #
    # #texto HP e SP jogador
    # hpJogador = Sprite("../assets/sprites/interface/combate/hpJogador.png")
    # valorHPJogador = Sprite("../assets/sprites/interface/combate/valorHPSPJogador.png")
    # spJogador = Sprite("../assets/sprites/interface/combate/spJogador.png")
    # valorSPJogador = Sprite("../assets/sprites/interface/combate/valorHPSPJogador.png")
    #
    # aninhar(hpJogador,janela, rHPJogador,"centro","acima")
    # aninhar(valorHPJogador,janela, rHPJogador,"centro","abaixo")
    # aninhar(spJogador,janela, rSPJogador,"centro","acima")
    # aninhar(valorSPJogador, janela, rSPJogador,"centro","abaixo")
    #
    # #região atributos do jogador
    # rAtributosJogador = Regiao(0,0,janela,"/combate/rAtributosJogador.png",3,3,rImagemJogador,"direita",rHPJogador,"abaixo")
    #
    # #atributos jogador
    # forJogador = Sprite("../assets/sprites/interface/combate/forJogador.png")
    # preJogador = Sprite("../assets/sprites/interface/combate/preJogador.png")
    # vigJogador = Sprite("../assets/sprites/interface/combate/vigJogador.png")
    # evaJogador = Sprite("../assets/sprites/interface/combate/evaJogador.png")
    #
    # aninhar(forJogador, janela, rAtributosJogador,"esquerda","acima",5,5)
    # aninhar(preJogador,janela, rAtributosJogador,"direita","acima", 5,5)
    # aninhar(vigJogador,janela, rAtributosJogador,"esquerda","abaixo",5,5)
    # aninhar(evaJogador,janela, rAtributosJogador,"direita","abaixo",5,5)
    #
    # #região descrição
    # rDescricao = Regiao(0,0,janela,"/combate/rDescricao.png",3,3,rNomeJogador,"direita",rTextoPrincipal,"abaixo")
    #
    # #texto descrição, ele é variavel e decidido no loop... No momento, futuramente esse processo será uma função da classe de texto
    # descricaoAtual = ""
    #
    # #cursor
    # cursor = Cursor(janela,"/glove3.png","/glove3Espelhada.png")
    # cursor.moveCursor(janela,0)
    #
    # #controle
    #
    # teclado = Window.get_keyboard()
    #
    # sair = "esc"
    # selecaoAbaixo = "down"
    # selecaoAcima = "up"

    #game loop

    # while(teclado.key_pressed(sair) == False):

        # if(teclado.key_pressed("down") or teclado.key_pressed("up")):
        #
        #     if(cursor.getPosAtual() == 1):
        #
        #         cursor.moveCursor(janela,0)
        #
        #     else:
        #
        #         cursor.moveCursor(janela,1)
        #
        # janela.set_background_color(janelaCorFundo)


        #draw regiões

        # rImagemInimigo.desenhaRegiao()
        # rNomeInimigo.desenhaRegiao()
        # rSimboloInimigo.desenhaRegiao()
        # rHPInimigo.desenhaRegiao()
        # rSPInimigo.desenhaRegiao()
        # rAtributosInimigo.desenhaRegiao()
        # rTextoPrincipal.desenhaRegiao()
        # rSelecaoAtaque.desenhaRegiao()
        # rSelecaoTecnica.desenhaRegiao()
        # rSelecaoElemental.desenhaRegiao()
        # rSelecaoAlinhamento.desenhaRegiao()
        # rSelecaoEmblema.desenhaRegiao()
        # rSelecaoEspecial.desenhaRegiao()
        # rDecoracaoSuperior1.desenhaRegiao()
        # rDecoracaoSuperior2.desenhaRegiao()
        # rDecoracaoSuperior3.desenhaRegiao()
        # # rDecoracaoSuperior4.desenhaRegiao()
        # rDecoracaoInferior1.desenhaRegiao()
        # rDecoracaoInferior2.desenhaRegiao()
        # rDecoracaoInferior3.desenhaRegiao()
        # # rDecoracaoInferior4.desenhaRegiao()
        # rImagemJogador.desenhaRegiao()
        # rSimboloJogador.desenhaRegiao()
        # rNomeJogador.desenhaRegiao()
        # rHPJogador.desenhaRegiao()
        # rSPJogador.desenhaRegiao()
        # rAtributosJogador.desenhaRegiao()
        # rDescricao.desenhaRegiao()
        #
        #
        # #draw textos
        #
        # nomeInimigo.draw()
        # hpInimigo.draw()
        # spInimigo.draw()
        # forInimigo.draw()
        # preInimigo.draw()
        # evaInimigo.draw()
        # vigInimigo.draw()
        # linha1.draw()
        # linha2.draw()
        # textoAtaque.draw()
        # textoTecnica.draw()
        # textoElemental.draw()
        # textoAlinhamento.draw()
        # textoEmblema.draw()
        # textoEspecial.draw()
        # nomeJogador.draw()
        # hpJogador.draw()
        # valorHPJogador.draw()
        # spJogador.draw()
        # valorSPJogador.draw()
        # forJogador.draw()
        # preJogador.draw()
        # evaJogador.draw()
        # vigJogador.draw()
        #
        # if(cursor.getPosAtual() == 0):
        #
        #     descricaoAtual = Sprite("../assets/sprites/interface/combate/textoDescricaoAtaque.png")
        #
        # elif(cursor.getPosAtual() == 1):
        #
        #     descricaoAtual = Sprite("../assets/sprites/interface/combate/textoDescricaoTecnica.png")
        #
        #
        # aninhar(descricaoAtual,janela, rDescricao,"esquerda","abaixo",5,2)
        #
        # descricaoAtual.draw()
        #
        # #draw sprites
        #
        # inimigo.draw()
        # simboloElemento.draw()
        # simboloAlinhamento.draw()
        # simboloEmblema.draw()
        # jogador.draw()
        # simboloElementoJogador.draw()
        # simboloAlinhamentoJogador.draw()
        # simboloEmblemaJogador.draw()
        #
        # #draw cursor
        # cursor.desenhaCursor()

main()