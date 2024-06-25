from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Cria rótulos (Labels) com diferentes estilos de borda.
rotulo1 = Label(janela, text='opção: FLAT', relief=FLAT)
rotulo2 = Label(janela, text='opção: RAISED', relief=RAISED)
rotulo3 = Label(janela, text='opção: SUNKEN', relief=SUNKEN)
rotulo4 = Label(janela, text='opção: GROOVE', relief=GROOVE)
rotulo5 = Label(janela, text='opção: RIDGE', relief=RIDGE)

# Cria rótulos (Labels) com outras propriedades customizadas.
rotulo6 = Label(janela, text='Cor de fundo e texto', bg='yellow', fg='blue') # Define cor de fundo e texto.
rotulo7 = Label(janela, text='Fonte customizada', font=('Arial', 16, 'bold')) # Define fonte do texto.
rotulo8 = Label(janela, text='Tamanho customizado', width=20, height=3) # Define largura e altura.
rotulo9 = Label(janela, text='Preenchimento', padx=10, pady=5) # Define preenchimento horizontal e vertical.
rotulo10 = Label(janela, text='Ancoragem à direita', anchor='e') # Define ancoragem do texto dentro do rótulo.
rotulo11 = Label(janela, text='Especura da borda', relief=RAISED,  borderwidth=10) # Define a especura da borda
# Adiciona os rótulos à janela principal e exibe-os usando o método pack().
rotulo1.pack() # Adiciona e exibe rotulo1.
rotulo2.pack() # Adiciona e exibe rotulo2.
rotulo3.pack() # Adiciona e exibe rotulo3.
rotulo4.pack() # Adiciona e exibe rotulo4.
rotulo5.pack() # Adiciona e exibe rotulo5.
rotulo6.pack() # Adiciona e exibe rotulo6.
rotulo7.pack() # Adiciona e exibe rotulo7.
rotulo8.pack() # Adiciona e exibe rotulo8.
rotulo9.pack() # Adiciona e exibe rotulo9.

# Adiciona e exibe rotulo10. Alinha à direita 'e'. 
rotulo10.pack(anchor='e')
rotulo11.pack() # Adiciona e exibe rotulo11.

#  Outras opções de ancoragem incluem 'w' (esquerda), 
# 'n' (topo), 's' (baixo), 'nw' (canto superior esquerdo), 
# 'ne' (canto superior direito), 'sw' (canto inferior esquerdo) 
# e 'se' (canto inferior direito).


# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()
