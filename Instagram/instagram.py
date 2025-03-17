import time
from SeleniumComand.Click import *
from SeleniumComand.Input import *
from SeleniumComand.Wait import WaitForSearchXpathButtonSeguir

def DentroPerfil(nav):
    time.sleep(7)
    #tela seguidores(Aberta)
    listaDiv =  WaitForSearchXpathButtonSeguir(nav)
    rtSegu = 0
    if len(listaDiv)> 0:
        rtSegu = ClickSeguir(nav, listaDiv)
    return rtSegu

def InstagramFunction(nav, seguir):
      
    #Pesquisar
    time.sleep(4)
    ClickSvgAriaLabel(nav, 'Pesquisa')

    #Campo pesquisar
    ImputAriaLabel(nav, 'Entrada da pesquisa', seguir)
    time.sleep(1)
    ClickByEnter(nav)
    
    dentroPerfil = ClickAhref(nav, seguir)
    if dentroPerfil == 1:
        #Seguidores
        time.sleep(1)
        ClickAclass(nav)
        contSeguidores = DentroPerfil(nav)
        return contSeguidores
    else:
        return 0
    