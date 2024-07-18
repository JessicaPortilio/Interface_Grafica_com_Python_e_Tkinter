from tkinter import *  # Importa todas as classes e funções do módulo tkinter
from tkinter import messagebox  # Importa a função messagebox do módulo tkinter

# Função para exibir uma mensagem com os dados preenchidos
def enviar():
    nome = entrada_nome.get()  # Obtém o texto inserido no campo de nome
    email = entrada_email.get()  # Obtém o texto inserido no campo de email
    senha = entrada_senha.get()  # Obtém o texto inserido no campo de senha
    sexo_f = var_sexo_f.get()  # Obtém o valor booleano do checkbutton de sexo feminino
    sexo_m = var_sexo_m.get()  # Obtém o valor booleano do checkbutton de sexo masculino
    
    # Determina o sexo selecionado com base nos valores dos checkbuttons
    sexo = 'F' if sexo_f else 'M' if sexo_m else 'Não selecionado'
    
    # Exibe uma mensagem informativa com os dados preenchidos
    messagebox.showinfo('Informações', f'Nome: {nome}\nEmail: {email}\nSenha: {senha}\nSexo: {sexo}')

# Função para alternar a seleção dos checkbuttons de sexo feminino
def toggle_f():
    if var_sexo_f.get():  # Se o checkbutton de sexo feminino estiver selecionado
        cb_masculino.deselect()  # Desseleciona o checkbutton de sexo masculino
        cb_masculino.config(state=DISABLED)  # Desabilita o checkbutton de sexo masculino
    else:
        cb_masculino.config(state=NORMAL)  # Habilita o checkbutton de sexo masculino

# Função para alternar a seleção dos checkbuttons de sexo masculino
def toggle_m():
    if var_sexo_m.get():  # Se o checkbutton de sexo masculino estiver selecionado
        # Limpa (desliga) o botão de seleção.
        cb_feminino.deselect()  # Desseleciona o checkbutton de sexo feminino
        cb_feminino.config(state=DISABLED)  # Desabilita o checkbutton de sexo feminino
    else:
        cb_feminino.config(state=NORMAL)  # Habilita o checkbutton de sexo feminino

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title('Formulário')  # Define o título da janela

janela.geometry('380x150')

# Campo de nome
Label(janela, text='Nome:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)  # Cria um rótulo para o nome
entrada_nome = Entry(janela, width=30, bd=5, font=('Lao UI', 12))  # Cria um campo de entrada para o nome
entrada_nome.grid(row=0, column=1)  # Posiciona o campo de entrada na janela

# Campo de email
Label(janela, text='Email:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)  # Cria um rótulo para o email
entrada_email = Entry(janela, width=30, bd=5, font=('Lao UI', 12))  # Cria um campo de entrada para o email
entrada_email.grid(row=1, column=1)  # Posiciona o campo de entrada na janela

# Campo de senha
Label(janela, text='Senha:', font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5)  # Cria um rótulo para a senha
entrada_senha = Entry(janela, width=30, show='*', bd=5, font=('Lao UI', 12))  # Cria um campo de entrada para a senha, ocultando os caracteres
entrada_senha.grid(row=2, column=1)  # Posiciona o campo de entrada na janela

frame_sexo = Frame(janela)
frame_sexo.grid(row=3, column=0, columnspan=2, padx=5, pady=5)  # Cria um rótulo para o sexo

# Checkbuttons para o sexo
Label(frame_sexo, text='Sexo:', font=('Arial', 12)).pack(side=LEFT,)

var_sexo_f = BooleanVar()  # Cria uma variável de controle para o checkbutton feminino
var_sexo_m = BooleanVar()  # Cria uma variável de controle para o checkbutton masculino

# Cria um checkbutton para sexo feminino e define a função de comando
cb_feminino = Checkbutton(frame_sexo, text='F', variable=var_sexo_f, font=('Arial', 12), command=toggle_f)
cb_feminino.pack(side=LEFT)  # Posiciona o checkbutton na janela

# Cria um checkbutton para sexo masculino e define a função de comando
cb_masculino = Checkbutton(frame_sexo, text='M', variable=var_sexo_m, font=('Arial', 12), command=toggle_m)
cb_masculino.pack(side=LEFT)  # Posiciona o checkbutton na janela

# Botão de enviar
botao_enviar = Button(janela, text='Enviar', command=enviar)  # Cria um botão para enviar os dados preenchidos
botao_enviar.grid(row=4, column=0, columnspan=2, pady=10)  # Posiciona o botão na janela

# Entra no loop principal da aplicação
janela.mainloop()