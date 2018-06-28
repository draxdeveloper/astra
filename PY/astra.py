#!/usr/bin/env python
# -*- coding: utf-8 -*-

#conjunto de classes e funções relacionadas a geração dos astras

import datetime
import math

#funções

def determinaFaseLua():

    #http://www.ehow.co.uk/how_6216301_calculate-moon-phases-specific-locations.html

    dataAtual = datetime.datetime.now()
    anoAtual = dataAtual.year
    mesAtual = dataAtual.month
    diaAtual = dataAtual.day
    dezenaAno = anoAtual - 2000
    restoAno = dezenaAno%19
    faseLua = "merda"

    if(restoAno > 9):

        restoAno -= 19

    restoVezesOnze = restoAno * 11
    moduloResto = restoVezesOnze

    while(moduloResto < -29 or moduloResto > 29):

        if(moduloResto < 0):

            moduloResto += 30

        else:

            moduloResto -= 30

    somandoMesDia = moduloResto + mesAtual + diaAtual
    idadeLua = somandoMesDia - 8

    if(idadeLua >= 0 and idadeLua < 7.5):

        faseLua = "nova"

    elif(idadeLua >= 7.5 and idadeLua < 15):

        faseLua = "crescente"

    elif(idadeLua >=15 and idadeLua < 22.5):

        faseLua = "cheia"

    elif(idadeLua >= 22.5 and idadeLua <= 29):

        faseLua = "minguante"

    return faseLua

def determinaFaseDia():

    dataAtual = datetime.datetime.now()
    horaAtual = dataAtual.hour
    faseDia = "dia"

    if(horaAtual > 6 and horaAtual < 18):

        faseDia = "dia"

    else:

        faseDia = "noite"

    return faseDia

def sorteiaFaseLua():

    pass

def sorteiaFaseDia():

    pass

def forcaFaseLua():

    pass

def forcaFaseDia():

    pass

#enderecos
assets = "../assets"
fontes = assets + "/fontes"
sprites = assets + "/sprites"
astras = sprites + "/astras"
interface = sprites + "/interface"
interfaceCombate = interface + "/combate"

#listas
listaAstras = []
listaElementos = []
listaAlinhamentos = []
listaEmblemas = []
listaEfeitos = []
listaTecnicas = []

#globais
faseLua = determinaFaseLua()
faseDia = determinaFaseDia()

print(faseLua)
print(faseDia)

#classes

class Jogador(object):

    astra = "" #recebe um Astra

    hpAtual = 0 #total de HP atual
    spAtual = 0 #total de SP atual
    listaStatus = [] #efeitos ativos

    bonusForca = 0
    bonusVigor = 0
    bonusPrecisao = 0
    bonusEvasao = 0

    defictForca = 0
    defictVigor = 0
    defictPrecisao = 0
    defictEvasao = 0

    forcaTotal = 0
    vigorTotal = 0
    precisaoTotal = 0
    evasaoTotal = 0

    def __init__(self,Astra):

        self.astra = Astra
        self.hpAtual = self.astra.hpTotal
        self.spAtual = self.astra.spTotal

        self.atualizaAtributos()

    def atualizaAtributos(self):

        self.forcaTotal = self.astra.forca + self.bonusForca - self.defictForca
        self.vigorTotal = self.astra.vigor + self.bonusVigor - self.defictVigor
        self.precisaoTotal = self.astra.precisao + self.bonusPrecisao - self.defictPrecisao
        self.evasaoTotal = self.astra.evasao + self.bonusEvasao - self.defictEvasao

    def resetaModificadores(self):

        self.bonusForca = 0
        self.bonusVigor = 0
        self.bonusPrecisao = 0
        self.bonusEvasao = 0

        self.defictForca = 0
        self.defictVigor = 0
        self.defictPrecisao = 0
        self.defictEvasao = 0

