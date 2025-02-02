from SeleniumComand.GetValue import getValueByXpath
from SeleniumComand.Click import ClickByXpath
from WritePlanilha.writePlanilha import WrittingPlan
import time

def TryClickNextPage(nav):
    rtClickForNextPage = 0
    for i in range(5):
            time.sleep(1)      
            rtClickForNextPage = ClickByXpath(nav, '//*[@id="__nuxt"]/div/div[2]/section/div[8]/div/nav/a[2]')
            if rtClickForNextPage == 1:
                break

def dentroPagina(nav, contadorGetCnpj):
    listaCnpjs = []   
    for i in range(1,21,1):
        c = str(i)  
        xpathCnpj = '//*[@id="__nuxt"]/div/div[2]/section/div[9]/div[1]/div/div/div/div/div['+c+']/article/div/div/p/strong[1]'
        
        #print(xpathCnpj)
        textoCnpj = getValueByXpath(nav, xpathCnpj)
        print(textoCnpj)
        listaCnpjs.append(textoCnpj)
        #significa que esta na 10 pagina
        if contadorGetCnpj == 10 and i == 20:
            return listaCnpjs
        if i == 20:
            TryClickNextPage(nav)
            return listaCnpjs       
    return listaCnpjs        
        

def getCnpj(nav):
    
    listaMaiorCnpjs = []
    for i in range(1,11,1):
        time.sleep(1.5)
        print("PAGINA")
        print(i)
        contadorGetCnpj =  i
        listaCnpjs = dentroPagina(nav, contadorGetCnpj)
        if len(listaCnpjs) == 0:
            listaMaiorCnpjs.append('Nao conseguiu ir para a proxima pagina')
            break
        else:
            for i in range(len(listaCnpjs)):
                listaMaiorCnpjs.append(listaCnpjs[i])
    
    WrittingPlan(listaMaiorCnpjs)