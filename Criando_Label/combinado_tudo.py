from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Cria rótulos (Labels) com diferentes estilos de borda.
rotulo1 = Label(janela, text='opção: FLAT', relief=FLAT, bg='yellow', fg='blue' )
rotulo2 = Label(janela, text='opção: RAISED', relief=RAISED, font=('Times New Roman', 16, 'bold'))
rotulo3 = Label(janela, text='opção: SUNKEN', relief=SUNKEN, width=20, height=3)
rotulo4 = Label(janela, text='opção: GROOVE', relief=GROOVE, padx=10, pady=5)
rotulo5 = Label(janela, text='opção: RIDGE', relief=RIDGE, bg='blue', fg='white', anchor='e')


# Adiciona os rótulos à janela principal e exibe-os usando o método pack().
rotulo1.pack() # Adiciona e exibe rotulo1.
rotulo2.pack() # Adiciona e exibe rotulo2.
rotulo3.pack() # Adiciona e exibe rotulo3.
rotulo4.pack() # Adiciona e exibe rotulo4.
rotulo5.pack(anchor='e') # Adiciona e exibe rotulo5.



# Adiciona e exibe rotulo10. Alinha à direita 'e'. 
#rotulo10.pack(anchor='e')

#  Outras opções de ancoragem incluem 'w' (esquerda), 
# 'n' (topo), 's' (baixo), 'nw' (canto superior esquerdo), 
# 'ne' (canto superior direito), 'sw' (canto inferior esquerdo) 
# e 'se' (canto inferior direito).


# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()
