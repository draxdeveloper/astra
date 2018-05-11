#aqui ficarão localizadas as classes de interface, no momento temos as seguintes:
#Regiao: uma regiao da tela, visualmente visivel
#subRegiao: uma regiao da tela, visualmente visivel, que está dentro de outra região
#texto: função para geração de texto e seleção de fontes e seus atributos

from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *

listaSelecionavel = {} #lista de todos as classes selecionaveis

# enderecos
sprites = "../assets/sprites"
interface = sprites + "/interface"

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
    # largura = 0 #a largura da região
    # altura = 0 #a altura da regiao
    # x = 0 #a posição x da região
    # y = 0 #a posição y da região

    # fundoX = 0 #a posição x do fundo em relação a região
    # fundoY = 0 #a posição y do fundo em relação a região



    #metodos

    def __init__(self,intX,intY,window,spriteBorda, intTamanhoBordaX, intTamanhoBordaY, regiaoHorizontal = "tela", strTipoAncoraHorizontal = "direita", regiaoVertical = "tela", strTipoAncoraVertical = "abaixo", spriteFundo="", intFundoX = 0, intFundoY = 0, boolSelecionavel = False, intOrdemSelecao = -1 ):

        "x e y é o deslocamento em relação a ancora, invertido no caso de esquerda e acima. Dados de aconramento ver função ancorarNaRegiao"

        self.setBorda(spriteBorda,intTamanhoBordaX,intTamanhoBordaY)
        self.ancorarNaRegiao(self.getBorda(),window,regiaoHorizontal,strTipoAncoraHorizontal,regiaoVertical,strTipoAncoraVertical)
        self.getBorda().x += intX
        self.getBorda().y += intY
        self.selecionavel = boolSelecionavel
        self.ordemSelecao = intOrdemSelecao

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

    # def setLargura(self,intLargura):
    #
    #     self.largura = int(intLargura)

    # def getLargura(self):
    #
    #     return self.largura

    # def setAltura(self,intAltura):
    #
    #     self.altura = int(intAltura)

    # def getAltura(self):
    #
    #     return self.altura

    def setX(self,intX):

        self.x = int(intX)
        self.borda.x = self.x

    def getX(self):

        return self.x

    def setY(self,intY):

        self.y = int(intY)
        self.borda.y = self.y

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

    def ancorarNaRegiao(self,objeto,window,regiaoHorizontal = "tela", strTipoAncoraHorizontal = "direita", regiaoVertical = "tela", strTipoAncoraVertical = "abaixo"):

        "ancora o objeto (que deve ter coordenadas existentes) em relação a uma região, o tipo de ancora horizontal pode ser (direita),(esquerda) e a vertical pode ser (acima) ou (abaixo)"

        if(regiaoHorizontal == "tela"):

            if(strTipoAncoraHorizontal == "direita"):

                objeto.x = 0

            else:

                objeto.x = window.width - objeto.width

        else:

            if (strTipoAncoraHorizontal == "direita"):

                objeto.x = regiaoHorizontal.getBorda().x + regiaoHorizontal.getBorda().width

            else:

                objeto.x = regiaoHorizontal.getBorda().x - objeto.width

        if (regiaoVertical == "tela"):

            if (strTipoAncoraVertical == "abaixo"):

                objeto.y = 0

            else:

                objeto.y = window.height - objeto.height

        else:

            if (strTipoAncoraVertical == "abaixo"):

                objeto.y = regiaoVertical.getBorda().y + regiaoVertical.getBorda().height

            else:

                objeto.x = regiaoVertical.getBorda().y - objeto.height

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

        self.posAtual = intNovaPos

        referencia = listaSelecionavel.get(intNovaPos)

        self.spriteCursorAtual = self.spriteCursorNormal
        self.spriteCursorAtual.x = referencia.getBorda().x + referencia.getBorda().width
        self.spriteCursorAtual.y = referencia.getBorda().y + (referencia.getBorda().height/2)

        if(self.spriteCursorAtual.x > (janela.width - self.spriteCursorAtual.width)): #fazer função que espelhe o cursor

            self.spriteCursorAtual = self.spriteCursorEspelhado
            self.spriteCursorAtual.x = referencia.getBorda().x - self.spriteCursorAtual.width


    def desenhaCursor(self):

        self.spriteCursorAtual.draw()



def aninharNaRegiao(objeto,regiao, strTipoAlinhamentoHorizontal = "esquerda", strTipoAlinhamentoVertical = "acima",intDeslocamentoX = 0,intDeslocamentoY = 0):

    "similar a ancorar, mas ancora internamente, os ancoramento verticais podem ser esquerda, direita e centro e os verticais acima,abaixo e centro"


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