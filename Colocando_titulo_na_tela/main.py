# Importa todas as classes e funções do módulo tkinter. Isso inclui a classe Tk, que é usada para criar a janela principal da aplicação GUI.
from tkinter import *

# Cria uma instância da classe Tk, que inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela principal da aplicação. Esse título aparecerá na barra de título da janela.
janela.title('Interface Gráfica')

# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()
