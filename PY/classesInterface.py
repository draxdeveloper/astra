#aqui ficarão localizadas as classes de interface, no momento temos as seguintes:
#Regiao: uma regiao da tela, visualmente visivel
#Area: uma regiao da tela, visualmente visivel, que está dentro de outra região
#Texto: classe para geração de texto e seleção de fontes e seus atributos
#Menu: classe que gera menus
#Ancorar e aninhar. Funções gerais que servem para posicionar elementos na tela

from pygame.font import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *

listaSelecionavel = {} #lista de todos os objetos selecionaveis
listaFontes = {} #lista de todas as fontes

# enderecos
sprites = "../assets/sprites"
interface = sprites + "/interface"
texto = sprites + "/texto"

class Regiao(object):

    #classe que define uma região visivel na tela

    #atributos

    # nome = "" #um nome para região (OPICIONAL), adicionar futuramente
    borda = "" #uma imagem padrão geralmente utilizada para definir a borda e outros detalhes
    tamanhoBorda = (0,0) #a espessura da borda horizontal e vertical
    fundo = "" #um fundo para a região, esse fundo fica sobre a base, util quando existe uma borda e um fundo variavel
    selecionavel = False #determina se o cursor pode se posicionar em certa região da tela
    ordemSelecao = 0 #determina a ordem que o cursor ira passar, nem sempre é exata devido a sub-menus, somente se selecionavel for True
    # corFundo = (0,0,0) #é a cor de fundo caso não exista nenhuma base na região
    width = 0 #a largura da região
    height = 0 #a altura da regiao
    x = 0 #a posição x da região
    y = 0 #a posição y da região

    # fundoX = 0 #a posição x do fundo em relação a região
    # fundoY = 0 #a posição y do fundo em relação a região



    #metodos

    def __init__(self,intX,intY,window,spriteBorda, intTamanhoBordaX, intTamanhoBordaY, regiaoHorizontal = "tela", strTipoAncoraHorizontal = "direita", regiaoVertical = "tela", strTipoAncoraVertical = "abaixo", spriteFundo="", intFundoX = 0, intFundoY = 0, boolSelecionavel = False, intOrdemSelecao = -1 ):

        "x e y é o deslocamento em relação a ancora, invertido no caso de esquerda e acima. Dados de aconramento ver função ancorarNaRegiao"

        self.setBorda(spriteBorda,intTamanhoBordaX,intTamanhoBordaY)
        ancorar(self.getBorda(),window,regiaoHorizontal,strTipoAncoraHorizontal,regiaoVertical,strTipoAncoraVertical)
        self.getBorda().x += intX
        self.getBorda().y += intY
        self.selecionavel = boolSelecionavel
        self.ordemSelecao = intOrdemSelecao

        self.x = self.getBorda().x
        self.y = self.getBorda().y
        self.width = self.getBorda().width
        self.height = self.getBorda().height

        if(spriteFundo != ""):

            self.setFundo(spriteFundo, intFundoX, intFundoY)

        if(self.selecionavel == True):

            listaSelecionavel[self.ordemSelecao] = self

    #>get_set

    def setNome(self, stringNome):

        self.nome = str(stringNome)

    def getNome(self):

        return self.nome

    def setBorda(self,spriteBase,tamX,tamY):

        "o argumento deve ser o endereço do sprite, para facilitar o endereço deve começar a partir da pasta interface"

        self.borda = Sprite(interface + spriteBase)
        self.tamanhoBorda = (tamX,tamY)

    def getBorda(self):

        return self.borda

    def setTamanhoBorda(self,tamX,tamY):

        self.tamanhoBorda = (tamX,tamY)

    def setTamanhoBordaX(self,tamX):

        self.tamanhoBorda[0] = tamX

    def setTamanhoBordaY(self,tamY):

        self.tamanhoBorda[1] = tamY

    def getTamanhoBorda(self):

        return self.tamanhoBorda

    def getTamanhoBordaX(self):

        return self.tamanhoBorda[0]

    def getTamanhoBordaY(self):

        return self.tamanhoBorda[1]

    def setCorFundo(self,rgbCor):

        self.corFundo = Color(rgbCor)

    def getCorFundo(self):

        return self.corFundo

    def setSelecionavel(self,boolSelecionavel):

        self.selecionavel = boolSelecionavel

    def getSelecionavel(self):

        return self.selecionavel

    def setOrdemSelecao(self,intOrdem):

        self.ordemSelecao = intOrdem

    def getOrdemSelecao(self):

        return  self.ordemSelecao

    def setLargura(self,intLargura):

        self.width = intLargura
        self.getBorda().width = int(intLargura)

    def getLargura(self):

        return self.width

    def setAltura(self,intAltura):

        self.height = intAltura
        self.getBorda().height = int(intAltura)

    def getAltura(self):

        return self.height

    def setX(self,intX):

        self.x = intX
        self.borda.x = intX

    def getX(self):

        return self.x

    def setY(self,intY):

        self.y = intY
        self.borda.y = self.getBorda().y

    def getY(self):

        return self.y


    def setFundo(self,spriteFundo,intX,intY):

        "o argumento deve ser o endereço do sprite, para facilitar o endereço deve começar a partir da pasta interface"

        self.fundo = Sprite(interface + spriteFundo)
        self.fundo.x = self.borda.x + self.tamanhoBorda[0] + int(intX)
        self.fundo.y = self.borda.y + self.tamanhoBorda[1] + int(intY)

    def getFundo(self):

        return self.fundo

    def setFundoX(self,intFundoX):

        self.fundo.x = int(intFundoX)

    def getFundoX(self):

        return self.fundoX

    def setFundoY(self,intFundoY):

        self.fundo.y = int(intFundoY)

    def getFundoY(self):

        return self.fundoY


    #outros metodos

    def moverRegiao(self,intX,intY):

        "desloca a regiao"

        self.getBorda().x += int(intX)
        self.getBorda().y += int(intY)

    def moveFundo(self,intX,intY):

        "desloca o fundo"

        self.getFundo().x += int(intX)
        self.getFundo().y += int(intY)

    def desenhaRegiao(self):

        self.borda.draw()
        if(self.fundo != ""):
            self.fundo.draw()

    # def ancorarNaRegiao(self,objeto,window,regiaoHorizontal = "tela", strTipoAncoraHorizontal = "direita", regiaoVertical = "tela", strTipoAncoraVertical = "abaixo"):
    #
    #     "ancora o objeto (que deve ter coordenadas existentes) em relação a uma região, o tipo de ancora horizontal pode ser (direita),(esquerda) e a vertical pode ser (acima) ou (abaixo)"
    #
    #     if(regiaoHorizontal == "tela"):
    #
    #         if(strTipoAncoraHorizontal == "direita"):
    #
    #             objeto.x = 0
    #
    #         else:
    #
    #             objeto.x = window.width - objeto.width
    #
    #     else:
    #
    #         if (strTipoAncoraHorizontal == "direita"):
    #
    #             objeto.x = regiaoHorizontal.getBorda().x + regiaoHorizontal.getBorda().width
    #
    #         else:
    #
    #             objeto.x = regiaoHorizontal.getBorda().x - objeto.width
    #
    #     if (regiaoVertical == "tela"):
    #
    #         if (strTipoAncoraVertical == "abaixo"):
    #
    #             objeto.y = 0
    #
    #         else:
    #
    #             objeto.y = window.height - objeto.height
    #
    #     else:
    #
    #         if (strTipoAncoraVertical == "abaixo"):
    #
    #             objeto.y = regiaoVertical.getBorda().y + regiaoVertical.getBorda().height
    #
    #         else:
    #
    #             objeto.y = regiaoVertical.getBorda().y - objeto.height

