from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Função para exibir a linguagem de programação selecionada
def mostrarSelecao():
    linguagem = combobox.get()
    messagebox.showinfo("Linguagem Selecionada", f"Sua linguagem de programação favorita é: {linguagem}")

# Inicializa a janela principal da aplicação
janela = Tk()

# Define o tamanho da janela
janela.geometry('400x200')

# Define o título da janela
janela.title('Seleção de Linguagem de Programação')

# Cria e posiciona um rótulo (label) para instruir o usuário
Label(janela, text='Selecione sua linguagem de programação favorita:', font=('Arial', 12)).pack(pady=10)

# Cria uma combobox para seleção de linguagens de programação
combobox = ttk.Combobox(janela, font=('Arial', 12))
combobox['values'] = ('Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'C#', 'Go', 'Swift', 'Kotlin')

# Posiciona a combobox na janela
combobox.pack(pady=5)

# Define um valor padrão
combobox.current(0)

# Cria um botão que, quando clicado, chama a função mostrarSelecao
botao = Button(janela, text='Mostrar Seleção', font=('Arial', 12), command=mostrarSelecao)
botao.pack(pady=20)

# Entra no loop principal da aplicação
janela.mainloop()
