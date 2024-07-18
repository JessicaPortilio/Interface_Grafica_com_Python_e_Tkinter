from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from openpyxl import load_workbook
import os

# Cria uma nova janela Tkinter
janela = Tk()

# Define as dimensões da janela principal
janela.geometry('900x350')

# Define o título da janela principal
janela.title('Janela Principal')

# grid - Divide a tela em grades / partes
# sticky - Usamos para preencher o item na tela ou seja, esticamos o item para não ficar espaço vazio nas Linhas (Norte, Sul, Leste e Oeste - NSEW)

# Cria um rótulo para o ID
id = Label(janela, text='ID', font=('Arial', 12))
# Posiciona o rótulo ID na grade
id.grid(row=1, column=0, sticky='W')

# Cria uma caixa de entrada para o ID
campoDigitadoID = Entry(janela, font=('Arial', 12))
# Posiciona a caixa de entrada ID na grade
campoDigitadoID.grid(row=1, column=1, sticky='W')

# Cria um rótulo para o Nome
nome = Label(janela, text='Nome', font=('Arial', 12))
# Posiciona o rótulo Nome na grade
nome.grid(row=1, column=2, sticky='W')

# Cria uma caixa de entrada para o Nome
campoDigitadoNome = Entry(janela, font=('Arial', 12))
# Posiciona a caixa de entrada Nome na grade
campoDigitadoNome.grid(row=1, column=3, sticky='W')

# Cria um rótulo para a Idade
idade = Label(janela, text='Idade', font=('Arial', 12))
# Posiciona o rótulo Idade na grade
idade.grid(row=1, column=4, sticky='W')

# Cria uma caixa de entrada para a Idade
campoDigitadoIdade = Entry(janela, font=('Arial', 12))
# Posiciona a caixa de entrada Idade na grade
campoDigitadoIdade.grid(row=1, column=5, sticky='W')

# Cria um rótulo para o Sexo
sexo = Label(janela, text='Sexo', font=('Arial', 12))
# Posiciona o rótulo Sexo na grade
sexo.grid(row=1, column=6, sticky='W')

# Cria uma caixa de entrada para o Sexo
campoDigitadoSexo = Entry(janela, font=('Arial', 12))
# Posiciona a caixa de entrada Sexo na grade
campoDigitadoSexo.grid(row=1, column=7, sticky='W')


# Função para verificar se todos os campos estão preenchidos
def verificarCampos():
    return campoDigitadoID.get() and campoDigitadoNome.get() and campoDigitadoIdade.get() and campoDigitadoSexo.get()


# Função para adicionar itens na Treeview
def addItemTreeView():
    if verificarCampos():
        # Insere um novo item na Treeview com os valores das caixas de entrada
        treeViewDados.insert('', 'end', values=(str(campoDigitadoID.get()), str(campoDigitadoNome.get()), campoDigitadoIdade.get(), str(campoDigitadoSexo.get())))
        # Limpa as caixas de entrada após a inserção
        campoDigitadoID.delete(0, END)
        campoDigitadoNome.delete(0, END)
        campoDigitadoIdade.delete(0, END)
        campoDigitadoSexo.delete(0, END)
        contarNumeroLinhas()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")
        
# Função para deletar itens da Treeview
def deleteItemTreeView():
    # Obtém os itens selecionados
    itemSelecionado = treeViewDados.selection()
    if itemSelecionado:
        # Deleta cada item selecionado
        for item in itemSelecionado:
            treeViewDados.delete(item)
        contarNumeroLinhas()
    else:
        messagebox.showerror("Erro", "Nenhum item selecionado para exclusão")
        
