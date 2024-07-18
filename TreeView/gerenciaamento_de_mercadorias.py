from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Cria uma nova janela Tkinter
janela = Tk()

# Define as dimensões da janela principal
janela.geometry('950x300')

# Define o título da janela principal
janela.title('Gerenciamento de Mercadorias')

# Função para verificar se todos os campos estão preenchidos
def verificarCampos():
    return campoID.get() and campoNome.get() and campoQuantidade.get() and campoPreco.get()

# Função para adicionar itens na Treeview
def addItemTreeView():
    if verificarCampos():
        treeViewDados.insert('', 'end', values=(str(campoID.get()), str(campoNome.get()), campoQuantidade.get(), campoPreco.get()))
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
        for item in itemSelecionado:
            treeViewDados.delete(item)
    else:
        messagebox.showerror("Erro", "Nenhum item selecionado para exclusão")

# Função para alterar itens na Treeview
def alterarItemTreeView():
    itemSelecionado = treeViewDados.selection()
    if itemSelecionado:
        if verificarCampos():
            for item in itemSelecionado:
                treeViewDados.item(item, values=(str(campoID.get()), str(campoNome.get()), campoQuantidade.get(), campoPreco.get()))
            campoID.delete(0, END)
            campoNome.delete(0, END)
            campoQuantidade.delete(0, END)
            campoPreco.delete(0, END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
    else:
        messagebox.showerror("Erro", "Nenhum item selecionado para alteração")

# Cria os rótulos e campos de entrada
idLabel = Label(janela, text='ID', font=('Arial', 12))
idLabel.grid(row=1, column=0, sticky='W')

campoID = Entry(janela, font=('Arial', 12))
campoID.grid(row=1, column=1, sticky='W')

nomeLabel = Label(janela, text='Nome', font=('Arial', 12))
nomeLabel.grid(row=1, column=2, sticky='W')

campoNome = Entry(janela, font=('Arial', 12))
campoNome.grid(row=1, column=3, sticky='W')

quantidadeLabel = Label(janela, text='Quantidade', font=('Arial', 12))
quantidadeLabel.grid(row=1, column=4, sticky='W')

campoQuantidade = Entry(janela, font=('Arial', 12))
campoQuantidade.grid(row=1, column=5, sticky='W')

precoLabel = Label(janela, text='Preço', font=('Arial', 12))
precoLabel.grid(row=1, column=6, sticky='W')

campoPreco = Entry(janela, font=('Arial', 12))
campoPreco.grid(row=1, column=7, sticky='W')

# Cria os botões
botaoAdicionar = Button(janela, text='Adicionar', font=('Arial', 16), command=addItemTreeView)
botaoAdicionar.grid(row=2, column=0, columnspan=2, sticky='NSEW')

botaoDeletar = Button(janela, text='Deletar', font=('Arial', 16), command=deleteItemTreeView)
botaoDeletar.grid(row=2, column=2, columnspan=2, sticky='NSEW')

botaoAlterar = Button(janela, text='Alterar', font=('Arial', 16), command=alterarItemTreeView)
botaoAlterar.grid(row=2, column=4, columnspan=2, sticky='NSEW')

# Define o estilo para a Treeview
estiloDaTreeView = ttk.Style()
estiloDaTreeView.theme_use('alt')
estiloDaTreeView.configure('.', font=('Arial', 14))

# Cria a Treeview com colunas para ID, Nome, Quantidade e Preço
treeViewDados = ttk.Treeview(janela, columns=(1, 2, 3, 4), show='headings')
treeViewDados.column('1', anchor=CENTER)
treeViewDados.heading('1', text='ID')

treeViewDados.column('2', anchor=CENTER)
treeViewDados.heading('2', text='Nome')

treeViewDados.column('3', anchor=CENTER)
treeViewDados.heading('3', text='Quantidade')

treeViewDados.column('4', anchor=CENTER)
treeViewDados.heading('4', text='Preço')

# Insere alguns dados de exemplo na Treeview
treeViewDados.insert('', 'end', text='1', values=('1', 'Produto A', '50', '10.00'))
treeViewDados.insert('', 'end', text='2', values=('2', 'Produto B', '30', '15.00'))
treeViewDados.insert('', 'end', text='3', values=('3', 'Produto C', '20', '20.00'))
treeViewDados.insert('', 'end', text='4', values=('4', 'Produto D', '10', '25.00'))
treeViewDados.insert('', 'end', text='5', values=('5', 'Produto E', '5', '30.00'))

treeViewDados.grid(row=3, column=0, columnspan=8, sticky='NSEW')

# Ajusta a grade para permitir que a Treeview se expanda
janela.grid_rowconfigure(4, weight=1)
janela.grid_columnconfigure(8, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()
