from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Define o tamanho da janela.
janela.geometry("720x520")

nome = Label(janela, text='Nome: ', font=('Arial', 16))
# grid - Divide a tela em grades em partes
# stick - Usamos para preencher o item na tela ou seja, 
# esticamos o item para não ficar espaço vazio nas laterais
nome.grid(row=1, column=0, sticky='w')

campo_nome = Entry(font=('Lao UI', 12), width=50)
campo_nome.grid(row=1, column=1, sticky='w')

sobrenome = Label(janela, text='Sobrenome: ', font=('Arial', 16))
sobrenome.grid(row=2, column=0, sticky='w')

campo_sobrenome = Entry(font=('Lao UI', 12), width=50)
campo_sobrenome.grid(row=2, column=1, sticky='w')


# Entra no loop principal da aplicação.
janela.mainloop()