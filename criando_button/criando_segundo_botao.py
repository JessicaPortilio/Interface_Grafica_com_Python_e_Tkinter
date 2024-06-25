from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

def mensagem():
    print('Curso')


# destroy fecha a tela ao clicar no botão
botao = Button(janela, text = 'Sair', command=janela.destroy)
botao.pack(side=LEFT, padx=5, pady=5)

botao2 = Button(janela, text = 'Entrar', command=mensagem)
botao2.pack(side=LEFT, padx=5, pady=5)
# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()