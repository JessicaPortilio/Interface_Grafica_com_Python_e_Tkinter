from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Inicializa a janela principal da aplicação
janela = Tk()

# Define o tamanho da janela
janela.geometry('300x300')

# Define o título da janela
janela.title('Janela Principal')

# Cria e posiciona um rótulo (label) com o texto "Lista de Nomes"
textoDiaDaSemana = Label(janela, text='Lista de Nomes', font=('Arial', 14))
textoDiaDaSemana.pack()

# Define uma lista de nomes
listaNomes = ('Ana', 'Amanda', 'Cesar', 'Pedro', 'Allan', 'Carlos', 'Marcos', 'Roger', 'Emile')

# Cria uma variável para armazenar a lista de nomes
variavelNomes = Variable(value=listaNomes)

# Cria uma Listbox para listar os nomes, com fonte Arial tamanho 14, altura de 6 linhas visíveis, e modo de seleção única
listBox = Listbox(janela, font=('Arial', 14), listvariable=variavelNomes, height=6, selectmode=SINGLE) # BROESE, SINGLE, MULTIPLE, EXTENDED
# Este comando faz com que a Listbox se expanda para ocupar todo o espaço disponível na janela, tanto na largura quanto na altura, 
# e se redimensione conforme a janela é redimensionada.
listBox.pack(expand=True, fill=BOTH)

# Função para exibir o item selecionado quando um item da Listbox é clicado
def itemSelecionado(evento):
    # Obtém o índice do item selecionado
    indiceSelecionado = listBox.curselection()
    
    # Obtém o nome correspondente ao índice selecionado
    # Este comando cria uma string contendo todos os itens selecionados na Listbox, separados por vírgulas.
    item = ','.join([listBox.get(posicao) for posicao in indiceSelecionado])
    
    # Cria uma mensagem para exibir o item selecionado
    mensagem = 'Você selecionou ' + item
    
    # Exibe uma messagebox com a mensagem do item selecionado
    messagebox.showinfo('Atenção!', mensagem)

# Vincula a função itemSelecionado ao evento de seleção de item da Listbox
listBox.bind('<<ListboxSelect>>', itemSelecionado)
# Este comando vincula o evento de seleção de item da Listbox (<<ListboxSelect>>) à função itemSelecionado. 
# Assim, sempre que um item na Listbox é selecionado ou desselecionado, a função itemSelecionado é chamada.

# Entra no loop principal da aplicação
janela.mainloop()
