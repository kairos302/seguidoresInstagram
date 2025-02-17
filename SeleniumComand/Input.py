import time
from selenium.webdriver.common.by import By
from SeleniumComand.Click import  *


def ImputById(nav, id, elemento):
    
    try:
        time.sleep(1.5)
        nav.find_element("id", id).clear()
        time.sleep(1)
        nav.find_element("id", id).send_keys(elemento)
    except:
        None

def ImputByXpath(nav, xpath, elemento):
    
    try:
        time.sleep(1.5)
        nav.find_element("xpath", xpath).clear()
        time.sleep(1)
        nav.find_element("xpath", xpath).send_keys(elemento)
    except:
        None

def ImputName(nav, name, elemento):
    
    try:
        time.sleep(1.5)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').clear()
        time.sleep(1)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').send_keys(elemento)
    except:
        None

def ImputNameNotClear(nav, name, elemento):
    
    try:
        time.sleep(1)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').send_keys(elemento)
    except:
        None
        
def ImputNameWithTab(nav, name, elemento):
    try:
        time.sleep(1)
        nav.find_element(By.CSS_SELECTOR,'input[name="'+name+'"]').send_keys(elemento)
        ClickByTab(nav)
    except:
        None

def ImputAriaLabel(nav, name, elemento):
    
    try:
        time.sleep(0.5)
        nav.find_element(By.CSS_SELECTOR,'input[aria-label="'+name+'"]').clear()
        time.sleep(1)
        nav.find_element(By.CSS_SELECTOR,'input[aria-label="'+name+'"]').send_keys(elemento)
    except:
        None