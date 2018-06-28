#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from classesInterface import *

import pygame
import sys
from astra import *
from cursor import *
from combate import *

# from PPlay.window import *
# from PPlay.sprite import *
# from PPlay.gameimage import *
# from PPlay.animation import *
#
# dictPosicaoCursor = {} #lista com as posições do cursor
# posicaoAtual = ""


# def adicionaPosicaoCursor(strTag,tuplePosicao):
#
#     dictPosicaoCursor[str(strTag)] = tuplePosicao

# def mudaPosicaoCursor(strNovaPosicao):
#
#     posicaoAtual = strNovaPosicao

def main():

    jogador = Jogador(astIgni)
    inimigo = Inimigo(astIgni)
    turnos = Turnos(jogador,inimigo)
    ai = AI(jogador,inimigo,turnos)

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

    cursor = Cursor(janela,interface + "/glove3.png", interface + "/glove3Espelhada.png")

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
    regiaoImagemInimigo = pygame.transform.scale(regiaoImagemInimigo,(int(unidadeAltura*5.5),int(unidadeAltura*5.5)))
    pygame.draw.rect(regiaoImagemInimigo, AZUL, (0, 0, regiaoImagemInimigo.get_width(), regiaoImagemInimigo.get_height()), larguraBorda)
    larguraRestante -= regiaoImagemInimigo.get_width()
    alturaRestante -= regiaoImagemInimigo.get_height()

    #>imagem do inimigo
    imagemInimigo = pygame.image.load(inimigo.astra.sprite)

    #região nome do inimigo
    regiaoNomeInimigo = pygame.Surface((int(larguraRestante/2),int(regiaoImagemInimigo.get_height()/9)*2))
    regiaoNomeInimigo.fill(PRETO)
    pygame.draw.rect(regiaoNomeInimigo,AZUL,(0,0,regiaoNomeInimigo.get_width(),regiaoNomeInimigo.get_height()),larguraBorda)
    larguraRestante -= regiaoNomeInimigo.get_width()

    #nome do inimigo
    strFonteTextoNomeInimigo = inimigo.astra.fonte
    tamanhoTextoNomeInimigo = 70
    fonteTextoNomeInimigo = pygame.font.Font(strFonteTextoNomeInimigo, tamanhoTextoNomeInimigo)
    corTextoNomeInimigo = inimigo.astra.corFonte
    textoNomeInimigo = inimigo.astra.nome
    nomeInimigo = fonteTextoNomeInimigo.render(textoNomeInimigo,True,corTextoNomeInimigo)

    #região icones inimigo
    regiaoIconesInimigo = pygame.Surface((regiaoNomeInimigo.get_width(),(regiaoImagemInimigo.get_height()/9)))
    regiaoIconesInimigo.fill(PRETO)
    pygame.draw.rect(regiaoIconesInimigo,AZUL,(0,0,regiaoIconesInimigo.get_width(),(regiaoIconesInimigo.get_height())),larguraBorda)

    #icone do elemento do inimigo
    iconeElementoInimigo = pygame.image.load(inimigo.astra.elemento.icone)
    iconeElementoInimigo = pygame.transform.scale(iconeElementoInimigo,(regiaoIconesInimigo.get_height()-(larguraBorda*2),regiaoIconesInimigo.get_height()-(larguraBorda*2)))

    # icone do alinhamento do inimigo
    iconeAlinhamentoInimigo = pygame.image.load(inimigo.astra.alinhamento.icone)
    iconeAlinhamentoInimigo = pygame.transform.scale(iconeAlinhamentoInimigo,(regiaoIconesInimigo.get_height()-(larguraBorda*2),regiaoIconesInimigo.get_height()-(larguraBorda*2)))

    # icone do emblema do inimigo
    iconeEmblemaInimigo = pygame.image.load(inimigo.astra.emblema.icone)
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
    valorHPInimigoAtual = inimigo.hpAtual
    valorHPInimigoTotal = inimigo.astra.hpTotal
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
    valorSPInimigoAtual = inimigo.spAtual
    valorSPInimigoTotal = inimigo.astra.spTotal
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
    valorForcaInimigo = inimigo.forcaTotal
    textoForcaInimigo = "Força: " + str(valorForcaInimigo)
    forcaInimigo = fonteTextoForcaInimigo.render(textoForcaInimigo, True, corTextoForcaInimigo)

    #vigor do inimigo
    strFonteTextoVigorInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoVigorInimigo = 40
    fonteTextoVigorInimigo = pygame.font.Font(strFonteTextoVigorInimigo, tamanhoTextoVigorInimigo)
    corTextoVigorInimigo = (255, 255, 255)
    valorVigorInimigo = inimigo.vigorTotal
    textoVigorInimigo = "Vigor: " + str(valorVigorInimigo)
    vigorInimigo = fonteTextoVigorInimigo.render(textoVigorInimigo, True, corTextoVigorInimigo)

    #precisão do inimigo
    strFonteTextoPrecisaoInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoPrecisaoInimigo = 40
    fonteTextoPrecisaoInimigo = pygame.font.Font(strFonteTextoPrecisaoInimigo, tamanhoTextoPrecisaoInimigo)
    corTextoPrecisaoInimigo = (255, 255, 255)
    valorPrecisaoInimigo = inimigo.precisaoTotal
    textoPrecisaoInimigo = "Precisão: " + str(valorPrecisaoInimigo)
    precisaoInimigo = fonteTextoPrecisaoInimigo.render(textoPrecisaoInimigo, True, corTextoPrecisaoInimigo)

    #evasão do inimigo
    strFonteTextoEvasaoInimigo = fontes + "/BebasNeue.ttf"
    tamanhoTextoEvasaoInimigo = 40
    fonteTextoEvasaoInimigo = pygame.font.Font(strFonteTextoEvasaoInimigo, tamanhoTextoEvasaoInimigo)
    corTextoEvasaoInimigo = (255, 255, 255)
    valorEvasaoInimigo = inimigo.astra.evasao
    textoEvasaoInimigo = "Evasão: " + str(valorEvasaoInimigo)
    evasaoInimigo = fonteTextoEvasaoInimigo.render(textoEvasaoInimigo, True, corTextoEvasaoInimigo)

    #regiao borda superior seleção de ação
    regiaoBordaSuperiorSelecao = pygame.Surface((regiaoImagemInimigo.get_width(),alturaRestante/4))
    regiaoBordaSuperiorSelecao.fill(PRETO)

    #região borda inferior seleção de ação
    regiaoBordaInferiorSelecao = regiaoBordaSuperiorSelecao

    #borda superior seleção de ação
    decoracaoBorda = pygame.image.load(interfaceCombate + "/decoracao4elementos.png")
    decoracaoBorda = pygame.transform.scale(decoracaoBorda,(int(regiaoBordaSuperiorSelecao.get_width()/3),regiaoBordaSuperiorSelecao.get_height()))

    #regiao seleção de ataque
    regiaoSelecaoAtaque = pygame.Surface((regiaoImagemInimigo.get_width()/3,regiaoBordaSuperiorSelecao.get_height()))
    regiaoSelecaoAtaque.fill(PRETO)
    pygame.draw.rect(regiaoSelecaoAtaque,AZUL,(0,0,regiaoSelecaoAtaque.get_width(),regiaoSelecaoAtaque.get_height()),larguraBorda)
    cursor.adicionaPosicao("ataque", (regiaoSelecaoAtaque.get_width(),regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height()*1.5))


    #texto ATAQUE
    strFonteTextoATAQUE = fontes + "/BebasNeue.ttf"
    tamanhoTextoATAQUE = 40
    fonteTextoATAQUE = pygame.font.Font(strFonteTextoATAQUE, tamanhoTextoATAQUE)
    corTextoATAQUE = (255, 255, 255)
    textoATAQUE = "ATAQUE"
    selecaoATAQUE = fonteTextoATAQUE.render(textoATAQUE, True, corTextoATAQUE)

    # regiao seleção de tecnica
    regiaoSelecaoTecnica = pygame.Surface((regiaoSelecaoAtaque.get_width(),regiaoSelecaoAtaque.get_height()))
    regiaoSelecaoTecnica.fill(PRETO)
    pygame.draw.rect(regiaoSelecaoTecnica,AZUL,(0, 0,regiaoSelecaoTecnica.get_width(),regiaoSelecaoTecnica.get_height()), larguraBorda)
    cursor.adicionaPosicao("tecnica", (regiaoSelecaoAtaque.get_width(), regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height() * 2.5))

    # texto TECNICA
    strFonteTextoTECNICA = fontes + "/BebasNeue.ttf"
    tamanhoTextoTECNICA = 40
    fonteTextoTECNICA = pygame.font.Font(strFonteTextoTECNICA, tamanhoTextoTECNICA)
    corTextoTECNICA = (255, 255, 255)
    textoTECNICA = "TÉCNICA"
    selecaoTECNICA = fonteTextoTECNICA.render(textoTECNICA, True, corTextoTECNICA)

    # regiao seleção de tecnica elemental
    regiaoSelecaoTecnicaElemental = pygame.Surface((regiaoSelecaoAtaque.get_width(), regiaoSelecaoAtaque.get_height()))
    regiaoSelecaoTecnicaElemental.fill((0,50,0))
    pygame.draw.rect(regiaoSelecaoTecnicaElemental, AZUL,(0, 0, regiaoSelecaoTecnicaElemental.get_width(), regiaoSelecaoTecnicaElemental.get_height()), larguraBorda)
    cursor.adicionaPosicao("elemental", (regiaoSelecaoAtaque.get_width()*2, regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height() * 1.5))

    # texto TECNICA ELEMENTAL
    strFonteTextoTECNICAELEMENTAL = fontes + "/BebasNeue.ttf"
    tamanhoTextoTECNICAELEMENTAL = 30
    fonteTextoTECNICAELEMENTAL = pygame.font.Font(strFonteTextoTECNICAELEMENTAL, tamanhoTextoTECNICAELEMENTAL)
    corTextoTECNICAELEMENTAL = (255, 255, 255)
    textoTECNICAELEMENTAL = inimigo.astra.tecnicaElemento.nome
    selecaoTECNICAELEMENTAL = fonteTextoTECNICAELEMENTAL.render(textoTECNICAELEMENTAL, True, corTextoTECNICAELEMENTAL)

    # regiao seleção de tecnica polares
    regiaoSelecaoTecnicaPolar = pygame.Surface((regiaoSelecaoAtaque.get_width(), regiaoSelecaoAtaque.get_height()))
    regiaoSelecaoTecnicaPolar.fill((0,50,0))
    pygame.draw.rect(regiaoSelecaoTecnicaPolar,AZUL,(0,0,regiaoSelecaoTecnicaPolar.get_width(),regiaoSelecaoTecnicaPolar.get_height()),larguraBorda)
    cursor.adicionaPosicao("polar", (regiaoSelecaoAtaque.get_width()*3, regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height() * 1.5))

    # texto TECNICA POLAR
    strFonteTextoTECNICAPOLAR = fontes + "/BebasNeue.ttf"
    tamanhoTextoTECNICAPOLAR = 30
    fonteTextoTECNICAPOLAR = pygame.font.Font(strFonteTextoTECNICAPOLAR, tamanhoTextoTECNICAPOLAR)
    corTextoTECNICAPOLAR = (255, 255, 255)
    textoTECNICAPOLAR = inimigo.astra.tecnicaAlinhamento.nome
    selecaoTECNICAPOLAR = fonteTextoTECNICAPOLAR.render(textoTECNICAPOLAR, True, corTextoTECNICAPOLAR)

    # regiao seleção de tecnica emblematicas
    regiaoSelecaoTecnicaEmblema = pygame.Surface((regiaoSelecaoAtaque.get_width(), regiaoSelecaoAtaque.get_height()))
    regiaoSelecaoTecnicaEmblema.fill((0, 50, 0))
    pygame.draw.rect(regiaoSelecaoTecnicaEmblema,AZUL,(0,0,regiaoSelecaoTecnicaEmblema.get_width(),regiaoSelecaoTecnicaEmblema.get_height()),larguraBorda)
    cursor.adicionaPosicao("emblema", (regiaoSelecaoAtaque.get_width()*2, regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height() * 2.5))


    # texto TECNICA EMBLEMA
    strFonteTextoTECNICAEMBLEMA = fontes + "/BebasNeue.ttf"
    tamanhoTextoTECNICAEMBLEMA = 30
    fonteTextoTECNICAEMBLEMA = pygame.font.Font(strFonteTextoTECNICAEMBLEMA, tamanhoTextoTECNICAEMBLEMA)
    corTextoTECNICAEMBLEMA = (255, 255, 255)
    textoTECNICAEMBLEMA = inimigo.astra.tecnicaEmblema.nome
    selecaoTECNICAEMBLEMA = fonteTextoTECNICAEMBLEMA.render(textoTECNICAEMBLEMA, True, corTextoTECNICAEMBLEMA)

    # regiao seleção de tecnica únicas
    regiaoSelecaoTecnicaUnica = pygame.Surface((regiaoSelecaoAtaque.get_width(), regiaoSelecaoAtaque.get_height()))
    regiaoSelecaoTecnicaUnica.fill((0, 50, 0))
    pygame.draw.rect(regiaoSelecaoTecnicaUnica, AZUL, (0, 0, regiaoSelecaoTecnicaUnica.get_width(), regiaoSelecaoTecnicaUnica.get_height()), larguraBorda)
    cursor.adicionaPosicao("unica", (regiaoSelecaoAtaque.get_width()*3, regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height() * 2.5))

    # texto TECNICA UNICA
    strFonteTextoTECNICAUNICA = fontes + "/BebasNeue.ttf"
    tamanhoTextoTECNICAUNICA = 30
    fonteTextoTECNICAUNICA = pygame.font.Font(strFonteTextoTECNICAUNICA, tamanhoTextoTECNICAUNICA)
    corTextoTECNICAUNICA = (255, 255, 255)
    textoTECNICAUNICA = inimigo.astra.tecnicaUnica.nome
    selecaoTECNICAUNICA = fonteTextoTECNICAUNICA.render(textoTECNICAUNICA, True, corTextoTECNICAUNICA)

    #26 de junho
    #fazer a parte inferior da interface
    #fazer o sistema de combate, incluindo as tecnicas dos astras da sexta feira

    #game loop
    while(jogando==True):

        #eventos
        eventos = pygame.event.get()
        # atualiza valores
        valorHPInimigoAtual = inimigo.hpAtual
        textoHPInimigo2 = str(valorHPInimigoAtual) + "/" + str(valorHPInimigoTotal)
        HPInimigo2 = fonteTextoHPInimigo.render(textoHPInimigo2, True, corTextoHPInimigo)

        valorSPInimigoAtual = inimigo.spAtual
        textoSPInimigo2 = str(valorSPInimigoAtual) + "/" + str(valorSPInimigoTotal)
        SPInimigo2 = fonteTextoSPInimigo.render(textoSPInimigo2, True, corTextoSPInimigo)

        valorForcaInimigo = inimigo.forcaTotal
        textoForcaInimigo = "Força: " + str(valorForcaInimigo)
        forcaInimigo = fonteTextoForcaInimigo.render(textoForcaInimigo, True, corTextoForcaInimigo)

        valorVigorInimigo = inimigo.vigorTotal
        textoVigorInimigo = "Vigor: " + str(valorVigorInimigo)
        vigorInimigo = fonteTextoVigorInimigo.render(textoVigorInimigo, True, corTextoVigorInimigo)

        valorPrecisaoInimigo = inimigo.precisaoTotal
        textoPrecisaoInimigo = "Precisão: " + str(valorPrecisaoInimigo)
        precisaoInimigo = fonteTextoPrecisaoInimigo.render(textoPrecisaoInimigo, True, corTextoPrecisaoInimigo)

        valorEvasaoInimigo = inimigo.astra.evasao
        textoEvasaoInimigo = "Evasão: " + str(valorEvasaoInimigo)
        evasaoInimigo = fonteTextoEvasaoInimigo.render(textoEvasaoInimigo, True, corTextoEvasaoInimigo)

        if(inimigo.hpAtual <= 0):

            print("você venceu!!!!")
            jogando = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        elif(jogador.hpAtual <= 0):

            print("você perdeu!!!!")
            jogando = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        for evento in eventos:

            #eventos de teclado
            if (evento.type == pygame.KEYDOWN):

                if (evento.key == pygame.K_ESCAPE):

                    jogando = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

                elif(evento.key == pygame.K_RETURN):

                    if(cursor.posicaoAtual == "ataque"):

                        ataque(jogador,inimigo)
                        turnos.incrementaTurno()
                        turnos.mudaLado()
                        ai.determinaAcao()

                    elif(cursor.posicaoAtual == "tecnica"):

                        cursor.mudaPosicao("elemental")

                    elif(cursor.posicaoAtual == "elemental"):

                        if(jogador.spAtual >= jogador.astra.tecnicaElemento.custo):

                            if(jogador.astra.tecnicaElemento.nome == "hellfire"):

                                hellfire(jogador,inimigo)

                            turnos.incrementaTurno()
                            turnos.mudaLado()
                            ai.determinaAcao()

                        else:

                            print(jogador.astra.nome + " não têm SP suficiente para usar " + jogador.astra.tecnicaElemento.nome + ".")

                    elif(cursor.posicaoAtual == "polar"):

                        if(jogador.spAtual >= jogador.astra.tecnicaAlinhamento.custo ):

                            if(jogador.astra.tecnicaAlinhamento.nome == "inspirar"):
                                inspirado = False

                                for i in jogador.listaStatus:

                                    if (i.nome == "inspiracao"):

                                        inspirado = True

                                if (inspirado == False):

                                    inspirar(jogador)

                                else:

                                    print("mas já está inspirado!")


                            turnos.incrementaTurno()
                            turnos.mudaLado()
                            ai.determinaAcao()

                        else:

                            print(jogador.astra.nome + " não têm SP suficiente para usar " + jogador.astra.tecnicaAlinhamento.nome)

                    elif(cursor.posicaoAtual == "emblema"):

                        if(jogador.spAtual >= jogador.astra.tecnicaEmblema.custo):

                                if(jogador.astra.tecnicaEmblema.nome == "encontrão"):

                                    encontrao(jogador,inimigo)

                                turnos.incrementaTurno()
                                turnos.mudaLado()
                                ai.determinaAcao()

                        else:

                            print(jogador.astra.nome + " não têm SP suficiente para usar " + jogador.astra.tecnicaEmblema.nome + ".")

                    elif(cursor.posicaoAtual == "unica"):

                        if(jogador.spAtual >= jogador.astra.tecnicaUnica.custo):

                            if(jogador.astra.tecnicaUnica.nome == "supernova"):

                                supernova(jogador,inimigo)

                            turnos.incrementaTurno()
                            turnos.mudaLado()
                            ai.determinaAcao()

                        else:
                            print(jogador.astra.nome + " não têm SP suficiente para usar " + jogador.astra.tecnicaUnica.nome + ".")

                elif(evento.key == pygame.K_DOWN or evento.key == pygame.K_UP):

                    if(cursor.posicaoAtual == "ataque"):

                        cursor.mudaPosicao("tecnica")

                    elif(cursor.posicaoAtual == "tecnica"):

                        cursor.mudaPosicao("ataque")

                    elif(cursor.posicaoAtual == "elemental"):

                        cursor.mudaPosicao("emblema")

                    elif(cursor.posicaoAtual == "polar"):

                        cursor.mudaPosicao("unica")

                    elif(cursor.posicaoAtual == "emblema"):

                        cursor.mudaPosicao("elemental")

                    elif(cursor.posicaoAtual == "unica"):

                        cursor.mudaPosicao("polar")

                elif(evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT):

                    if(cursor.posicaoAtual == "elemental"):

                        cursor.mudaPosicao("polar")

                    elif(cursor.posicaoAtual == "polar"):

                        cursor.mudaPosicao("elemental")

                    elif(cursor.posicaoAtual == "emblema"):

                        cursor.mudaPosicao("unica")

                    elif(cursor.posicaoAtual  == "unica"):

                        cursor.mudaPosicao("emblema")

                elif(evento.key == pygame.K_BACKSPACE and cursor.posicaoAtual != "tecnica"):

                    cursor.mudaPosicao("ataque")


        #game loop

        #draws e blits

        janela.fill(PRETO)

        #>regioes

        janela.blit(regiaoImagemInimigo,(0, 0))
        janela.blit(regiaoNomeInimigo,(regiaoImagemInimigo.get_width(),0))
        janela.blit(regiaoIconesInimigo,(regiaoImagemInimigo.get_width(),regiaoNomeInimigo.get_height()))
        janela.blit(regiaoTextoPrincipal,((regiaoImagemInimigo.get_width()+regiaoNomeInimigo.get_width()),0))
        janela.blit(regiaoHPInimigo,(regiaoImagemInimigo.get_width(),(regiaoNomeInimigo.get_height()+regiaoIconesInimigo.get_height())))
        janela.blit(regiaoSPInimigo,((regiaoImagemInimigo.get_width()+regiaoHPInimigo.get_width()),(regiaoNomeInimigo.get_height()+regiaoIconesInimigo.get_height())))
        alturaRegiaoAtributosInimigo = regiaoNomeInimigo.get_height() + regiaoIconesInimigo.get_height() + regiaoHPInimigo.get_height()
        janela.blit(regiaoAtributosInimigo,(regiaoImagemInimigo.get_width(),alturaRegiaoAtributosInimigo))
        janela.blit(regiaoBordaSuperiorSelecao,(0,regiaoImagemInimigo.get_height()))
        janela.blit(regiaoBordaInferiorSelecao,(0,regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height()*3))
        janela.blit(regiaoSelecaoAtaque,(0,regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height()))
        janela.blit(regiaoSelecaoTecnica,(0,regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height()*2))
        janela.blit(regiaoSelecaoTecnicaElemental,(regiaoSelecaoAtaque.get_width(), regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height()))
        janela.blit(regiaoSelecaoTecnicaPolar,(regiaoSelecaoAtaque.get_width()*2, regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height()))
        janela.blit(regiaoSelecaoTecnicaEmblema,(regiaoSelecaoAtaque.get_width(),regiaoImagemInimigo.get_height()+regiaoBordaSuperiorSelecao.get_height()*2))
        janela.blit(regiaoSelecaoTecnicaUnica, (regiaoSelecaoAtaque.get_width()*2, regiaoImagemInimigo.get_height() + regiaoBordaSuperiorSelecao.get_height() * 2))

        #>sprites
        regiaoImagemInimigo.blit(imagemInimigo,((regiaoImagemInimigo.get_width()-imagemInimigo.get_width())/2,regiaoImagemInimigo.get_height()/2-(imagemInimigo.get_height()/9)))
        regiaoIconesInimigo.blit(iconeElementoInimigo,(iconeElementoInimigo.get_width(),larguraBorda))
        regiaoIconesInimigo.blit(iconeAlinhamentoInimigo,((regiaoIconesInimigo.get_width()-(iconeAlinhamentoInimigo.get_width()*2)),larguraBorda))
        regiaoIconesInimigo.blit(iconeEmblemaInimigo,((regiaoIconesInimigo.get_width()/2)-(iconeEmblemaInimigo.get_width()/2),larguraBorda))
        regiaoBordaSuperiorSelecao.blit(decoracaoBorda,(0,0))
        regiaoBordaSuperiorSelecao.blit(decoracaoBorda, (decoracaoBorda.get_width(), 0))
        regiaoBordaSuperiorSelecao.blit(decoracaoBorda, (decoracaoBorda.get_width()*2, 0))


        #textos
        regiaoNomeInimigo.blit(nomeInimigo,((regiaoNomeInimigo.get_width()/2)-(fonteTextoNomeInimigo.size(textoNomeInimigo)[0]/2),(regiaoNomeInimigo.get_height()/2)-(fonteTextoNomeInimigo.get_height()/3)))
        regiaoHPInimigo.fill(PRETO)
        pygame.draw.rect(regiaoHPInimigo, AZUL, (0, 0, regiaoHPInimigo.get_width(), regiaoHPInimigo.get_height()), larguraBorda)
        regiaoHPInimigo.blit(HPInimigo1,((regiaoHPInimigo.get_width()/2)-(fonteTextoHPInimigo.size(textoHPInimigo1)[0]/2),(regiaoHPInimigo.get_height()/5)-(fonteTextoHPInimigo.get_height()/4)))
        regiaoHPInimigo.blit(HPInimigo2,((regiaoHPInimigo.get_width()/2)-(fonteTextoHPInimigo.size(textoHPInimigo2)[0]/2),(regiaoHPInimigo.get_height()/2)-(fonteTextoHPInimigo.get_height()/100)))
        regiaoSPInimigo.fill(PRETO)
        pygame.draw.rect(regiaoSPInimigo, AZUL, (0, 0, regiaoSPInimigo.get_width(), regiaoSPInimigo.get_height()), larguraBorda)
        regiaoSPInimigo.blit(SPInimigo1,((regiaoSPInimigo.get_width()/2)-(fonteTextoSPInimigo.size(textoSPInimigo1)[0]/2),(regiaoSPInimigo.get_height()/5)-(fonteTextoSPInimigo.get_height()/4)))
        regiaoSPInimigo.blit(SPInimigo2,((regiaoSPInimigo.get_width()/2)-(fonteTextoSPInimigo.size(textoSPInimigo2)[0]/2),(regiaoSPInimigo.get_height()/2)-(fonteTextoSPInimigo.get_height()/100)))
        regiaoAtributosInimigo.fill(PRETO)
        pygame.draw.rect(regiaoAtributosInimigo, AZUL, (0, 0, regiaoAtributosInimigo.get_width(), regiaoAtributosInimigo.get_height()), larguraBorda)
        regiaoAtributosInimigo.blit(forcaInimigo,((regiaoAtributosInimigo.get_width()/4)-fonteTextoForcaInimigo.size(textoForcaInimigo)[0]/2,regiaoAtributosInimigo.get_height()/6))
        regiaoAtributosInimigo.blit(vigorInimigo,((regiaoAtributosInimigo.get_width()/2)+fonteTextoVigorInimigo.size(textoVigorInimigo)[0]/4,regiaoAtributosInimigo.get_height()/6))
        regiaoAtributosInimigo.blit(precisaoInimigo,((regiaoAtributosInimigo.get_width()/4)-fonteTextoPrecisaoInimigo.size(textoPrecisaoInimigo)[0]/2,(regiaoAtributosInimigo.get_height()/2)+fonteTextoForcaInimigo.get_height()/4))
        regiaoAtributosInimigo.blit(evasaoInimigo,((regiaoAtributosInimigo.get_width()/2)+fonteTextoEvasaoInimigo.size(textoEvasaoInimigo)[0]/4,(regiaoAtributosInimigo.get_height()/2)+fonteTextoEvasaoInimigo.get_height()/4))
        regiaoSelecaoAtaque.blit(selecaoATAQUE,(regiaoSelecaoAtaque.get_width()/2-fonteTextoATAQUE.size(textoATAQUE)[0]/2,regiaoSelecaoAtaque.get_height()/2-fonteTextoATAQUE.get_height()/2))
        regiaoSelecaoTecnica.blit(selecaoTECNICA,(regiaoSelecaoTecnica.get_width()/2-fonteTextoTECNICA.size(textoTECNICA)[0]/2,regiaoSelecaoTecnica.get_height()/2-fonteTextoTECNICA.get_height()/2))
        regiaoSelecaoTecnicaElemental.blit(selecaoTECNICAELEMENTAL,(regiaoSelecaoTecnicaElemental.get_width()/2-fonteTextoTECNICAELEMENTAL.size(textoTECNICAELEMENTAL)[0]/2,regiaoSelecaoTecnicaElemental.get_height()/2-fonteTextoTECNICAELEMENTAL.get_height()/2))
        regiaoSelecaoTecnicaPolar.blit(selecaoTECNICAPOLAR,(regiaoSelecaoTecnicaPolar.get_width()/2-fonteTextoTECNICAPOLAR.size(textoTECNICAPOLAR)[0]/2,regiaoSelecaoTecnicaPolar.get_height()/2-fonteTextoTECNICAPOLAR.get_height() / 2))
        regiaoSelecaoTecnicaEmblema.blit(selecaoTECNICAEMBLEMA, (regiaoSelecaoTecnicaEmblema.get_width() / 2 - fonteTextoTECNICAEMBLEMA.size(textoTECNICAEMBLEMA)[0] / 2, regiaoSelecaoTecnicaEmblema.get_height() / 2 - fonteTextoTECNICAEMBLEMA.get_height() / 2))
        regiaoSelecaoTecnicaUnica.blit(selecaoTECNICAUNICA, (regiaoSelecaoTecnicaUnica.get_width() / 2 - fonteTextoTECNICAUNICA.size(textoTECNICAUNICA)[0] / 2, regiaoSelecaoTecnicaUnica.get_height() / 2 - fonteTextoTECNICAUNICA.get_height() / 2))

        # cursor
        cursor.draw()

        # updates
        pygame.display.update()


main()