class Pilha(object):

    "classe que cria uma pilha vertical de outros objetos posicionaveis, nescessariamente precisa de uma lista desses objetos"

    pilha = ()
    x = 0
    y = 0
    espacamento = 0
    alinhamento = ""
    selecionavel = ""
    ordemSelecao = 0


    def __init__(self,window,listaObjetos,intEspacamento=0,strAncora = "tela",strAlinhamento = "esquerda",bollSelecionavel = "False"):

        #intEspacamento é o espaço entre os itens da pilha

        self.selecionavel = bollSelecionavel
        janela = window

        self.pilha = listaObjetos

        if (self.selecionavel == True):

            # listaSelecionavel = {}

            for i in range(len(self.pilha)):

                listaSelecionavel[i] = self.pilha[i]

        self.espacamento = intEspacamento
        self.empilhar(janela,strAlinhamento,strAncora)

    def atualizaPilha(self,window,novaPilha,intEspacamento=0,strAncora = "tela",strAlinhamento = "esquerda",bollSelecionavel = "False"):

        janela = window

        self.pilha = ()

        self.selecionavel = bollSelecionavel

        self.pilha = novaPilha

        for i in self.pilha:

            i.x = 0
            i.y = 0

        if (self.selecionavel == True):

            for i in range(len(self.pilha)):
                listaSelecionavel[i] = self.pilha[i]

        self.espacamento = intEspacamento
        self.empilhar(janela,strAlinhamento,strAncora)

    def empilhar(self,window,strAlinhamento = "esquerda",strAncora = "tela"):

        janela = window

        self.alinhamento = strAlinhamento

        ancorar(self.pilha[0], janela, strAncora, "centro", strAncora, "abaixo") #gambiarra, corrigir depois

        for i in range(1,(len(self.pilha))):

            self.pilha[i].y += self.pilha[i-1].y + self.pilha[i-1].height + self.espacamento

            if(self.alinhamento == "esquerda"):

                self.pilha[i].x = self.pilha[i-1].x

            elif(self.alinhamento == "direita"):

                self.pilha[i].x = self.pilha[i-1].x - (self.pilha[i].width - self.pilha[i-1].width)

            elif(self.alinhamento == "centro"):

                self.pilha[i].x = (self.pilha[i-1].x + self.pilha[i-1].width/2) - self.pilha[i].width/2



    def aninharPilha(self,window,regiao, strTipoAlinhamentoHorizontal = "esquerda", strTipoAlinhamentoVertical = "acima",intDeslocamentoX = 0,intDeslocamentoY = 0):

        #aninha o primeiro elemento na regiao

        aninhar(self.pilha[0],window,regiao,strTipoAlinhamentoHorizontal,strTipoAlinhamentoVertical,intDeslocamentoX,intDeslocamentoY)
        self.empilhar()

    def desenhaPilha(self):

        for i in range(len(self.pilha)):

            self.pilha[i].draw()