class Inimigo(object):

    astra = ""  # recebe um Astra

    hpAtual = 0  # total de HP atual
    spAtual = 0  # total de SP atual
    listaStatus = []  # efeitos ativos

    bonusForca = 0
    bonusVigor = 0
    bonusPrecisao = 0
    bonusEvasao = 0

    defictForca = 0
    defictVigor = 0
    defictPrecisao = 0
    defictEvasao = 0

    forcaTotal = 0
    vigorTotal = 0
    precisaoTotal = 0
    evasaoTotal = 0

    def __init__(self, Astra):

        self.astra = Astra
        self.hpAtual = self.astra.hpTotal
        self.spAtual = self.astra.spTotal

        self.atualizaAtributos()


    def atualizaAtributos(self):

        self.forcaTotal = self.astra.forca + self.bonusForca - self.defictForca
        self.vigorTotal = self.astra.vigor + self.bonusVigor - self.defictVigor
        self.precisaoTotal = self.astra.precisao + self.bonusPrecisao - self.defictPrecisao
        self.evasaoTotal = self.astra.evasao + self.bonusEvasao - self.defictEvasao


    def resetaModificadores(self):

        self.bonusForca = 0
        self.bonusVigor = 0
        self.bonusPrecisao = 0
        self.bonusEvasao = 0

        self.defictForca = 0
        self.defictVigor = 0
        self.defictPrecisao = 0
        self.defictEvasao = 0

class Astra(object):

    #atributos do astra, valores de base

    nome = "base"
    fonte = "/BebasNeue.ttf" #endereco a partir da pasta fontes
    corFonte = ()
    sprite = "/orbFogo.png" #endereco a partir da pasta astras

    elemento = "base" #elemento do astra
    alinhamento = "base" #alinhamento do astra
    emblema = "base" #emblema do astra

    forca = 20 #força do astra
    vigor = 20 #vigor do astra
    precisao = 90  #precisao do astra
    evasao = 30 #evasao do astra

    hpTotal = 400
    spTotal = 200

    tecnicaElemento = None
    tecnicaAlinhamento = None
    tecnicaEmblema = None
    tecnicaUnica = None

    def __init__(self,strNome,strFonte,colorCorFonte,strSprite,Elemento,Alinhamento,Emblema):

        self.nome = strNome
        self.fonte = fontes + str(strFonte)
        self.corFonte = colorCorFonte
        self.sprite = astras + str(strSprite)

        self.elemento = Elemento
        self.alinhamento = Alinhamento
        self.emblema = Emblema

        self.forca += self.elemento.forca + self.alinhamento.forca + self.emblema.forca
        self.vigor += self.elemento.vigor + self.alinhamento.vigor + self.emblema.vigor
        self.precisao += self.elemento.precisao + self.alinhamento.precisao + self.emblema.precisao
        self.evasao += self.elemento.evasao + self.alinhamento.evasao + self.emblema.evasao
        self.hpTotal += self.elemento.hp + self.alinhamento.hp + self.emblema.hp
        self.spTotal += self.elemento.sp + self.alinhamento.sp + self.emblema.sp

        self.tecnicaElemento = self.elemento.tecnica
        self.tecnicaAlinhamento = self.alinhamento.tecnica
        self.tecnicaEmblema = self.emblema.tecnica

        buscaTecUnica = str(self.alinhamento.nome) + "_" + str(self.emblema.nome) + "_" + str(self.elemento.nome)

        for i in listaTecnicas:

            if(i.valor == buscaTecUnica):


                self.tecnicaUnica = i
                break

        listaAstras.append(self)

class Elemento(object):

    nome = ""

    forca = 0 #modificador de força
    vigor = 0 #modificador de vigor
    precisao = 0  #modificador de precisao
    evasao = 0 #modificador de evasao

    hp = 0 #modificador de HP
    sp = 0 #modificador de SP

    tecnica = None

    faseLua = "" #fase da lua que o elemento é ativado

    icone = ""

    def __init__(self,strNome,intForca,intVigor,intPrecisao,intEvasao,intHP,intSP,Tecnica,strFaseLua,strIcone):

        self.nome = strNome
        self.forca = intForca
        self.vigor = intVigor
        self.precisao = intPrecisao
        self.evasao = intEvasao
        self.hp = intHP
        self.sp = intSP
        self.tecnica = Tecnica
        self.faseLua = strFaseLua
        self.icone = interfaceCombate + str(strIcone)

        listaElementos.append(self)
        #fazer função de capturar tecnica

