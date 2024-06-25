from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Define o tamanho da janela.
janela.geometry("300x150")

# Função que será chamada ao clicar no botão 'Entrar'.
def mensagem():
    # Obtém o texto do campo de entrada e o imprime.
    texto = campo_entrada.get()
    print(f'Curso: {texto}')

# Cria um rótulo para o campo de entrada.
label_entrada = Label(janela, text='Curso:')
label_entrada.grid(row=0, column=0, padx=10, pady=10, sticky='e')

# Cria o campo de entrada.
campo_entrada = Entry(janela, width=30)
campo_entrada.grid(row=0, column=1, padx=10, pady=10)

# Cria um frame para conter os botões.
frame_botoes = Frame(janela)
frame_botoes.grid(row=1, column=0, columnspan=2, pady=10)

# Cria o botão 'Entrar' que chama a função mensagem ao ser clicado.
botao_entrar = Button(frame_botoes, text='Entrar', command=mensagem)
botao_entrar.pack(side=LEFT, padx=5)

# Cria o botão 'Sair' que fecha a janela ao ser clicado.
botao_sair = Button(frame_botoes, text='Sair', command=janela.destroy)
botao_sair.pack(side=RIGHT, padx=5)

# Entra no loop principal da aplicação.
janela.mainloop()
