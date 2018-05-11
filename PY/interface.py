# import os

from classesInterface import *

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

    # região da imagem do inimigo

    rImagemInimigo = Regiao(0,0,janela,"/combate/rImagemInimigo.png",3,3,"tela","direita","tela","abaixo","/combate/fundoTeste.jpg")

    #astra inimigo, aqui são colocadas as questão de interface do inimigo, o funcionamento fica em outro script

    inimigo = Sprite("../assets/sprites/astras/orbFogo360.png")

    aninharNaRegiao(inimigo,rImagemInimigo,"centro","abaixo")

    #regiao nome do astra inimigo

    rNomeInimigo = Regiao(-3,0,janela,"/combate/rNomeAstraInimigo.png",3,3,rImagemInimigo,"direita","tela","abaixo")

    #nome do inimigo

    nomeInimigo = Sprite("../assets/sprites/interface/combate/nomeAstraIgni.png")

    aninharNaRegiao(nomeInimigo,rNomeInimigo,"centro","centro")

    # região dos simbolos do inimigo

    rSimboloInimigo = Regiao(-3,-3,janela,"/combate/rSimboloAstraInimigo.png",3,3,rImagemInimigo,"direita",rNomeInimigo,"abaixo")

    #simbolos do inimigo

    simboloElemento = Sprite("../assets/sprites/interface/combate/fogoIcone.png")
    simboloAlinhamento = Sprite("../assets/sprites/interface/combate/solIcone.png")
    simboloEmblema = Sprite("../assets/sprites/interface/combate/espadaIcone.png")

    aninharNaRegiao(simboloElemento,rSimboloInimigo,"esquerda","centro",simboloElemento.width/2)
    aninharNaRegiao(simboloAlinhamento,rSimboloInimigo,"esquerda","centro",simboloElemento.width*2.5)
    aninharNaRegiao(simboloEmblema,rSimboloInimigo,"esquerda","centro",simboloElemento.width*4.5)

    #região HP e SP do inimigo

    rHPInimigo = Regiao(-3,-3,janela,"/combate/rHPSP.png",3,3,rImagemInimigo,"direita",rSimboloInimigo,"abaixo")
    rSPInimigo = Regiao(0,-3, janela, "/combate/rHPSP.png", 3, 3, rHPInimigo, "direita", rSimboloInimigo, "abaixo")

    #HP e SP do inimigo

    hpInimigo = Sprite("../assets/sprites/interface/combate/hpInimigo.png")
    spInimigo = Sprite("../assets/sprites/interface/combate/spInimigo.png")

    aninharNaRegiao(hpInimigo,rHPInimigo,"centro,","centro")
    aninharNaRegiao(spInimigo, rSPInimigo, "centro,", "centro")

    #região de atributos do inimigo

    rAtributosInimigo = Regiao(-3,0,janela,"/combate/rAtributosInimigo.png",3,3,rImagemInimigo,"direita",rHPInimigo,"abaixo")

    #atributos do inimigo

    forInimigo = Sprite("../assets/sprites/interface/combate/forInimigo.png")
    evaInimigo = Sprite("../assets/sprites/interface/combate/evaInimigo.png")
    preInimigo = Sprite("../assets/sprites/interface/combate/preInimigo.png")
    vigInimigo = Sprite("../assets/sprites/interface/combate/vigInimigo.png")

    aninharNaRegiao(forInimigo,rAtributosInimigo,"esquerda","acima",10,10)
    aninharNaRegiao(evaInimigo,rAtributosInimigo,"direita","abaixo",10,10)
    aninharNaRegiao(preInimigo,rAtributosInimigo,"direita","acima",10,10)
    aninharNaRegiao(vigInimigo,rAtributosInimigo,"esquerda","abaixo",10,10)

    #regiao do texto principal
    rTextoPrincipal = Regiao(0,0,janela,"/combate/rTextoPrincipal.png",3,3,"tela","esquerda","tela","abaixo")

    #textoPrincipal

    #>posicionamento baseado em como ira funcionar as linhas

    totalLinhas = 2

    linha1 = Sprite("../assets/sprites/interface/combate/textoPrincipalL1.png")
    linha2 = Sprite("../assets/sprites/interface/combate/textoPrincipalL2.png")

    aninharNaRegiao(linha1,rTextoPrincipal,"esquerda","abaixo",5,linha1.height * (totalLinhas - 1) + 5)
    aninharNaRegiao(linha2,rTextoPrincipal,"esquerda","abaixo",5,linha1.height * (totalLinhas - 2) + 5)

    #região seleção de ataque
    rSelecaoAtaque = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,"tela","direita",rImagemInimigo,"abaixo","",0,0,True,0)
    rSelecaoAtaque.moverRegiao(0,rSelecaoAtaque.getBorda().height)

    #texto seleção de ataque
    textoAtaque = Sprite("../assets/sprites/interface/combate/textoSelecaoAtaque.png")
    aninharNaRegiao(textoAtaque,rSelecaoAtaque,"centro","centro")

    #regiao seleção de tecnica
    rSelecaoTecnica = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,"tela","direita",rSelecaoAtaque,"abaixo","",0,0,True,1)

    #texto seleção tecnica
    textoTecnica = Sprite("../assets/sprites/interface/combate/textoSelecaoTecnica.png")
    aninharNaRegiao(textoTecnica,rSelecaoTecnica,"centro","centro")

    #regiao selecao tecnica elemental
    rSelecaoElemental = Regiao(0,rSelecaoAtaque.getBorda().height,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoAtaque,"direita",rAtributosInimigo,"abaixo","",0,0,True,2)

    #texto tecnical elemental
    textoElemental = Sprite("../assets/sprites/interface/combate/textoElemental.png")
    aninharNaRegiao(textoElemental,rSelecaoElemental,"centro","centro")

    #cursor
    cursor = Cursor(janela,"/glove3.png","/glove3Espelhada.png")
    cursor.moveCursor(janela,0)

    #controle

    teclado = Window.get_keyboard()

    sair = "esc"
    selecaoAbaixo = "down"
    selecaoAcima = "up"

    #game loop

    while(teclado.key_pressed(sair) == False):

        if(teclado.key_pressed("down") or teclado.key_pressed("up")):

            if(cursor.getPosAtual() == 1):

                cursor.moveCursor(janela,0)

            else:

                cursor.moveCursor(janela,1)

        janela.set_background_color(janelaCorFundo)

        #draw regiões

        rImagemInimigo.desenhaRegiao()
        rNomeInimigo.desenhaRegiao()
        rSimboloInimigo.desenhaRegiao()
        rHPInimigo.desenhaRegiao()
        rSPInimigo.desenhaRegiao()
        rAtributosInimigo.desenhaRegiao()
        rTextoPrincipal.desenhaRegiao()
        rSelecaoAtaque.desenhaRegiao()
        rSelecaoTecnica.desenhaRegiao()
        rSelecaoElemental.desenhaRegiao()

        #draw sprites

        inimigo.draw()
        simboloElemento.draw()
        simboloAlinhamento.draw()
        simboloEmblema.draw()
        cursor.desenhaCursor()

        #draw textos

        nomeInimigo.draw()
        hpInimigo.draw()
        spInimigo.draw()
        forInimigo.draw()
        preInimigo.draw()
        evaInimigo.draw()
        vigInimigo.draw()
        linha1.draw()
        linha2.draw()
        textoAtaque.draw()
        textoTecnica.draw()
        textoElemental.draw()

        janela.update()

main()