class Alinhamento(object):

    nome = ""

    forca = 0 #modificador de força
    vigor = 0 #modificador de vigor
    precisao = 0  #modificador de precisao
    evasao = 0 #modificador de evasao

    hp = 0 #modificador de HP
    sp = 0 #modificador de SP

    tecnica = None

    faseDia = "" #fase da lua que o elemento é ativado

    icone = ""

    def __init__(self,strNome,intForca,intVigor,intPrecisao,intEvasao,intHP,intSP,Tecnica,strFaseDia,strIcone):

        self.nome = strNome
        self.forca = intForca
        self.vigor = intVigor
        self.precisao = intPrecisao
        self.evasao = intEvasao
        self.hp = intHP
        self.sp = intSP
        self.tecnica = Tecnica
        self.faseDia = strFaseDia

        self.icone = interfaceCombate + str(strIcone)

        listaAlinhamentos.append(self)

        #fazer função de capturar tecnica

class Emblema(object):

    nome = ""

    forca = 0 #modificador de força
    vigor = 0 #modificador de vigor
    precisao = 0  #modificador de precisao
    evasao = 0 #modificador de evasao

    hp = 0 #modificador de HP
    sp = 0 #modificador de SP

    tecnica = None

    icone = ""

    def __init__(self,strNome,intForca,intVigor,intPrecisao,intEvasao,intHP,intSP,Tecnica,strIcone):

        self.nome = strNome
        self.forca = intForca
        self.vigor = intVigor
        self.precisao = intPrecisao
        self.evasao = intEvasao
        self.hp = intHP
        self.sp = intSP
        self.tecnica = Tecnica
        self.icone = interfaceCombate + str(strIcone)

        listaEmblemas.append(self)

        #fazer função de capturar tecnica

class Tecnica(object):

    nome = ""
    tipo = "" #elemental,polar,emblematica,unica
    valor = "" #valor que representa o elemento,alinhamento,emblema ou combincao unica com 3 letras maiusculas
    modo = "" #comportamento padrão da tecnica, decide como ela vai funcionar: "ofensivaPura","ofensivaPositiva","ofensivaNegativa","passivaNegativa","passivaPositiva"
    descricao = ""

    custo = 0
    danoBase = 0 #dano base da tecnica
    precisaoBase = 0
    precisaoEfeito = 0
    efeito = None #efeito da tecnica, se existente

    def __init__(self,strNome,strTipo,strValor,strModo,strDescricao,intCusto,intDanoBase,intPrecisaoBase,intPrecisaoEfeito,Efeito):

        self.nome = strNome
        self.tipo = strTipo
        self.valor = strValor
        self.modo = strModo
        self.descricao = strDescricao

        self.custo = intCusto
        self.danoBase = intDanoBase
        self.precisaoBase = intPrecisaoBase
        self.precisaoEfeito = intPrecisaoEfeito
        self.efeito = Efeito

        listaTecnicas.append(self)

class Efeito(object):

    "flags que causam algum efeito todo turno até serem retirados"

    nome = ""
    tipo = "" #positivo ou negativo
    probabilidadeManter = 0

    def __init__(self,strNome,strTipo,intProbabilidadeManter):

        self.nome = strNome
        self.tipo = strTipo
        self.probabilidadeManter = intProbabilidadeManter

        listaEfeitos.append(self)

    def getNome(self):

        return self.nome

    def getTipo(self):

        return self.tipo

    def getProbabilidadeManter(self):

        return self.probabilidadeManter


#funções

#instancias

