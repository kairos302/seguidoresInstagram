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