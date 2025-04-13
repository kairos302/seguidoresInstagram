from SeleniumComand.Input import *
from SeleniumComand.Wait import *

def logInsta(nav, nomeUser):
    try:
        #Telefone, email
        ImputName(nav, 'username', nomeUser)
        #senha
        #ImputName(nav, 'password', senha)
        time.sleep(18)
        #Entrar
        #ClickByXpath(nav, '//*[@id="loginForm"]/div[1]/div[3]/button/div')
        
        rtLog =   WaitByCssSelectorSvgAriaLabel(nav, 10, 'Pesquisa')                   
        return rtLog
    except Exception as e:
        print(e)
        return 0