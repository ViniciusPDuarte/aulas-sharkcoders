from tkinter import *

root = Tk()

root.title('Agenda')
root.geometry('500x500+300+200')
root.wm_resizable(width=False, height=False)


# nome
nometxt = Text(root, width=40, height=1)
nometxt.place(x=100, y=30)

nomelb = Label(root, text='Nome', font='Time 10 italic')
nomelb.place(width=80, height=30, x=20, y=25)


# telefone
teletxt = Text(root, width=40, height=1)
teletxt.place(x=100, y=70)

telelb = Label(root, text='Telefone', font='Time 10 italic')
telelb.place(width=80, height=30, x=20, y=65)


# endereço
endtxt = Text(root, width=40, height=1)
endtxt.place(x=100, y=110)

endlb = Label(root, text='Endereço', font='Time 10 italic')
endlb.place(width=80, height=30, x=20, y=105)


# distrito
disttxt = Text(root, width=15, height=1)
disttxt.place(x=100, y=150)

dislb = Label(root, text='Distrito', font='Time 10 italic')
dislb.place(width=80, height=30, x=20, y=145)


# país
paistxt = Text(root, width=15, height=1)
paistxt.place(x=300, y=150)

paislb = Label(root, text='País', font='Time 10 italic')
paislb.place(width=80, height=30, x=220, y=145)


# e-mail
emtxt = Text(root, width=40, height=1)
emtxt.place(x=100, y=190)

emaillb = Label(root, text='E-mail', font='Time 10 italic')
emaillb.place(width=80, height=30, x=20, y=185)


# botões
pesquisarbt = Button(root, text="Pesquisar", font="Time 10 bold")
pesquisarbt.place(width=80, height=30, x=130, y=250)

criarbt = Button(root, text="Criar", font="Time 10 bold")
criarbt.place(width=80, height=30, x=300, y=250)


# mainloop
root.mainloop()
