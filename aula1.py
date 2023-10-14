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


def amarelocor():
    root.configure(bg=amarelo)


def vermelhocor():
    root.configure(bg=vermelho)


def verdecor():
    root.configure(bg=verde)


bt1 = Button(root, text="azul", command=azulcor, font="Time 10 bold")
bt1.place(width=200, height=100, x=100, y=20)

bt2 = Button(root, text="amarelo", command=amarelocor, font="Time 10 bold")
bt2.place(width=200, height=100, x=300, y=20)

bt3 = Button(root, text="vermelho", command=vermelhocor, font="Time 10 bold")
bt3.place(width=200, height=100, x=100, y=200)

bt4 = Button(root, text="verde", command=verdecor, font="Time 10 bold")
bt4.place(width=200, height=100, x=300, y=200)

root.mainloop()