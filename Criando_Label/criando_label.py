from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

texto = """Criando Interface Gráfica.
Utilizando Tkinter.
Vamos apreender utilizar a interface gráfica do python.
"""

texto1 = Label(janela, text= texto, font=('Microsoft Tai Le', 15, 'italic'))
texto1.pack()
# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()