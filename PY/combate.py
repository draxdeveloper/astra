#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math
import random
from astra import *

class Turnos(object):

    turnoAtual = 1
    ladoAtual = "jogador"

    jogador = None
    inimigo = None

    def __init__(self,jogador,inimigo):

        self.jogador = jogador
        self.inimigo = inimigo

    def incrementaTurno(self):

        self.turnoAtual += 1
        print("turno atual:" + str(self.turnoAtual))



    def mudaLado(self):

        if(self.ladoAtual == "jogador"):

            self.ladoAtual = "inimigo"
            print("turno do:" + self.ladoAtual)
            print("HP do jogador:" + str(self.jogador.hpAtual))
            aplicaStatus(self.inimigo)
            self.inimigo.atualizaAtributos()



        else:

            self.ladoAtual = "jogador"
            print("turno do:" + self.ladoAtual)
            print("HP do jogador:" + str(self.jogador.hpAtual))
            aplicaStatus(self.jogador)
            self.jogador.atualizaAtributos()

class AI(object):

    inimigo = None
    jogador = None
    turnos = None
    probabilidadeAtacar = 40
    tecnicasUsaveis = []

    def __init__(self,jogador,inimigo,turnos):

        self.inimigo = inimigo
        self.jogador = jogador
        self.turnos = turnos

    def determinaAcao(self):

        if(self.turnos.ladoAtual == "inimigo"):

            random.seed()

            tentativa = random.randint(0,100)

            print(self.inimigo.astra.nome + " está pensando...")

            self.listaTecnicasUsaveis()

            if(tentativa <= 40 or len(self.tecnicasUsaveis ) == 0):

                ataque(self.inimigo,self.jogador)

            else:

                print(self.inimigo.astra.nome + " está pensando em qual tecnica usar...")

                escolha = random.randint(0,len(self.tecnicasUsaveis)-1)

                print(self.inimigo.astra.nome + " decidiu usar " + self.tecnicasUsaveis[escolha].nome)

                if(self.tecnicasUsaveis[escolha].nome == "hellfire"):

                    hellfire(self.inimigo,self.jogador)

                elif(self.tecnicasUsaveis[escolha].nome == "inspirar"):


                    inspirado = False

                    for i in self.inimigo.listaStatus:

                        if (i.nome == "inspiracao"):

                            inspirado = True

                    if (inspirado == False):

                        inspirar(self.inimigo)

                    else:

                        print("mas já está inspirado!")

                elif(self.tecnicasUsaveis[escolha].nome == "encontrão"):

                    encontrao(self.inimigo,self.jogador)

                elif(self.tecnicasUsaveis[escolha].nome == "supernova"):

                    supernova(self.inimigo,self.jogador)


            self.limpaListaTecnicasUsaveis()
            self.turnos.incrementaTurno()
            self.turnos.mudaLado()


    def listaTecnicasUsaveis(self):

        if(self.inimigo.spAtual >= self.inimigo.astra.tecnicaElemento.custo):

            self.tecnicasUsaveis.append(self.inimigo.astra.tecnicaElemento)
            print(self.inimigo.astra.nome + " pode usar " + self.inimigo.astra.tecnicaElemento.nome)

        if(self.inimigo.spAtual >= self.inimigo.astra.tecnicaAlinhamento.custo):

            self.tecnicasUsaveis.append(self.inimigo.astra.tecnicaAlinhamento)
            print(self.inimigo.astra.nome + " pode usar " + self.inimigo.astra.tecnicaAlinhamento.nome)

        if (self.inimigo.spAtual >= self.inimigo.astra.tecnicaEmblema.custo):

            self.tecnicasUsaveis.append(self.inimigo.astra.tecnicaEmblema)
            print(self.inimigo.astra.nome + " pode usar " + self.inimigo.astra.tecnicaEmblema.nome)

        if (self.inimigo.spAtual >= self.inimigo.astra.tecnicaUnica.custo):

            self.tecnicasUsaveis.append(self.inimigo.astra.tecnicaUnica)
            print(self.inimigo.astra.nome + " pode usar " + self.inimigo.astra.tecnicaUnica.nome)


    def limpaListaTecnicasUsaveis(self):

        self.tecnicasUsaveis.clear()

def aplicaStatus(alvo):

    for i in alvo.listaStatus:

            if(i.nome == "inspiracao"):

                alvo.resetaModificadores()

                random.seed()

                tentativa = random.randint(0,100)

                if(tentativa <= effInspiracao.probabilidadeManter):


                    aplicaInspiracao(alvo)

                    print("força:" + str(alvo.forcaTotal) + "/ vigor:" + str(alvo.vigorTotal) + "/ precisão:" + str(alvo.precisaoTotal) + "/ evasao:" + str(alvo.evasaoTotal))

                else:

                    print(alvo.astra.nome + " não está mais inspirado!")
                    alvo.listaStatus.remove(i)

