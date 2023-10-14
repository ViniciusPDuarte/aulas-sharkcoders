from tkinter import *

root = Tk()
root.title('hello')
root.geometry('500x300+200+200')

root.wm_resizable(width=True, height=False)

azul = '#2902ff'
amarelo = '#fffc03'
vermelho = '#ff0303'
verde = '#17ff03'

def azulcor():
    root.configure(bg=azul)
    lb = Label(root, text='azul', font='Time 20 bold')
    lb.place(width=150, height=30, x=170, y=120)


def amarelocor():
    root.configure(bg=amarelo)
    lb = Label(root, text='amarelo', font='Time 20 bold')
    lb.place(width=150, height=30, x=170, y=120)


def vermelhocor():
    root.configure(bg=vermelho)
    lb = Label(root, text='vermelho', font='Time 20 bold')
    lb.place(width=150, height=30, x=170, y=120)


def verdecor():
    root.configure(bg=verde)
    lb = Label(root, text='verde', font='Time 20 bold')
    lb.place(width=150, height=30, x=170, y=120)


bt1 = Button(root, text="azul", command=azulcor, font="Time 10 bold")
bt1.place(width=100, height=50, x=100, y=20)

bt2 = Button(root, text="amarelo", command=amarelocor, font="Time 10 bold")
bt2.place(width=100, height=50, x=300, y=20)

bt3 = Button(root, text="vermelho", command=vermelhocor, font="Time 10 bold")
bt3.place(width=100, height=50, x=100, y=200)

bt4 = Button(root, text="verde", command=verdecor, font="Time 10 bold")
bt4.place(width=100, height=50, x=300, y=200)

root.mainloop()