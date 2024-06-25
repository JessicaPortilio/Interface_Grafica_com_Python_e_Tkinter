from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Loop para criar a grade 3x3
for linha in range(3):
    for coluna in range(3):
        # Cria um frame com borda levantada (RAISED) e largura da borda de 1
        tabela = Frame(
            master=janela,
            relief=RAISED,
            borderwidth=1
        )
        # Posiciona o frame na grade usando grid layout
        tabela.grid(row=linha, column=coluna, padx=10, pady=10, sticky='nsew')# Adiciona espaços entre as células e centraliza
        
        # Cria um rótulo dentro do frame com informações de linha e coluna
        texto = Label(master=tabela, text=f'Linha: {linha}\nColuna: {coluna}', padx=20, pady=20, justify=CENTER)
        texto.pack(fill=BOTH, expand=True)  # Adiciona o rótulo ao frame e define espaços internos

# Configura o redimensionamento das linhas e colunas para preencher a janela
# for i in range(3):
#     janela.grid_rowconfigure(i, weight=1)    # Configuração de peso para linhas
#     janela.grid_columnconfigure(i, weight=1) # Configuração de peso para colunas

# Entra no loop principal da aplicação.
janela.mainloop()
