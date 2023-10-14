# imports

from tkinter import *
from random import randint

# titulo e tela

tela = Tk()
tela.title('Blackjack, jogo do 21')
tela.geometry('1300x700+200+200')
tela.wm_resizable(width=True, height=False)

# sistemas dos botões

# ---------------------------------------------------------------------------------------

# comprar

lbcmpr = Label(tela, text='0', font='Time 70 italic')
lbcmpr.place(width=100, height=100, x=200, y=180)
def comprar():
    nvcarta = randint(1, 11)
    cmpr = int(lbcmpr.cget('text'))
    cmpr += nvcarta
    lbcmpr.config(text=str(cmpr))

# ---------------------------------------------------------------------------------------

# deitar

def deitar():
    deita = randint(14, 21)
    lbdtr = Label(tela, text=deita, font='Time 70 italic', fg='red')
    lbdtr.place(width=100, height=100, x=1000, y=180)

# ---------------------------------------------------------------------------------------

# botões

btcmpr = Button(tela, text="Comprar",command=comprar, font="Time 20 bold")
btcmpr.place(width=150, height=75, x=100, y=370)

btdtr = Button(tela, text="Deitar",command=deitar, font="Time 20 bold")
btdtr.place(width=150, height=75, x=100, y=500)

# ---------------------------------------------------------------------------------------

# mainloop <<essencial>>

tela.mainloop()