def aplicaInspiracao(alvo):

    random.seed()

    atributo = random.randint(1, 4)

    print(alvo.astra.nome + " está inspirado!")

    if (atributo == 1):
        alvo.bonusForca = 20
        print("aumentou 20 de força!")

    elif (atributo == 2):
        alvo.bonusVigor = 20
        print("aumentou 20 de vigor!")

    elif (atributo == 3):
        alvo.bonusPrecisao = 10
        print("aumentou 10 de precisão!")

    elif (atributo == 4):
        alvo.bonusEvasao = 10
        print("aumentou 10 de evasão!")

    alvo.atualizaAtributos()

def ataque(atacante,defensor):

    chanceAcertar = atacante.precisaoTotal - defensor.evasaoTotal
    dano = atacante.forcaTotal - defensor.vigorTotal

    random.seed()
    tentativa = random.randint(0,100)
    print(str(atacante.astra.nome) + " desfere um golpe em " + defensor.astra.nome + "!")
    if(tentativa <= chanceAcertar):

        defensor.hpAtual -= dano
        print(defensor.astra.nome + " tomou " + str(dano) + " de dano!")

    else:

        print("mas " + defensor.astra.nome + " esquivou!")

def hellfire(atacante,defensor):

    chanceAcertar = (atacante.precisaoTotal + tecHellfire.precisaoBase) - (defensor.evasaoTotal)
    dano = (atacante.forcaTotal + tecHellfire.danoBase) - defensor.vigorTotal

    atacante.spAtual -= tecHellfire.custo
    print("SP:" + str(atacante.spAtual))

    random.seed()
    tentativa = random.randint(0, 100)
    print(str(atacante.astra.nome) + " tenta invocar chamas infernais!!!")
    if (tentativa <= chanceAcertar):
        defensor.hpAtual -= dano
        print(defensor.astra.nome + " tomou " + str(dano) + " de dano!")

    else:
        print("mas não conseguiu!")

def encontrao(atacante,defensor):

    chanceAcertar = (atacante.precisaoTotal + tecEncontrao.precisaoBase) - (defensor.evasaoTotal)
    dano = int(((atacante.forcaTotal + tecEncontrao.danoBase) - defensor.vigorTotal) * 1.4)

    atacante.spAtual -= tecEncontrao.custo
    print("SP:"+str(atacante.spAtual))

    random.seed()
    tentativa = random.randint(0, 100)
    print(str(atacante.astra.nome) + " lança seu corpo contra " + defensor.astra.nome)

    if (tentativa <= chanceAcertar):

        defensor.hpAtual -= dano
        print(defensor.astra.nome + " tomou " + str(dano) + " de dano!")
        atacante.hpAtual -= int(dano * 0.2)
        print("mas " + defensor.astra.nome + " tomou de volta " + str(int(dano*0.2)) + " de dano")
        print(atacante.hpAtual)

    else:

        print("mas " + defensor.astra.nome + " esquivou elegantemente!")

def inspirar(atacante):

    print(atacante.astra.nome + " tenta se inspirar.")



    chanceAcertar = atacante.precisaoTotal + tecInspirar.precisaoBase

    atacante.spAtual -= tecInspirar.custo
    print("SP:"+str(atacante.spAtual))

    random.seed()
    tentativa = random.randint(0,100)

    if(tentativa <= chanceAcertar):

        atacante.listaStatus.append(tecInspirar.efeito)

        print("e conseguiu!")

        atacante.resetaModificadores()

        aplicaInspiracao(atacante)

        print("força:" + str(atacante.forcaTotal) + "/ vigor:" +  str(atacante.vigorTotal) + "/ precisão:" + str(atacante.precisaoTotal) + "/ evasao:" + str(atacante.evasaoTotal))

    else:

        print("mas não conseguiu!")

def supernova(atacante,defensor):

    chanceAcertar = (atacante.precisaoTotal + tecSuperNova.precisaoBase) - (defensor.evasaoTotal)
    dano = (atacante.forcaTotal + tecSuperNova.danoBase) - defensor.vigorTotal

    atacante.spAtual -= tecSuperNova.custo
    print(atacante.spAtual)

    random.seed
    tentativa = random.randrange(0, 100)
    print(str(atacante.astra.nome) + " começa concentra um supernova")
    if (tentativa <= chanceAcertar):

        defensor.hpAtual -= dano
        print(defensor.astra.nome + " tomou " + str(dano) + " de dano!")

    else:
        print("mas ela falhou!")