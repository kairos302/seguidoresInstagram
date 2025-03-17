import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from SeleniumComand.RoolPage import *
from SeleniumComand.GetValue import getValueByXpath
from SeleniumComand.Wait import WaitByXpath

def ClickByAlert(nav, xpath):
    try:
        nav.find_element("xpath", xpath).click()
        time.sleep(1)
        return 1
    except:
        None

def ClickById(nav, id):
    try:
        nav.find_element("id", id).click()
        return 1
    except:
        return 0 

def ClickByXpath(nav, xpath):
    try:
        nav.find_element("xpath", xpath).click()
        return 1
    except Exception as e:
        print(e)
        return 0

def ClickByEsc(nav):
    try:
        #ESC
        time.sleep(1)
        action = ActionChains(nav)
        action.key_down(Keys.ESCAPE).perform() 
        time.sleep(0.5)
    except:
        None
 
def ClickByTab(nav):
    try:
        #TAB
        time.sleep(1)
        action = ActionChains(nav)
        action.key_down(Keys.TAB).perform() 
        time.sleep(0.5)
    except:
        None    

def ClickByEnter(nav):
    try:
        #ENTER
        time.sleep(1)
        action = ActionChains(nav)
        action.key_down(Keys.ENTER).perform() 
        time.sleep(0.5)
    except:
        None         

def ClickInputName(nav, name):
    
    try:
        time.sleep(1.5)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').click()               
    except:
        None     

def ClickByAlertAccept(nav, tempo):
    try:
       time.sleep(tempo)
       WebDriverWait(nav, 3).until(EC.alert_is_present())
       nav.switch_to.alert.accept()
    except:
           print("")

def ClickSvgAriaLabel(nav, name):
    try:
        time.sleep(1.5)                      
        nav.find_element(By.CSS_SELECTOR,'svg[aria-label="'+name+'"]').click()               
    except:
        None

def ClickAhref(nav, name):
    try:
        time.sleep(5)                             
        nav.find_element(By.CSS_SELECTOR,'a[href="/'+name+'/"]').click() 
        time.sleep(4)
        return 1              
    except:
        return 0
#Seguidores(Tela aberta)
def ClickAclass(nav):
    try:
        time.sleep(1.5)                             
        nav.find_element(By.CSS_SELECTOR,'a[class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x5n08af x9n4tj2 _a6hd"]').click() 
        return 1              
    except:
        return 0

def ClickButtonDeixarSeguir(nav):
    try:
        time.sleep(1.5)
        ClickByXpath(nav, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]')        
    except:
        None

def ClickOkInPoupTenteNovamenteMaisTarde(nav):
    try:
        time.sleep(2)
        ClickByXpath(nav, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')        
    except:
        None

def PoupOpenWhenClickButtonSeguir(nav):
    time.sleep(2)
    ClickButtonDeixarSeguir(nav)
    time.sleep(1.5)
    ClickOkInPoupTenteNovamenteMaisTarde(nav)

def TryVerificationIfTextButtonIsSeguir(nav, xpath):
    txtButtonSeguir = getValueByXpath(nav, xpath)
    if txtButtonSeguir == 'Seguir':
        return 1
    return 0
    
def ClickSeguir(nav, listaDiv):

    numDiv1 = listaDiv[0]
    numDiv2 = listaDiv[1]
    contSeg = 0
    for i in range(numDiv2, 100, 1):   
        rtBtnSeguir = TryVerificationIfTextButtonIsSeguir(nav, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div['+str(numDiv1)+']/div[1]/div/div['+str(i)+']/div/div/div/div[3]/div/button/div/div')               
        if rtBtnSeguir == 1:
            time.sleep(3)
            rtSegu = ClickByXpath(nav, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div['+str(numDiv1)+']/div[1]/div/div['+str(i)+']/div/div/div/div[3]/div/button')
            contSeg = contSeg + rtSegu
            ClickOkInPoupTenteNovamenteMaisTarde(nav)
        if i % 4 == 0:
            RoolPageWithSendKeysByXpath(nav, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div['+str(numDiv1)+']/div[1]/div/div['+str(i)+']/div/div/div/div[3]/div/button', i)
        #Regra instagram de poder seguir 30 usuarios durante 5 minutos
        if i % 20 == 0:
            time.sleep(320)
    return contSeg
    


