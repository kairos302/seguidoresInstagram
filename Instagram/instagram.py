import time
from SeleniumComand.Click import *
from SeleniumComand.Input import *

def DentroPerfil(nav):
    time.sleep(5)
    #tela seguidores(Aberta)
    rtSegu = ClickSeguir(nav)
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
    