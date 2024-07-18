from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Inicializa a janela principal da aplicação
janela = Tk()

# Define o tamanho da janela
janela.geometry('300x300')

# Define o título da janela
janela.title('Janela Principal')

# Cria e posiciona um rótulo (label) com o texto "Dia da Semana"
textoDiaDaSemana = Label(janela, text='Dia da Semana', font=('Arial', 14))
textoDiaDaSemana.pack()

# Cria uma Listbox para listar os dias da semana
listBox = Listbox(janela, font=('Arial', 14))

# Insere os dias da semana na Listbox
listBox.insert(1, 'Domingo')
listBox.insert(2, 'Segunda-Feira')
listBox.insert(3, 'Terça-Feira')
listBox.insert(4, 'Quarta-Feira')
listBox.insert(5, 'Quinta-Feira')
listBox.insert(6, 'Sexta-Feira')
listBox.insert(7, 'Sábado')

# Posiciona a Listbox na janela
listBox.pack()

# Entra no loop principal da aplicação
janela.mainloop()
