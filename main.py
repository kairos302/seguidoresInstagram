from selenium import webdriver
from LogConta.logInstagram import logInsta
from Instagram.instagram import InstagramFunction
from SeleniumComand.Click import *
from SeleniumComand.Input import *
from tkinter import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def index(user, seguir):
    service = Service()
    options = webdriver.ChromeOptions()
    nav = webdriver.Chrome(service=service, options=options)
    nav.get("https://www.instagram.com/") 
    time.sleep(2)
    rtLog = logInsta(nav, user)
    if rtLog == 1:
        contadorSeguidores = InstagramFunction(nav, seguir)
        if contadorSeguidores > 0:
            rtTextoSeguidores['text'] = "Conseguiu seguir cerca de "+str(contadorSeguidores)+ " pessoas"
        else:
            rtTextoSeguidores['text'] = "Não conseguiu seguir ninguem do perfil "+seguir
    else:
        rtTextoSeguidores['text'] = "Não conseguiu entrar na conta do Instagram"
    #nav.quit()

janela = Tk()
janela.title('Instagram')

t1 = Label(janela, text=" 40 segundos parado a cada 20 pessoas seguir")
t1.place(x=0,y=10)
#INICIA COM VALORES DEFAULT
#USER
u1 = Label(janela, text="User")
u1.place(x=10,y=40)
u = StringVar()
user = Entry(janela, bd=5, text=u)
u.set('conta usuario')
user.place(x=60,y=40)

#SENHA
#s1=Label(janela,text="senha")
#s1.place(x=10,y=40)
#se = StringVar()
#senha=Entry(janela,bd=5, text=se)
#se.set("")
#senha.place(x=60,y=40)

#seguir
seg1=Label(janela,text="seguir")
seg1.place(x=10,y=70)
seg = StringVar()
seguir=Entry(janela,bd=5, text=seg)
seg.set('perfil para seguir')
seguir.place(x=60,y=70)

rtTextoSeguidores=Label(janela,text="")
rtTextoSeguidores.place(x=5,y=150)

B = Button(janela, text= "Clique para começar", command=lambda: index(user.get(), seguir.get()), fg="black", bg="light blue")
B.place(x=65, y=110)
janela.geometry("250x250+10+10")

janela.mainloop()





