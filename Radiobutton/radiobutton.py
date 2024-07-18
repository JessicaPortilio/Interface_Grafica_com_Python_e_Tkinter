from tkinter import Tk, Label, Radiobutton, StringVar

# Função para atualizar o rótulo com a cor selecionada
def atualizarLabel():
    labelCorSelecionada.config(text=f"Cor selecionada: {cor.get()}")

# Cria a janela principal
janela = Tk()
janela.geometry('400x300')
janela.title('Escolha sua cor favorita')

# Variável para armazenar a cor selecionada
cor = StringVar(janela, 0)
#cor.set("Azul")  # Define a cor padrão selecionada

# Cria e posiciona os RadioButtons
radioAzul = Radiobutton(janela, text='Azul', variable=cor, value='Azul', command=atualizarLabel)
radioAzul.pack(anchor='w', padx=20, pady=5)

radioVermelho = Radiobutton(janela, text='Vermelho', variable=cor, value='Vermelho', command=atualizarLabel)
radioVermelho.pack(anchor='w', padx=20, pady=5)

radioVerde = Radiobutton(janela, text='Verde', variable=cor, value='Verde', command=atualizarLabel)
radioVerde.pack(anchor='w', padx=20, pady=5)

radioAmarelo = Radiobutton(janela, text='Amarelo', variable=cor, value='Amarelo', command=atualizarLabel)
radioAmarelo.pack(anchor='w', padx=20, pady=5)

# Cria e posiciona o rótulo para mostrar a cor selecionada
labelCorSelecionada = Label(janela, text="Cor selecionada: ", font=('Arial', 14))
labelCorSelecionada.pack(pady=20)

# Inicia o loop principal da interface gráfica
janela.mainloop()
