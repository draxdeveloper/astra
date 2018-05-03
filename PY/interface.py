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

    #região imagem do inimigo

    rImagemInimigo = Sprite("/home/mimi/astra/trunk/assets/sprites/interface/combate/regiaoImagemInimigo.png")

    rImagemInimigoPosX = 0  # pos X da região imagem do inimigo
    rImagemInimigoPosY = 0  # pos Y da região imagem do inimigo

    rImagemInimigo.x = rImagemInimigoPosX
    rImagemInimigo.y = rImagemInimigoPosY

    #astra inimigo, aqui são colocadas as questão de interface do inimigo, o funcionamento fica em outro script

    inimigo = Sprite("/home/mimi/astra/trunk/assets/sprites/astras/orbFogo360.png")

    inimigoPosX = (rImagemInimigo.width/4)
    inimigoPosY = (rImagemInimigo.height/4)*2
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
        inimigo.draw()
        janela.update()

main()