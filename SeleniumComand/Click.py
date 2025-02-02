import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
    except:
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

   