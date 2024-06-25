from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

def exibirMensagem():
    # print('Olá Mundo')
    messagebox.showinfo('Mensagem', 'Olá, Mundo!')

botao = Button(janela, text = 'Clique aqui', command=exibirMensagem)
botao.pack()
# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()