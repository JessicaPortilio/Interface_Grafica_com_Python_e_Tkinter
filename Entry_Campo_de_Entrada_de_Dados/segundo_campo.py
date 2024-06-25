from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Interface Gráfica')

# Define o tamanho da janela.
janela.geometry("720x520")

Usuario = Label(janela, text='Usuário: ', font=('Arial', 16))
# grid - Divide a tela em grades em partes
# stick - Usamos para preencher o item na tela ou seja, 
# esticamos o item para não ficar espaço vazio nas laterais
Usuario.grid(row=1, column=0, sticky='w')

campo_usuario = Entry(font=('Lao UI', 12), width=50)
campo_usuario.grid(row=1, column=1, sticky='w')

senha = Label(janela, text='Senha: ', font=('Arial', 16))
senha.grid(row=2, column=0, sticky='w')

campo_senha = Entry(janela, font=('Lao UI', 12), width=50)
campo_senha.grid(row=2, column=1, sticky='w')

def entrar():
    nome = str(campo_usuario.get())
    senha = str(campo_senha.get())
    
    if nome.lower() == 'jessica' and senha.lower() == '1234':
        messagebox.showinfo('Mensagem', f'Bem-vindo(a) ao sistema! {nome}')
    else:
        messagebox.showinfo('Mensagem', 'Usuário ou Senha incorreto!')
        
botao = Button(janela, text='ENTRAR', font=('Arial', 16, 'bold'), command=entrar)
botao.grid(row=3, column=1, sticky='w') 

# Entra no loop principal da aplicação.
janela.mainloop()