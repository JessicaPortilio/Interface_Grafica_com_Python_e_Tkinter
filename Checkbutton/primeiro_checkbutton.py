from tkinter import *

janela = Tk()

janela.geometry('950x400')

janela.title('Janela Principal')

informacao = Label(janela, text='Selecione a opção desejada', fg='blue', font=('Arial', 20))
informacao.pack()

def azulClicado():
    print(varAzul.get())

varAzul = StringVar()
cheackAzul = Checkbutton(janela, text='Azul', variable= varAzul, font=('Arial', 20),
                    onvalue='Clicou na cor Azul', offvalue='', height=2, width=10, command=azulClicado)
cheackAzul.pack()

def amareloClicado():
    print(varAmarelo.get())

varAmarelo = StringVar()

cheackAmarelo = Checkbutton(janela, text='Amarelo', variable= varAmarelo, font=('Arial', 20),
                    onvalue='Clicou na cor Amarelo', offvalue='', height=2, width=10, command=amareloClicado)
cheackAmarelo.pack()

def verdeClicado():
    print(varVerde.get())

varVerde = StringVar()

cheackVerde = Checkbutton(janela, text='Verde', variable= varVerde, font=('Arial', 20),
                    onvalue='Clicou na cor Verde', offvalue='', height=2, width=10, command=verdeClicado)
cheackVerde .pack()

janela.mainloop()