from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Define o tamanho da janela.
janela.geometry("300x150")

def mensagem():
    print('Curso')

# Cria e posiciona o label de boas-vindas na linha 0, ocupando 2 colunas e centralizando.
texto = Label(janela, text='Sejam Bem-vindos!', font=('Gautami', 16, 'italic'))
texto.grid(row=0, column=2, columnspan=2, pady=10,)

# Configura o peso das colunas para permitir a centralização
# janela.grid_columnconfigure(0, weight=1)
# janela.grid_columnconfigure(1, weight=1)

# Cria um frame para conter os botões e posiciona-o na linha 1, ocupando 2 colunas e centralizando.
frame_botoes = Frame(janela)
frame_botoes.grid(row=1, column=2, columnspan=2, pady=10)

# Cria o botão 'Sair' que fecha a janela ao ser clicado e o adiciona ao frame.
botao = Button(frame_botoes, text='Sair', command=janela.destroy)
botao.pack(side=LEFT, padx=5, pady=5)

# Cria o botão 'Entrar' que chama a função mensagem ao ser clicado e o adiciona ao frame.
botao2 = Button(frame_botoes, text='Entrar', command=mensagem)
botao2.pack(side=LEFT, padx=5, pady=5)

# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()
