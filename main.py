from selenium import webdriver
from GetCnpjs.indexCnpjs import getCnpj
from SeleniumComand.Input import ImputByXpath
from SeleniumComand.RoolPage import RollPage
from SeleniumComand.Click import *
from GetCnpjs.indexCnpjs import getCnpj
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
nav = webdriver.Chrome(service=service, options=options)

def index():
    nav.get("https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada") 
    
    #Atividade Principal (CNAE)
    ImputByXpath(nav, '//*[@id="__nuxt"]/div/div[2]/section/div[2]/div[2]/section/div/div/div/div/div[1]/input', '4721102')

    #PESQUISAR
    time.sleep(3)
    RollPage(nav, 300)
    ClickByTab(nav)
    ClickByXpath(nav, '//*[@id="__nuxt"]/div/div[2]/section/div[6]/div/div/a[1]')
    
    getCnpj(nav)
    time.sleep(5)
    nav.quit()

index()