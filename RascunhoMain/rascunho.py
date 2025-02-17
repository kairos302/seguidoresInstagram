from tkinter import *

janela = Tk()
janela.title('Seguidores no instagram')
janela.geometry("500x500+10+10")

#INICIA NOT VALORES DEFAULT
#USER
u1 = Label(janela, text="User")
u1.place(x=10,y=10)
user = Entry(janela, bd =5)
user.place(x=60,y=10)

#SENHA
s1=Label(janela,text="senha")
s1.place(x=10,y=40)
senha=Entry(janela,bd=5)
senha.place(x=60,y=40)

#seguir
seg1=Label(janela,text="seguir")
seg1.place(x=10,y=70)
seguir=Entry(janela,bd=5)
seguir.place(x=60,y=70)

janela.mainloop()