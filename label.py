# Cor de Fundo (bg):
# Cor do Texto (fg):
# Fonte (font):
# Largura (width):
# Altura (height):
# Borda (borderwidth) e Estilo de Borda (relief):
# borderwidth: Define a largura da borda do botão.
# relief: Define o estilo da borda 
# (por exemplo, RAISED, SUNKEN, FLAT, GROOVE, RIDGE).

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
# Adiciona o rótulo à janela principal e exibe-o.
rotulo1.pack()
# Cria rótulos (Labels) com outras propriedades customizadas.
rotulo6 = Label(janela, text='Cor de fundo e texto', bg='yellow', fg='blue') # Define cor de fundo e texto.
rotulo7 = Label(janela, text='Fonte customizada', font=('Arial', 16, 'bold')) # Define fonte do texto.
rotulo8 = Label(janela, text='Tamanho customizado', width=20, height=3) # Define largura e altura.
rotulo9 = Label(janela, text='Preenchimento', padx=10, pady=5) # Define preenchimento horizontal e vertical.
rotulo10 = Label(janela, text='Ancoragem à direita', anchor='e') # Define ancoragem do texto dentro do rótulo.
rotulo11 = Label(janela, text='Especura da borda', relief=RAISED,  borderwidth=10) # Define a especura da borda

rotulo6.pack() # Adiciona e exibe rotulo6.
rotulo7.pack() # Adiciona e exibe rotulo7.
rotulo8.pack() # Adiciona e exibe rotulo8.
rotulo9.pack() # Adiciona e exibe rotulo9.

# Adiciona e exibe rotulo10. Alinha à direita 'e'. 
rotulo10.pack(anchor='e')
rotulo11.pack() # Adiciona e exibe rotulo11.

#____________________________________
# Cria rótulos (Labels) com diferentes estilos de borda.
# rotulo1 = Label(janela, text='opção: FLAT', relief=FLAT, bg='yellow', fg='blue' )
# rotulo2 = Label(janela, text='opção: RAISED', relief=RAISED, font=('Times New Roman', 16, 'bold'))
# rotulo3 = Label(janela, text='opção: SUNKEN', relief=SUNKEN, width=20, height=3)
# rotulo4 = Label(janela, text='opção: GROOVE', relief=GROOVE, padx=10, pady=5)
# rotulo5 = Label(janela, text='opção: RIDGE', relief=RIDGE, bg='blue', fg='white', anchor='e')


# Adiciona os rótulos à janela principal e exibe-os usando o método pack().
# rotulo1.pack() # Adiciona e exibe rotulo1.
# rotulo2.pack() # Adiciona e exibe rotulo2.
# rotulo3.pack() # Adiciona e exibe rotulo3.
# rotulo4.pack() # Adiciona e exibe rotulo4.
# rotulo5.pack(anchor='e') # Adiciona e exibe rotulo5.


# texto = """Criando Interface Gráfica.
# Utilizando Tkinter.
# Vamos apreender utilizar a interface gráfica do python.
# """

# texto1 = Label(janela, text= texto, font=('Microsoft Tai Le', 15, 'italic'))
# texto1.pack()

# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()