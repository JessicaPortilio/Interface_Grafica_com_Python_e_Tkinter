from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Define o tamanho da janela.
janela.geometry("620x200")

# Label e Entry para o Usuário
usuario_label = Label(janela, text='Usuário:', font=('Arial', 16))
# Posiciona o label do usuário na grade, linha 0, coluna 0, com padding e alinhamento à direita.
usuario_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

# Cria o campo de entrada de texto para o usuário.
usuario_entry = Entry(janela, font=('Lao UI', 12), width=50)
# Posiciona a entrada de texto do usuário na grade, linha 0, coluna 1, com padding.
usuario_entry.grid(row=0, column=1, padx=10, pady=10)

# Label e Entry para a Senha
senha_label = Label(janela, text='Senha:', font=('Arial', 16))
# Posiciona o label da senha na grade, linha 1, coluna 0, com padding e alinhamento à direita.
senha_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

# Cria o campo de entrada de texto para a senha, com o texto oculto.
senha_entry = Entry(janela, font=('Lao UI', 12), width=50, show='*')
# Posiciona a entrada de texto da senha na grade, linha 1, coluna 1, com padding.
senha_entry.grid(row=1, column=1, padx=10, pady=10)

# Função que será chamada ao clicar no botão "ENTRAR".
def entrar():
    nome = usuario_entry.get()  # Obtém o texto inserido no campo de usuário.
    senha = senha_entry.get()  # Obtém o texto inserido no campo de senha.
    
    # Verifica se o nome de usuário e senha estão corretos.
    if nome.lower() == 'jessica' and senha == '1234':
        # Exibe uma mensagem de boas-vindas se o login for bem-sucedido.
        messagebox.showinfo('Mensagem', f'Bem-vindo(a) ao sistema, {nome}!')
        # Limpa os campos de entrada após login bem-sucedido.
        usuario_entry.delete(0, END)
        senha_entry.delete(0, END)
    else:
        # Exibe uma mensagem de erro se o login falhar.
        messagebox.showerror('Erro', 'Usuário ou Senha incorretos!')
        # Limpa apenas o campo de senha após tentativa falhada.
        senha_entry.delete(0, END)

# Função que será chamada ao clicar no botão "SAIR" para fechar a janela.
def sair():
    janela.destroy()  # Fecha a janela principal.

# Cria um frame para conter os botões.
frame_botoes = Frame(janela)
# Posiciona o frame que contém os botões na grade, linha 2, coluna 0, abrangendo 2 colunas (columnspan=2), com padding vertical (pady).
frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)

# Botão de Entrar
entrar_button = Button(frame_botoes, text='ENTRAR', font=('Arial', 16, 'bold'), command=entrar)
# Adiciona o botão "ENTRAR" ao frame, posicionado à esquerda, com padding horizontal (padx).
entrar_button.pack(side=LEFT, padx=10)

# Botão de Sair
sair_button = Button(frame_botoes, text='SAIR', font=('Arial', 16, 'bold'), command=sair)
# Adiciona o botão "SAIR" ao frame, posicionado à direita, com padding horizontal (padx).
sair_button.pack(side=RIGHT, padx=10)

# Entra no loop principal da aplicação. Esse loop espera por eventos (como cliques de mouse, teclas pressionadas, etc.)
# e atualiza a interface em resposta a esses eventos. O método mainloop() mantém a janela aberta até que o usuário a feche.
janela.mainloop()
