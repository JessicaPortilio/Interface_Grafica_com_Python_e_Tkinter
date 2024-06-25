# Cor de Fundo (bg):
# Cor do Texto (fg):
# Fonte (font):
# Largura (width):
# Altura (height):
# Borda (borderwidth) e Estilo de Borda (relief):
# borderwidth: Define a largura da borda do botão.
# relief: Define o estilo da borda 
# (por exemplo, RAISED, SUNKEN, FLAT, GROOVE, RIDGE).
# Cursor (cursor):
# Ativação (state):
# Define o estado do botão (ACTIVE para ativo, DISABLED para desativado).
from tkinter import *

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de Personalização de Botões")

# Criando botões personalizados

# Botão 1: Texto "Clique Aqui", fundo azul, texto branco, fonte Arial 12 bold
botao1 = Button(janela, text="Clique Aqui", bg="blue", fg="white", font=("Arial", 12, "bold"))
botao1.pack(pady=10)

# Botão 2: Texto "Botão 2", fundo verde, texto preto, largura 15 caracteres, altura 2 linhas
botao2 = Button(janela, text="Botão 2", bg="green", fg="black", width=15, height=2)
botao2.pack(pady=10)

# Botão 3: Texto "Botão 3", borda elevada (RAISED), largura da borda 2 pixels
botao3 = Button(janela, text="Botão 3", relief=RAISED, borderwidth=2)
botao3.pack(pady=10)

# Botão 4: Texto "Desativado", estado desativado (DISABLED), cursor mudado para "watch"
botao4 = Button(janela, text="Desativado", state=DISABLED, cursor="watch")
botao4.pack(pady=10)

# Loop principal da aplicação
janela.mainloop()
