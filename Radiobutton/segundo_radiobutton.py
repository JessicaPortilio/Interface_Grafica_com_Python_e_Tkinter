from tkinter import *

janela = Tk()

janela.geometry('950x400')

janela.title('Janela Principal')

def imprimirItemSelecionada():
    LabelResultado.config(text=f'Você selecionou a letra {variavelOpcaoSelecionada.get()}')

variavelOpcaoSelecionada = StringVar(janela, '0')

letras = {
    'Letra A': 'A',
    'Letra B': 'B',
    'Letra C': 'C',
    'Letra D': 'D',
    'Letra E': 'E',
    'Letra F': 'F',
    }

for textoColuna0, textoColuna1 in letras.items():
    Radiobutton(janela, text=textoColuna0, variable=variavelOpcaoSelecionada, value=textoColuna1, font=20, command=imprimirItemSelecionada).pack()

LabelResultado = Label(janela, text='', font=30)
LabelResultado.pack()

janela.mainloop()