#aqui ficarão localizadas as classes de interface, no momento temos as seguintes:
#Regiao: uma regiao da tela, visualmente visivel
#subRegiao: uma regiao da tela, visualmente visivel, que está dentro de outra região
#texto: função para geração de texto e seleção de fontes e seus atributos

from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *

class Regiao(object):

    #classe que define uma região visivel na tela

    #atributos

    nome = "" #um nome para região (OPICIONAL)
    base = "" #a base é uma imagem padrão geralmente utilizada para definir a borda e outros detalhes (OPICIONAL)
    corFundo = (0,0,0) #é a cor de fundo caso não exista nenhuma base na região (OPICIONAL)
    # largura = 0 #a largura da região
    # altura = 0 #a altura da regiao
    # x = 0 #a posição x da região
    # y = 0 #a posição y da região
    fundo = "" #um fundo para a região, esse fundo fica sobre a base, util quando existe uma borda e um fundo variavel
    # fundoX = 0 #a posição x do fundo em relação a região
    # fundoY = 0 #a posição y do fundo em relação a região

    #enderecos
    sprites = "../assets/sprites"
    interface = sprites + "/interface"

    #metodos

    def __init__(self,intX,intY):

        self.x = intX
        self.y = intY

    #>get_set

    def setNome(self, stringNome):

        self.nome = str(stringNome)

    def getNome(self):

        return self.nome

    def setBase(self,spriteBase):

        "o argumento deve ser o endereço do sprite, para facilitar o endereço deve começar a partir da pasta interface"

        self.base = Sprite(self.interface + spriteBase)

    def getBase(self):

        return self.base

    def setCorFundo(self,rgbCor):

        self.corFundo = Color(rgbCor)

    def getCorFundo(self):

        return self.corFundo

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
        self.base.x = self.x

    def getX(self):

        return self.x

    def setY(self,intY):

        self.y = int(intY)
        self.base.y = self.y

    def getY(self):

        return self.y

    def setFundo(self,spriteFundo,intX,intY):

        "o argumento deve ser o endereço do sprite, para facilitar o endereço deve começar a partir da pasta interface"

        self.fundo = Sprite(self.interface + spriteFundo)
        self.fundo.x = self.x + int(intX)
        self.fundo.y = self.y + int(intY)

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

    def mover(self,intX,intY):

        "move a regiao para outra posicao"

        self.x = intX
        self.y = intY

    def desenhaRegiao(self):

        self.base.draw()
        self.fundo.draw()