# class Selecionavel(object):
#
#     "torna um objeto como um Sprite selecionavel por um cursor"
#
#     selecionavel = True
#     ordemSelecao = -1
#     x = 0
#     y = 0
#     width = 0
#     height = 0
#     sprite = ""
#
#     def __init__(self,objeto,intOrdemSelecao):
#
#         self.x = objeto.x
#         self.y = objeto.y
#         self.width = objeto.width
#         self.height = objeto.height
#         self.sprite = objeto
#
#         self.ordemSelecao = intOrdemSelecao
#
#         listaSelecionavel[self.ordemSelecao] = self
#
#     def mudaOrdem(self,intOrdemSelecao):
#
#         pass
#
#     def desativaSelecao(self):
#
#         pass
#
#     def ativaSelecao(self):
#
#         pass
#
#     def draw(self):
#
#         self.sprite.draw()

class BlocoPadraoSprite(object):
    "gera um bloco x por y usando o mesmo sprite"

    sprite = "" #o endereco da imagem de base do sprite
    linhas = 0 #total de linhas do bloco
    colunas = 0 #total de colunas do bloco
    espacamentoX = 0 #espacamento vertical entre os elementos
    espacamentoY = 0 #espacamento horizontal entre os elementos
    listaElementos = []
    primeiroElementoX = "" #primeiro elemento do bloco
    ultimoElementoX  = "" #ultimo elemento do bloco
    primeiroElementoY = ""
    ultimoElementoY = ""
    janela = ""

    def __init__(self,window,strSprite,intLinhas,intColunas,intEspacamentoX = 0,intEspacamentoY=0,intPosX=0,intPosY=0):

        #inicializa

        self.janela = window
        self.sprite = strSprite
        self.linhas = intLinhas
        self.colunas = intColunas
        self.espacamentoX = intEspacamentoX
        self.espacamentoY = intEspacamentoY

        for i in range(self.linhas):

            self.listaElementos.append([])

            for j in range(self.colunas):

                self.listaElementos[i].append(Sprite(self.sprite))

                if(i>0):

                    self.listaElementos[i][j].y += self.listaElementos[i-1][j].y + self.listaElementos[i-1][j].height + self.espacamentoY

                else:

                    self.listaElementos[i][j].y = intPosY

                if(j>0):

                    self.listaElementos[i][j].x += self.listaElementos[i][j-1].x + self.listaElementos[i][j-1].width + self.espacamentoX

                else:

                    self.listaElementos[i][j].x = intPosX

        self.primeiroElementoX = self.listaElementos[0][0]
        self.primeiroElementoY = self.listaElementos[0][0]
        self.ultimoElementoX = self.listaElementos[intLinhas-1][intColunas-1]
        self.ultimoElementoY = self.listaElementos[intLinhas - 1][intColunas - 1]

    def moveBloco(self,intX,intY):
        "move o bloco em x e y"

        if(self.getTotalItens() > 0):

            for i in range(len(self.listaElementos)):

                for j in range(len(self.listaElementos[i])):

                    self.listaElementos[i][j].x += intX * self.janela.delta_time()
                    self.listaElementos[i][j].y += intY * self.janela.delta_time()

    def testaColisao(self,objeto):
        "testa colisoes com os elementos do bloco"

        if (self.getTotalItens() > 0):

            tuplaR = ()



            for i in range(len(self.listaElementos)):

                for j in range(len(self.listaElementos[i])):

                    #testa eixo X
                    if((objeto.x >= self.listaElementos[i][j].x) and ((objeto.x) <= (self.listaElementos[i][j].x+self.listaElementos[i][j].width))):

                        if((objeto.y >= self.listaElementos[i][j].y) and ((objeto.y) <= (self.listaElementos[i][j].y + self.listaElementos[i][j].height))):

                            tuplaR = (i,self.listaElementos[i][j])

                        elif (((objeto.y+objeto.height) >= self.listaElementos[i][j].y) and ((objeto.y+objeto.height) <= (self.listaElementos[i][j].y + self.listaElementos[i][j].height))):

                            tuplaR = (i,self.listaElementos[i][j])

                    elif(((objeto.x+objeto.width) >= self.listaElementos[i][j].x) and ((objeto.x+objeto.width) <= (self.listaElementos[i][j].x + self.listaElementos[i][j].width))):

                        if(((objeto.y) >= self.listaElementos[i][j].y) and ((objeto.y) <= (self.listaElementos[i][j].y + self.listaElementos[i][j].height))):

                            tuplaR = (i,self.listaElementos[i][j])

                        elif (((objeto.y+objeto.height) >= self.listaElementos[i][j].y) and ((objeto.y+objeto.height) <= (self.listaElementos[i][j].y + self.listaElementos[i][j].height))):

                            tuplaR = (i,self.listaElementos[i][j])

            return tuplaR

    def removeAlien(self,alien):

        if (self.getTotalItens() > 0):

            removido = False

            if(alien != ()):

                if(removido==False):
                    # print(alien)
                    self.listaElementos[alien[0]].remove(alien[1])
                    removido = True

                self.atualizaBloco()

            return alien

    def atualizaBloco(self):
        "atualiza primeiro e ultimo elemento do bloco"

        for k in range(len(self.listaElementos)):

            if((k+1) <= len(self.listaElementos)):

                if(len(self.listaElementos[k]) <= 0):

                    self.listaElementos.pop(k)
                    k -= 1

        if(self.getTotalItens() > 0):

            self.primeiroElementoX = self.listaElementos[0][0]
            self.primeiroElementoY = self.listaElementos[0][0]
            self.ultimoElementoX = self.listaElementos[0][0]
            self.ultimoElementoY = self.listaElementos[0][0]

            for i in range(len(self.listaElementos)):

                for j in range(len(self.listaElementos[i])):

                    if(self.listaElementos[i][j].x < self.primeiroElementoX.x):

                        self.primeiroElementoX = self.listaElementos[i][j]

                    elif(self.listaElementos[i][j].x > self.ultimoElementoX.x):

                        self.ultimoElementoX = self.listaElementos[i][j]

                    if(self.listaElementos[i][j].y < self.primeiroElementoY.y):

                        self.primeiroElementoY = self.listaElementos[i][j]

                    elif(self.listaElementos[i][j].y > self.ultimoElementoY.y):

                        self.ultimoElementoY = self.listaElementos[i][j]



    def desenhaBloco(self):

        if(len(self.listaElementos) > 0):

            for i in range(len(self.listaElementos)):

                for j in range(len(self.listaElementos[i])):

                    self.listaElementos[i][j].draw()

    def getPrimeiroElementoX(self):

        return self.primeiroElementoX

    def getPrimeiroElementoY(self):

        return self.primeiroElementoY

    def getUltimoElementoX(self):

        return self.ultimoElementoX

    def getUltimoElementoY(self):

        return self.ultimoElementoY

    def getTotalItens(self):

        total = 0

        if(len(self.listaElementos) <= 0):

            total = 0

        else:

            for i in range(len(self.listaElementos)):

                total += len(self.listaElementos[i])

        return total

