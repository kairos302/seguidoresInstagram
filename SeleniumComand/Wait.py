from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def WaitById(nav, tempo, id):
    try:
        wait = WebDriverWait(nav, tempo)                               
        element = wait.until(EC.element_to_be_clickable((By.ID, id)))
        return 1
    except:
        return 0      

def WaitByXpath(nav, tempo, xpath):
    try:
        wait = WebDriverWait(nav, tempo)                               
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return 1
    except:
        return 0      

def WaitByCssSelector(nav, tempo, name):
    try:
        wait = WebDriverWait(nav, tempo)                               
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="'+name+'"]')))
        return 1
    except:
        return 0

def WaitByCssSelectorSvgAriaLabel(nav, tempo, name):
    try:
        wait = WebDriverWait(nav, tempo)                               
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="'+name+'"]')))
        return 1
    except:
        return 0

def WaitForSearchXpathButtonSeguir(nav):
                       
    listaDiv = []
    for numberDiv in range(2, 6, 1):
        for numberDiv2 in range(1,4,1):
            rtSegu = WaitByXpath(nav, 2,'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div['+str(numberDiv)+']/div[1]/div/div['+str(numberDiv2)+']/div/div/div/div[3]/div/button')
            if rtSegu == 1:
                listaDiv.append(numberDiv)
                listaDiv.append(numberDiv2)
                return listaDiv
    return listaDiv   

     