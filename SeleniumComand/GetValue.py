from SeleniumComand.Click import *

def getValueByXpath(nav, xpath):
    try:
        txt = nav.find_element("xpath", xpath)
        txtC  = txt.text
        return txtC
    except Exception as e:
        print(e)
        return  ''

