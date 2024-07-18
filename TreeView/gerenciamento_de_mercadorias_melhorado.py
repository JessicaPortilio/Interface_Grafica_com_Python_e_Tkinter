# Importa os módulos necessários do tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Cria a janela principal
janela = Tk()
janela.geometry('900x500')  # Define o tamanho da janela
janela.title('Gerenciamento de Mercadorias')  # Define o título da janela

# Função para verificar se todos os campos estão preenchidos
def verificarCampos():
    return campoID.get() and campoNome.get() and campoQuantidade.get() and campoPreco.get()

# Função para adicionar itens na Treeview
def addItemTreeView():
    if verificarCampos():
        # Insere um novo item na Treeview com os valores dos campos de entrada
        treeViewDados.insert('', 'end', values=(str(campoID.get()), str(campoNome.get()), campoQuantidade.get(), campoPreco.get()))
        # Limpa os campos de entrada após a inserção
        campoID.delete(0, END)
        campoNome.delete(0, END)
        campoQuantidade.delete(0, END)
        campoPreco.delete(0, END)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")

# Função para deletar itens da Treeview
def deleteItemTreeView():
    itemSelecionado = treeViewDados.selection()
    if itemSelecionado:
        # Deleta cada item selecionado na Treeview
        for item in itemSelecionado:
            treeViewDados.delete(item)
        campoID.delete(0, END)
        campoNome.delete(0, END)
        campoQuantidade.delete(0, END)
        campoPreco.delete(0, END)
    else:
        messagebox.showerror("Erro", "Nenhum item selecionado para exclusão")

# Função para preencher campos com dados do item selecionado
def preencherCamposComItemSelecionado(event):
    itemSelecionado = treeViewDados.selection()
    if itemSelecionado:
        item = treeViewDados.item(itemSelecionado[0], 'values')
        campoID.delete(0, END)
        campoID.insert(0, item[0])
        campoNome.delete(0, END)
        campoNome.insert(0, item[1])
        campoQuantidade.delete(0, END)
        campoQuantidade.insert(0, item[2])
        campoPreco.delete(0, END)
        campoPreco.insert(0, item[3])
    

# Função para alterar itens na Treeview
def alterarItemTreeView():
    itemSelecionado = treeViewDados.selection()
    if itemSelecionado:
        if verificarCampos():
            # Altera o item selecionado na Treeview com os novos valores dos campos de entrada
            for item in itemSelecionado:
                treeViewDados.item(item, values=(str(campoID.get()), str(campoNome.get()), campoQuantidade.get(), campoPreco.get()))
            # Limpa os campos de entrada após a alteração
            campoID.delete(0, END)
            campoNome.delete(0, END)
            campoQuantidade.delete(0, END)
            campoPreco.delete(0, END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
    else:
        messagebox.showerror("Erro", "Nenhum item selecionado para alteração")

# Cria o frame para entrada de dados e botões
frameEntrada = Frame(janela, pady=10, padx=10)  # Cria um frame dentro da janela com padding
frameEntrada.pack(fill=X)  # Faz o frame se ajustar na largura da janela

# Cria um título para a seção de entrada de dados
titulo = Label(frameEntrada, text='Entrada de Dados de Mercadorias', font=('Arial', 16, 'bold'))
titulo.grid(row=0, column=0, columnspan=4, pady=10)  # Define a posição e o tamanho do título

# Cria labels e campos de entrada para ID, Nome, Quantidade e Preço
idLabel = Label(frameEntrada, text='ID', font=('Arial', 12))
idLabel.grid(row=1, column=0, sticky='E', padx=5, pady=5)

campoID = Entry(frameEntrada, font=('Arial', 12), width=70)
campoID.grid(row=1, column=1, sticky='W', padx=5, pady=5)

nomeLabel = Label(frameEntrada, text='Nome', font=('Arial', 12))
nomeLabel.grid(row=2, column=0, sticky='E', padx=5, pady=5)

campoNome = Entry(frameEntrada, font=('Arial', 12), width=70)
campoNome.grid(row=2, column=1, sticky='W', padx=5, pady=5)

quantidadeLabel = Label(frameEntrada, text='Quantidade', font=('Arial', 12))
quantidadeLabel.grid(row=3, column=0, sticky='E', padx=5, pady=5)

campoQuantidade = Entry(frameEntrada, font=('Arial', 12), width=70)
campoQuantidade.grid(row=3, column=1, sticky='W', padx=5, pady=5)

precoLabel = Label(frameEntrada, text='Preço', font=('Arial', 12))
precoLabel.grid(row=4, column=0, sticky='E', padx=5, pady=5)

campoPreco = Entry(frameEntrada, font=('Arial', 12), width=70)
campoPreco.grid(row=4, column=1, sticky='W', padx=5, pady=5)

# Ajusta os botões para ocuparem mais espaço na grade
botaoAdicionar = Button(frameEntrada, text='Adicionar', font=('Arial', 12), command=addItemTreeView)
botaoAdicionar.grid(row=1, column=2, pady=5, padx=10, sticky='NSEW', rowspan=1, columnspan=1)

botaoDeletar = Button(frameEntrada, text='Deletar', font=('Arial', 12), command=deleteItemTreeView)
botaoDeletar.grid(row=2, column=2, pady=5, padx=10, sticky='NSEW', rowspan=1, columnspan=1)

botaoAlterar = Button(frameEntrada, text='Alterar', font=('Arial', 12), command=alterarItemTreeView)
botaoAlterar.grid(row=3, column=2, pady=5, padx=10, sticky='NSEW', rowspan=1, columnspan=1)


# Define o estilo para a Treeview
estiloDaTreeView = ttk.Style()
estiloDaTreeView.theme_use('alt')
estiloDaTreeView.configure('.', font=('Arial', 14))

# Cria o frame para a visualização dos dados
frameVisualizacao = Frame(janela, pady=10, padx=10)
frameVisualizacao.pack(fill=BOTH, expand=True)  # Expande o frame para preencher o espaço disponível

# Cria a Treeview com colunas para ID, Nome, Quantidade e Preço
treeViewDados = ttk.Treeview(frameVisualizacao, columns=(1, 2, 3, 4), show='headings')
treeViewDados.column('1', anchor=CENTER)
treeViewDados.heading('1', text='ID')

treeViewDados.column('2', anchor=CENTER)
treeViewDados.heading('2', text='Nome')

treeViewDados.column('3', anchor=CENTER)
treeViewDados.heading('3', text='Quantidade')

treeViewDados.column('4', anchor=CENTER)
treeViewDados.heading('4', text='Preço')

# Insere alguns dados de exemplo na Treeview
# Insere produtos reais na Treeview
treeViewDados.insert('', 'end', values=('1', 'Smartphone Samsung Galaxy S21', 20, 2399.99))
treeViewDados.insert('', 'end', values=('2', 'Notebook Dell Inspiron 15', 15, 3499.00))
treeViewDados.insert('', 'end', values=('3', 'Smart TV LG 55" 4K', 10, 2799.90))
treeViewDados.insert('', 'end', values=('4', 'Fone de Ouvido Sony WH-1000XM4', 30, 1499.99))
treeViewDados.insert('', 'end', values=('5', 'Console PlayStation 5', 5, 4999.00))

treeViewDados.bind('<ButtonRelease-1>', preencherCamposComItemSelecionado)  # Liga o evento de clique na Treeview à função

treeViewDados.pack(fill=BOTH, expand=True)  # Expande a Treeview para preencher o espaço disponível

# Inicia o loop principal da interface gráfica
janela.mainloop()
