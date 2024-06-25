from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# pack - TOP, BOTTOM, LEFT, RIGTH
botao1 = Button(janela, text = 'VERDE', fg= 'white', bg='green' )
botao1.pack(side= LEFT, padx=10, pady=10)

botao2 = Button(janela, text = 'AMARELO', fg= 'black', bg='yellow' )
botao2.pack(side= LEFT, padx=10, pady=10)

botao3 = Button(janela, text = 'Azul', fg= 'white', bg='blue' )
botao3.pack(side= LEFT, padx=10, pady=10)

# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()