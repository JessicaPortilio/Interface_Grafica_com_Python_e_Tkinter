# Importa a classe Tk da biblioteca tkinter, que é usada para criar a janela principal da aplicação GUI.
from tkinter import Tk

# Cria uma instância da classe Tk. Isso inicializa a janela principal da aplicação.
janela = Tk()

# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.) 
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()