class Cursor(object):

    spriteCursorAtual = ""
    spriteCursorNormal = ""
    spriteCursorEspelhado = ""
    posAtual = -1
    janela = ""

    def __init__(self,window,spriteCursorNormal,spriteCursorEspepelhado,intPosAtual = 0):

        self.spriteCursorNormal = Sprite(interface + spriteCursorNormal)
        self.spriteCursorEspelhado = Sprite(interface + spriteCursorEspepelhado)
        self.spriteCursorAtual = self.spriteCursorNormal
        self.posAtual = intPosAtual
        janela = window

    #get_set

    def setSpriteCursor(self,spriteNovoCursor):

        self.spriteCursor = spriteNovoCursor

    def getSpriteCursor(self):

        return self.spriteCursor

    def getPosX(self):

        self.spriteCursor.x

    def getPosY(self):

        self.spriteCursor.y

    def getPosAtual(self):

        return self.posAtual


    def moveCursor(self,janela,intNovaPos):

        # print(listaSelecionavel)

        self.posAtual = intNovaPos

        referencia = listaSelecionavel.get(intNovaPos)

        self.spriteCursorAtual = self.spriteCursorNormal
        self.spriteCursorAtual.x = referencia.x + referencia.width
        self.spriteCursorAtual.y = referencia.y + (referencia.height/2) - (self.spriteCursorAtual.height/2)

        if(self.spriteCursorAtual.x > (janela.width - self.spriteCursorAtual.width)): #fazer função que espelhe o cursor

            self.spriteCursorAtual = self.spriteCursorEspelhado
            self.spriteCursorAtual.x = referencia.x - self.spriteCursorAtual.width


    def desenhaCursor(self):

        self.spriteCursorAtual.draw()

