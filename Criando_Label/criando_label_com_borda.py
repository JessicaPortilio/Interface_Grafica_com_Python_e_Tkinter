# Importa todas as classes e funções do módulo tkinter. Isso inclui a classe Tk, que é usada para criar a janela principal da aplicação GUI.
from tkinter import *

# Cria uma instância da classe Tk, que inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela principal da aplicação. Esse título aparecerá na barra de título da janela.
janela.title('Interface Gráfica')


# Estilo de Borda

# Cria um rótulo (Label) com o texto 'opção: FLAT' e define o estilo de borda como FLAT.
# relief - Relevo - Uma borda decorativa ao redor do label
# FLAT - Plana
rotulo1 = Label(janela, text='opção: FLAT', relief=FLAT)

# Cria um rótulo (Label) com o texto 'opção: RAISED' e define o estilo de borda como RAISED.
rotulo2 = Label(janela, text='opção: RAISED', relief=RAISED)

# Cria um rótulo (Label) com o texto 'opção: SUNKEN' e define o estilo de borda como SUNKEN.
# SUNKEN - Afundado
rotulo3 = Label(janela, text='opção: SUNKEN', relief=SUNKEN)

# Cria um rótulo (Label) com o texto 'opção: GROOVE' e define o estilo de borda como GROOVE.
rotulo4 = Label(janela, text='opção: GROOVE', relief=GROOVE)

# Cria um rótulo (Label) com o texto 'opção: RIDGE' e define o estilo de borda como RIDGE.
rotulo5 = Label(janela, text='opção: RIDGE', relief=RIDGE)

# Adiciona o rótulo à janela principal e exibe-o.
rotulo1.pack()
rotulo2.pack()
rotulo3.pack()
rotulo4.pack()
rotulo5.pack()

# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()