#instancia de efeitos
effInspiracao = Efeito("inspiracao","positivo",90) #a cada turno aumenta um dos atributos durante aquele turno
effInsanidade = Efeito("insanidade","negativo",80) #a cada turno reduz um dos atributos durante aquele turno
effVeneno = Efeito("veneno","negativo",70) #a cada turno perde 5% do HP
effExaustao = Efeito("exaustao","negativo",70) #a cada turno perde 5% do SP
effRaiva = Efeito("raiva","positivo",70) #aumenta a força e reduz o vigor em 20
effZen = Efeito("zen","positivo",70) #aumenta o vigor e reduz a força em 20
effMirar = Efeito("mirar","positivo",70) #aumenta a precisao e reduz evasao em 20
effNevoa = Efeito("nevoa","positivo",70) #aumenta a evasão e reduz a precisao em 20
effRefletir = Efeito("refletir","positivo",40) #reflete parte do dano tomado de volta
effDormir = Efeito("dormir","negativo",10) #enquanto estiver dormindo perde o turno
effCorrupcao = Efeito("corrupcao","positivo",40) #aumenta todos atributos em 30, porem perde 20% do HP a cada turno
effSalvacao = Efeito("salvacao","positivo",60) #cura 50%, reduz todos atributos em 20

#instancia de tecnicas

#tecnicas de alinhamento
tecInspirar = Tecnica("inspirar","polar","yang","passivaPositiva","a cada turno, aumenta um atributo aleatório durante um turno",40,0,-10,100,effInspiracao)
tecLoucura = Tecnica("loucura","polar","yin","passivaNegativa","a cada turno, reduz um atributo aleatório do inimigo durante um turno",40,0,-20,100,effInsanidade)

#tecnicas de elemento
tecHellfire = Tecnica("hellfire","elemental","fogo","ofensivaPura","o fogo infernal da muito dano, porém é fácil de esquivar",20,40,-50,0,None)
tecCura = Tecnica("cura","elemental","agua","passivaPositiva","cura um pouco de HP",30,0,-10,0,None)
tecLullaby = Tecnica("lullaby","elemental","vento","passivaNegativa","faz o inimigo dormir",30,0,-20,100,effDormir)
tecAbsorver = Tecnica("absorver","elemental","terra","ofensivaPura","absorve um pouco do dano dado no inimigo",20,10,-10,0,None)

#tecnicas de emblema
tecEncontrao = Tecnica("encontrão","emblematica","espada","ofensivaPura","lança o seu corpo contra o inimigo, recebendo dano de volta",20,0,-10,0,None)
tecEspelho = Tecnica("espelho","emblematica","escudo","passivaPositiva","aplica um escudo que reflete o dano",40,0,-20,0,effRefletir)

#tecnicas unicas

#orbs elementais (yang espada)
tecSuperNova = Tecnica("supernova","unica","yang_espada_fogo","ofensivaPura","uma explosão de dano massivo, porém de alto custo",95,100,-20,0,None)

#golens
tecQueimar = Tecnica("queimar","unica","yang_escudo_fogo","passivaNegativa","queima um pouco do SP do inimigo",20,0,-10,0,None)

#instancia de elementos
fogo = Elemento("fogo",10,5,-10,-5,10,-10,tecHellfire,"cheia","/fogoIcone.png")
agua = Elemento("agua",-5,-10,10,5,-10,10,tecCura,"nova","/fogoIcone.png")
vento = Elemento("vento",-10,-5,5,10,10,-10,tecLullaby,"crescente","/fogoIcone.png")
terra = Elemento("terra",5,10,-5,-10,-10,10,tecAbsorver,"minguante","/fogoIcone.png")

#instancia de alinhamento
yin = Alinhamento("yin",-5,5,-5,5,-20,20,tecLoucura,"noite","/solIcone.png")
yang = Alinhamento("yang",5,-5,5,-5,20,-20,tecInspirar,"dia","/solIcone.png")

#instancia de emblemas
espada = Emblema("espada",10,-10,10,-10,-20,20,tecEncontrao,"/espadaIcone.png")
escudo = Emblema("escudo",-10,10,-10,10,20,-20,tecEspelho,"/espadaIcone.png")

#instancia astras

#orbs
astIgni = Astra("Igni","/fuegoFatuo.ttf",(255,0,0),"/orbFogo.png",fogo,yang,espada)