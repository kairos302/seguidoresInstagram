#Rolar pagina
from selenium.webdriver.common.keys import Keys 
import time

def RoolPageWithSendKeysByXpath(nav, xpath, i):
    try:
        time.sleep(2.5)
        print("indice  "+ str(i))
        nav.find_element("xpath", xpath).send_keys(Keys.PAGE_DOWN)
    except:
        None