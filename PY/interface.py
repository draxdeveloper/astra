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

    #regiao de decorcao dos 4 elementos, não está na estrutura certa, depois criar uma função para ancorar sprites numa região, não apenas uma região na outra
    rDecoracaoSuperior1 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,"tela","direita",rImagemInimigo,"abaixo")
    rDecoracaoSuperior2 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoSuperior1,"direita",rImagemInimigo,"abaixo")
    rDecoracaoSuperior3 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoSuperior2,"direita",rImagemInimigo,"abaixo")
    # rDecoracaoSuperior4 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoSuperior3,"direita",rImagemInimigo,"abaixo")
    rDecoracaoInferior1 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,"tela","direita","tela","acima")
    rDecoracaoInferior2 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoInferior1,"direita","tela","acima")
    rDecoracaoInferior3 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoInferior2,"direita","tela","acima")
    # rDecoracaoInferior4 = Regiao(0,0,janela,"/combate/decoracao4elementos.png",0,0,rDecoracaoInferior3,"direita","tela","acima")

    #região seleção de ataque
    rSelecaoAtaque = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,"tela","direita",rDecoracaoSuperior1,"abaixo","",0,0,True,0)
    # rSelecaoAtaque.moverRegiao(0,rSelecaoAtaque.getBorda().height)

    #texto seleção de ataque
    textoAtaque = Sprite("../assets/sprites/interface/combate/textoSelecaoAtaque.png")
    aninharNaRegiao(textoAtaque,rSelecaoAtaque,"centro","centro")

    #regiao seleção de tecnica
    rSelecaoTecnica = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,"tela","direita",rDecoracaoInferior1,"acima","",0,0,True,1)

    #texto seleção tecnica
    textoTecnica = Sprite("../assets/sprites/interface/combate/textoSelecaoTecnica.png")
    aninharNaRegiao(textoTecnica,rSelecaoTecnica,"centro","centro")

    #regiao selecao tecnica elemental
    rSelecaoElemental = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoAtaque,"direita",rDecoracaoSuperior2,"abaixo","",0,0,True,2)

    #texto tecnica elemental
    textoElemental = Sprite("../assets/sprites/interface/combate/textoElemental.png")
    aninharNaRegiao(textoElemental,rSelecaoElemental,"centro","centro")

    #regiao selecao tecnica alinhamento
    rSelecaoAlinhamento = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoElemental,"direita",rDecoracaoSuperior3,"abaixo","",0,0,True,3)

    #texto tecnica alinhamento
    textoAlinhamento = Sprite("../assets/sprites/interface/combate/textoAlinhamento.png")
    aninharNaRegiao(textoAlinhamento,rSelecaoAlinhamento,"centro","centro")

    #regiao selecao tecnica emblema
    rSelecaoEmblema = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoTecnica,"direita",rDecoracaoInferior2,"acima","",0,0,True,4)

    #texto tecnical emblema
    textoEmblema = Sprite("../assets/sprites/interface/combate/textoEmblema.png")
    aninharNaRegiao(textoEmblema,rSelecaoEmblema,"centro","centro")

    #regiao selecao tecnica especial
    rSelecaoEspecial = Regiao(0,0,janela,"/combate/rSelecaoAtaque.png",3,3,rSelecaoEmblema,"direita",rDecoracaoInferior3,"acima","",0,0,True,5)

    #texto tecnical especial
    textoEspecial = Sprite("../assets/sprites/interface/combate/textoEspecial.png")
    aninharNaRegiao(textoEspecial,rSelecaoEspecial,"centro","centro")

    #região  do imagem do astra do jogador
    rImagemJogador = Regiao(0,0,janela,"/combate/rImagemJogador.png",3,3,rSelecaoAlinhamento,"direita",rAtributosInimigo,"abaixo")

    #imagem astra do jogador
    jogador = Sprite("../assets/sprites/astras/orbAgua138.png")
    aninharNaRegiao(jogador,rImagemJogador,"centro","centro")

    #região icones do jogador
    rSimboloJogador = Regiao(0,0,janela,"/combate/rSimboloAstraJogador.png",3,3,rSelecaoEspecial,"direita",rImagemJogador,"abaixo")

    #simbolos do jogador
    simboloElementoJogador = Sprite("../assets/sprites/interface/combate/aguaIconeRedux.png")
    simboloAlinhamentoJogador = Sprite("../assets/sprites/interface/combate/solIconeRedux.png")
    simboloEmblemaJogador = Sprite("../assets/sprites/interface/combate/espadaIconeRedux.png")

    aninharNaRegiao(simboloElementoJogador,rSimboloJogador,"esquerda","centro,")
    aninharNaRegiao(simboloAlinhamentoJogador,rSimboloJogador,"centro","centro",-4)
    aninharNaRegiao(simboloEmblemaJogador,rSimboloJogador,"direita","centro")

    #região nome do jogador
    rNomeJogador = Regiao(0,0,janela,"/combate/rNomeAstraJogador.png",3,3,rImagemJogador,"direita",rAtributosInimigo,"abaixo")

    #nome do jogador
    nomeJogador = Sprite("../assets/sprites/interface/combate/nomeAstraAquaRedux.png")
    aninharNaRegiao(nomeJogador,rNomeJogador,"centro","centro")

    #região HP e SP do jogador
    rHPJogador = Regiao(0,0,janela,"/combate/rHPSPJogador.png",3,3,rImagemJogador,"direita",rNomeJogador,"abaixo")
    rSPJogador = Regiao(0,0,janela,"/combate/rHPSPJogador.png",3,3, rHPJogador, "direita", rNomeJogador, "abaixo")

    #texto HP e SP jogador
    hpJogador = Sprite("../assets/sprites/interface/combate/hpJogador.png")
    valorHPJogador = Sprite("../assets/sprites/interface/combate/valorHPSPJogador.png")
    spJogador = Sprite("../assets/sprites/interface/combate/spJogador.png")
    valorSPJogador = Sprite("../assets/sprites/interface/combate/valorHPSPJogador.png")

    aninharNaRegiao(hpJogador,rHPJogador,"centro","acima")
    aninharNaRegiao(valorHPJogador,rHPJogador,"centro","abaixo")
    aninharNaRegiao(spJogador,rSPJogador,"centro","acima")
    aninharNaRegiao(valorSPJogador,rSPJogador,"centro","abaixo")

    #região atributos do jogador
    rAtributosJogador = Regiao(0,0,janela,"/combate/rAtributosJogador.png",3,3,rImagemJogador,"direita",rHPJogador,"abaixo")

    #atributos jogador
    forJogador = Sprite("../assets/sprites/interface/combate/forJogador.png")
    preJogador = Sprite("../assets/sprites/interface/combate/preJogador.png")
    vigJogador = Sprite("../assets/sprites/interface/combate/vigJogador.png")
    evaJogador = Sprite("../assets/sprites/interface/combate/evaJogador.png")

    aninharNaRegiao(forJogador,rAtributosJogador,"esquerda","acima",5,5)
    aninharNaRegiao(preJogador,rAtributosJogador,"direita","acima", 5,5)
    aninharNaRegiao(vigJogador,rAtributosJogador,"esquerda","abaixo",5,5)
    aninharNaRegiao(evaJogador,rAtributosJogador,"direita","abaixo",5,5)

    #região descrição
    rDescricao = Regiao(0,0,janela,"/combate/rDescricao.png",3,3,rNomeJogador,"direita",rTextoPrincipal,"abaixo")

    #texto descrição, ele é variavel e decidido no loop... No momento, futuramente esse processo será uma função da classe de texto
    descricaoAtual = ""

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
        rSelecaoAlinhamento.desenhaRegiao()
        rSelecaoEmblema.desenhaRegiao()
        rSelecaoEspecial.desenhaRegiao()
        rDecoracaoSuperior1.desenhaRegiao()
        rDecoracaoSuperior2.desenhaRegiao()
        rDecoracaoSuperior3.desenhaRegiao()
        # rDecoracaoSuperior4.desenhaRegiao()
        rDecoracaoInferior1.desenhaRegiao()
        rDecoracaoInferior2.desenhaRegiao()
        rDecoracaoInferior3.desenhaRegiao()
        # rDecoracaoInferior4.desenhaRegiao()
        rImagemJogador.desenhaRegiao()
        rSimboloJogador.desenhaRegiao()
        rNomeJogador.desenhaRegiao()
        rHPJogador.desenhaRegiao()
        rSPJogador.desenhaRegiao()
        rAtributosJogador.desenhaRegiao()
        rDescricao.desenhaRegiao()


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
        textoAlinhamento.draw()
        textoEmblema.draw()
        textoEspecial.draw()
        nomeJogador.draw()
        hpJogador.draw()
        valorHPJogador.draw()
        spJogador.draw()
        valorSPJogador.draw()
        forJogador.draw()
        preJogador.draw()
        evaJogador.draw()
        vigJogador.draw()

        if(cursor.getPosAtual() == 0):

            descricaoAtual = Sprite("../assets/sprites/interface/combate/textoDescricaoAtaque.png")

        elif(cursor.getPosAtual() == 1):

            descricaoAtual = Sprite("../assets/sprites/interface/combate/textoDescricaoTecnica.png")


        aninharNaRegiao(descricaoAtual,rDescricao,"esquerda","abaixo",5,2)

        descricaoAtual.draw()

        #draw sprites

        inimigo.draw()
        simboloElemento.draw()
        simboloAlinhamento.draw()
        simboloEmblema.draw()
        jogador.draw()
        simboloElementoJogador.draw()
        simboloAlinhamentoJogador.draw()
        simboloEmblemaJogador.draw()

        #draw cursor
        cursor.desenhaCursor()

        janela.update()

main()