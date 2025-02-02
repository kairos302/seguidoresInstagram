#Rolar pagina
def RollPage(nav, q):
    try:
        c =  str(q)
        nav.execute_script('window.scrollBy(0, '+c+')')
    except Exception as e:
        print(e)
        None