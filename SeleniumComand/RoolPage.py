#Rolar pagina
from selenium.webdriver.common.keys import Keys 
import time

def RoolPageUpWithSendKeysByXpath(nav, xpath):
    try:
        time.sleep(1)
        nav.find_element("xpath", xpath).send_keys(Keys.PAGE_UP)
        time.sleep(2)
    except:
        None

def RoolPageDownWithSendKeysByXpath(nav, xpath):
    try:
        time.sleep(1.5)
        nav.find_element("xpath", xpath).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
    except:
        None

def FunctionRollPageDownAndUp(nav, xpath, i):
   print("indice  "+ str(i))
   RoolPageDownWithSendKeysByXpath(nav, xpath) 
   #Rolar page para cima
   RoolPageUpWithSendKeysByXpath(nav, xpath)
   
   RoolPageDownWithSendKeysByXpath(nav, xpath)