# Função para alterar itens na Treeview
def alterarItemTreeView():
    # Obtém o primeiro item selecionado
    itemSelecionado = treeViewDados.selection()[0]
    if itemSelecionado:
        if verificarCampos():
            # Altera o item selecionado com os novos valores das caixas de entrada
            treeViewDados.item(itemSelecionado, values=(str(campoDigitadoID.get()), str(campoDigitadoNome.get()), campoDigitadoIdade.get(), str(campoDigitadoSexo.get())))
            
            # Limpa as caixas de entrada após a alteração
            campoDigitadoID.delete(0, END)
            campoDigitadoNome.delete(0, END)
            campoDigitadoIdade.delete(0, END)
            campoDigitadoSexo.delete(0, END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
    else:
        messagebox.showerror("Erro", "Nenhum item selecionado para alteração")

def exportarItemParaExcel():
    workbook = load_workbook(filename='D:\\Interface_Grafica_com_Python_e_Tkinter\\TreeView\\Exportando_Arquivo_Excel\\Arquivo.xlsx')
    sheet = workbook['Dados']
    sheet.append(['ID', 'Nome', 'Idade', 'Sexo'])
    for numeroLinhas in treeViewDados.get_children():
        linha = treeViewDados.item(numeroLinhas)['values']
        sheet.append(linha)
    
    workbook.save('Dados_Exportados.xlsx')
    print('Dados exportado com sucesso!')
    
# Cria um botão para cadastrar os dados
botaoAdicionar = Button(text='Cadastrar', font=('Arial', 16), command=addItemTreeView)
# Posiciona o botão Cadastrar na grade
botaoAdicionar.grid(row=2, column=0, columnspan=2, sticky='NSEW')

# Cria um botão para deletar os dados
botaoDeletar = Button(text='Deletar', font=('Arial', 16), command=deleteItemTreeView)
# Posiciona o botão Deletar na grade
botaoDeletar.grid(row=2, column=2, columnspan=2, sticky='NSEW')

# Cria um botão para alterar os dados
botaoAlterar = Button(text='Alterar', font=('Arial', 16), command=alterarItemTreeView)
# Posiciona o botão Alterar na grade
botaoAlterar.grid(row=2, column=4, columnspan=2, sticky='NSEW')

# Cria um botão para exportar os dados
botaoExportar = Button(text='Exportar', font=('Arial', 16), command=exportarItemParaExcel)
# Posiciona o botão exportar na grade
botaoExportar.grid(row=2, column=6, columnspan=2, sticky='NSEW')

# Define o estilo para a Treeview
estiloDaTreeView = ttk.Style()
# Usa o tema 'alt' para a Treeview
estiloDaTreeView.theme_use('alt')
# Configura o estilo da Treeview para usar a fonte Arial 14
estiloDaTreeView.configure('.', font=('Arial', 14))

# Cria a Treeview com colunas para ID, Nome, Idade e Sexo
treeViewDados = ttk.Treeview(janela, columns=(1, 2, 3, 4), show='headings')

# Define a coluna 1 (ID) com centralização
treeViewDados.column('1', anchor=CENTER)
# Define o cabeçalho da coluna 1 (ID)
treeViewDados.heading('1', text='ID')

# Define a coluna 2 (Nome) com centralização
treeViewDados.column('2', anchor=CENTER)
# Define o cabeçalho da coluna 2 (Nome)
treeViewDados.heading('2', text='Nome')

# Define a coluna 3 (Idade) com centralização
treeViewDados.column('3', anchor=CENTER)
# Define o cabeçalho da coluna 3 (Idade)
treeViewDados.heading('3', text='Idade')

# Define a coluna 4 (Sexo) com centralização
treeViewDados.column('4', anchor=CENTER)
# Define o cabeçalho da coluna 4 (Sexo)
treeViewDados.heading('4', text='Sexo')

# Insere alguns dados de exemplo na Treeview
treeViewDados.insert('', 'end', text='1', values=('1', 'Allan', 29, 'Masculino'))
treeViewDados.insert('', 'end', text='2', values=('2', 'Ana', 41, 'Feminino'))
treeViewDados.insert('', 'end', text='3', values=('3', 'Vanessa', 64, 'Feminino'))
treeViewDados.insert('', 'end', text='4', values=('4', 'Pedro', 19, 'Masculino'))
treeViewDados.insert('', 'end', text='5', values=('5', 'Thiago', 32, 'Masculino'))


# Posiciona a Treeview na grade
treeViewDados.grid(row=3, column=0, columnspan=8, sticky='NSEW')

# Função para contar o número de linhas na Treeview
def contarNumeroLinhas(item=''):
    numero = 0
    linhas = treeViewDados.get_children(item)
    
    for linha in linhas:
        numero += 1
    labelNumeroLinhas.config(text='Linhas: ' + str(numero))

# Cria um rótulo para mostrar o número de linhas
labelNumeroLinhas = Label(text='Linhas: ', font=('Arial', 12))
labelNumeroLinhas.grid(row=4, column=0, columnspan=8, sticky='W')

# Chama a função contarNumeroLinhas para exibir o número de linhas inicial
contarNumeroLinhas()

# Ajusta a grade para permitir que a Treeview se expanda
janela.grid_rowconfigure(4, weight=1)
janela.grid_columnconfigure(8, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()
