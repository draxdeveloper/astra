import os

from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *


def main():

    #janela

    janelaLargura = int((1920/5) * 3) #3/5 da resolução 1920X1080
    janelaAltura = int((1080/5) * 3) #3/5 da resolução 1920X1080

    janela = Window(janelaLargura,janelaAltura)

    janelaNome = "astra"
    janelaCorFundo = (0,0,0)

    janela.set_title(janelaNome)
    janela.set_background_color(janelaCorFundo)

    #texto padrão
    textoPadraoFonte = "Sans"
    textoPadraoTamanho = 70
    textoPadraoCor = (0, 255, 0)
    textoPadraoBold = True
    textoPadraoItalic = True

    #região imagem do inimigo

    rImagemInimigo = Sprite("../assets/sprites/interface/combate/regiaoImagemInimigo.png")

    rImagemInimigoPosX = 0  # pos X da região imagem do inimigo
    rImagemInimigoPosY = 0  # pos Y da região imagem do inimigo

    rImagemInimigo.x = rImagemInimigoPosX
    rImagemInimigo.y = rImagemInimigoPosY

    #regiao nome do astra inimigo

    rNomeInimigo = Sprite("../assets/sprites/interface/combate/nomeAstraInimigo.png")

    rNomeInimigoposX = rImagemInimigo.width
    rNomeInimigoPosY = 0

    rNomeInimigo.x = rNomeInimigoposX
    rNomeInimigo.y = rNomeInimigoPosY

    nomeInimigo = "Igni"
    nomeInimigoPosX = int(rNomeInimigo.x + (rNomeInimigo.width/3))
    nomeInimigoPosY = int(rNomeInimigo.height/4)

    # região dos simbolos do inimigo

    rSimboloInimigo = Sprite("../assets/sprites/interface/combate/rSimboloAstraInimigo.png")

    rSimboloInimigoPosX = rImagemInimigo.width  # pos X da região imagem do inimigo
    rSimboloInimigoPosY = rNomeInimigo.height  # pos Y da região imagem do inimigo

    rSimboloInimigo.x = rSimboloInimigoPosX
    rSimboloInimigo.y = rSimboloInimigoPosY

    #astra inimigo, aqui são colocadas as questão de interface do inimigo, o funcionamento fica em outro script

    inimigo = Sprite("/home/mimi/astra/trunk/assets/sprites/astras/orbFogo360.png")

    inimigoPosX = int((rImagemInimigo.width/4))
    inimigoPosY = int((rImagemInimigo.height/4)*2)
    inimigo.x = inimigoPosX
    inimigo.y = inimigoPosY
    print(inimigoPosX)

    #controle

    teclado = Window.get_keyboard()

    sair = "esc"

    #game loop

    while(teclado.key_pressed(sair) == False):

        janela.set_background_color(janelaCorFundo)
        rImagemInimigo.draw()
        rNomeInimigo.draw()
        rSimboloInimigo.draw()
        Window.draw_text(janela,nomeInimigo,nomeInimigoPosX,nomeInimigoPosY,textoPadraoTamanho,textoPadraoCor,textoPadraoFonte,textoPadraoBold,textoPadraoItalic)
        inimigo.draw()
        janela.update()

main()