class Contador(object):

    "classe que gera um contador"

    ativo = False
    # encerrado = False
    tempoLimite = 0
    tempoDecorrido = 0
    janela = ""

    def __init__(self,window):

        self.janela = window

    def getAtivo(self):

        return self.ativo

    def getEncerrado(self):

        return self.encerrado

    def ativar(self,intTempo):

        # self.encerrado = False
        self.ativo = True
        self.tempoLimite = intTempo

    def desativar(self):

        self.ativo = False

    def atualizar(self):

        if(self.ativo == True):

            self.tempoDecorrido += self.janela.delta_time()
            if(self.tempoDecorrido >= self.tempoLimite):
                # self.encerrado = True
                self.tempoDecorrido = 0
                self.ativo = False

def aninhar(objeto,window, regiao="tela", strTipoAlinhamentoHorizontal = "esquerda", strTipoAlinhamentoVertical = "acima",intDeslocamentoX = 0,intDeslocamentoY = 0):

    "similar a ancorar, mas ancora internamente, os ancoramento verticais podem ser esquerda, direita e centro e os verticais acima,abaixo e centro"

    if(regiao == "tela"):

        if (strTipoAlinhamentoHorizontal == "esquerda"):

            objeto.x =  intDeslocamentoX

        elif (strTipoAlinhamentoHorizontal == "direita"):

            objeto.x = (window.width - objeto.width - intDeslocamentoX)

        else:

            objeto.x = (window.width / 2) - (objeto.width / 2) + intDeslocamentoX

        if (strTipoAlinhamentoVertical == "acima"):

            objeto.y = intDeslocamentoY

        elif (strTipoAlinhamentoVertical == "abaixo"):

            objeto.y = (window.height) - objeto.height - intDeslocamentoY

        else:

            objeto.y = (window.height / 2) - (objeto.height / 2) + intDeslocamentoY

    else:

        if (strTipoAlinhamentoHorizontal == "esquerda"):

            objeto.x = regiao.getBorda().x + regiao.getTamanhoBordaX() + intDeslocamentoX

        elif(strTipoAlinhamentoHorizontal == "direita"):

            objeto.x = (regiao.getBorda().x + regiao.getBorda().width) - regiao.getTamanhoBordaX() - objeto.width - intDeslocamentoX

        else:

            objeto.x = regiao.getBorda().x + (regiao.getBorda().width/2) - (objeto.width/2) + intDeslocamentoX

        if (strTipoAlinhamentoVertical == "acima"):

            objeto.y = regiao.getBorda().y + regiao.getTamanhoBordaY() + intDeslocamentoY

        elif (strTipoAlinhamentoVertical == "abaixo"):

            objeto.y = (regiao.getBorda().y + regiao.getBorda().height) - regiao.getTamanhoBordaY() - objeto.height - intDeslocamentoY

        else:

            objeto.y = regiao.getBorda().y + (regiao.getBorda().height/2) - (objeto.height/2) + intDeslocamentoY

