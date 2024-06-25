# O método pack() é usado para organizar widgets em blocos 
# retangulares dentro do widget pai, 
# geralmente a janela principal (Tk()).
# Os widgets são posicionados um abaixo do outro ou lado a lado, 
# dependendo do parâmetro side e fill.

# O método grid() é usado para organizar widgets 
# em uma grade (tabela) de linhas e colunas.
# Cada widget é colocado em uma célula específica 
# da grade usando coordenadas de linha (row) e coluna (column).

# O método place() é usado para posicionar widgets em coordenadas 
# absolutas dentro do widget pai.
# Você especifica as coordenadas x e y do canto superior esquerdo 
# do widget e pode definir sua largura e altura.

from tkinter import *

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de Posicionamento")

# Criando botões com diferentes métodos de posicionamento

# Usando pack()
# pack - TOP, BOTTOM, LEFT, RIGTH
botao1 = Button(janela, text="Botão 1 - Pack")
botao1.pack(side=LEFT, padx=10, pady=10)

botao2 = Button(janela, text="Botão 2 - Pack")
botao2.pack(side=LEFT, padx=10, pady=10)

# Usando grid()
# botao3 = Button(janela, text="Botão 3 - Grid")
# botao3.grid(row=0, column=0, padx=10, pady=10)

# botao4 = Button(janela, text="Botão 4 - Grid")
# botao4.grid(row=0, column=1, padx=10, pady=10)

# # Usando place()
# botao5 = Button(janela, text="Botão 5 - Place")
# botao5.place(x=50, y=50, width=100, height=50)

# botao6 = Button(janela, text="Botão 6 - Place")
# botao6.place(x=200, y=50, width=100, height=50)

# Loop principal da aplicação
janela.mainloop()


