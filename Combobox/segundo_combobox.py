from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Inicializa a janela principal da aplicação
janela = Tk()

# Define o tamanho da janela
janela.geometry('350x65')

# Define o título da janela
janela.title('Janela Principal')

# Cria e posiciona um rótulo (label) que pede para selecionar um mês
Label(janela, text='Selecione um mês: ', font=('Arial', 12)).grid(row=1, column=0)

# Cria uma caixa de seleção (combobox) para selecionar um mês
mesSelecionado = ttk.Combobox(janela, font=('Arial', 12))

# Define os valores possíveis para a combobox (os meses do ano)
mesSelecionado['values'] = ('Janeiro', 
                            'Fevereiro',
                            'Março',
                            'Abril',
                            'Maio',
                            'Junho',
                            'Julho',
                            'Agosto',
                            'Setembro',
                            'Outubro',
                            'Novembro',
                            'Dezembro')

# Posiciona a combobox na janela
mesSelecionado.grid(row=1, column=1)

# Define o mês selecionado por padrão como Maio (índice 4)
mesSelecionado.current(4)

# Função que exibe o mês selecionado no terminal
def itemSelecionado():
    print(str(mesSelecionado.get()))

# Cria um botão que, quando clicado, chama a função itemSelecionado
botaoSelecionado = Button(text='Item selecionado', font=('Arial', 12), command=itemSelecionado)

# Posiciona o botão na janela
botaoSelecionado.grid(row=2, column=0, columnspan=2, sticky='NEW')

# Entra no loop principal da aplicação
janela.mainloop()
