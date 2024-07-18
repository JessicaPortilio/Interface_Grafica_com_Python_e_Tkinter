from tkinter import *

janela = Tk()

janela.geometry('950x400')

janela.title('Janela Principal')

def imprimirItemSelecionada():
    LabelResultado.config(text=f'Você selecionou a letra {variavelOpcaoSelecionada.get()}')

variavelOpcaoSelecionada = StringVar(janela, '0')
radioButtonA = Radiobutton(janela, text='Latra A', variable=variavelOpcaoSelecionada, value='A', 
                command=imprimirItemSelecionada, font=20)
radioButtonA.pack()

radioButtonB = Radiobutton(janela, text='Latra B', variable=variavelOpcaoSelecionada, value='B', 
                command=imprimirItemSelecionada, font=20)
radioButtonB.pack()

radioButtonC = Radiobutton(janela, text='Latra C', variable=variavelOpcaoSelecionada, value='C', 
                command=imprimirItemSelecionada, font=20)
radioButtonC.pack()

LabelResultado = Label(janela, text='', font=30)
LabelResultado.pack()

janela.mainloop()