def ancorar(objeto,window,ancoraHorizontal = "tela", strTipoAncoraHorizontal = "direita", ancoraVertical = "tela", strTipoAncoraVertical = "abaixo", intDeslocamentoX = 0, intDeslocamentoY = 0):

    "ancora o objeto (que deve ter coordenadas existentes) em relação a uma região, o tipo de ancora horizontal pode ser (direita),(esquerda) e a vertical pode ser (acima) ou (abaixo)"

    if(ancoraHorizontal == "tela"):

        if(strTipoAncoraHorizontal == "direita"):

            objeto.x = 0 + intDeslocamentoX

        elif(strTipoAncoraHorizontal == "esquerda"):

            objeto.x = window.width - objeto.width + intDeslocamentoX

        else:

            objeto.x = (window.width/2) - (objeto.width/2) + intDeslocamentoX


    else:

        if(strTipoAncoraHorizontal == "direita"):

            objeto.x = ancoraHorizontal.x + ancoraHorizontal.width + intDeslocamentoX

        elif(strTipoAncoraHorizontal == "esquerda"):

            objeto.x = ancoraHorizontal.x - objeto.width + intDeslocamentoX

        else:

            objeto.x = (ancoraHorizontal.x + (ancoraHorizontal.width/2)) - (objeto.width/2) + intDeslocamentoX

    if (ancoraVertical == "tela"):

        if (strTipoAncoraVertical == "abaixo"):

            objeto.y = 0 + intDeslocamentoY

        elif(strTipoAncoraVertical == "acima"):

            objeto.y = window.height - objeto.height + intDeslocamentoY

        else:

            objeto.y = (window.height/2) - (objeto.height/2) +intDeslocamentoY

    else:

        if (strTipoAncoraVertical == "abaixo"):

            objeto.y = ancoraVertical.y + ancoraVertical.height + intDeslocamentoY

        elif(strTipoAncoraVertical == "acima"):

            objeto.y = ancoraVertical.y - objeto.height + intDeslocamentoY

        else:

            objeto.y = ancoraVertical.y + (ancoraVertical.height/2) - (objeto.height/2) + intDeslocamentoY