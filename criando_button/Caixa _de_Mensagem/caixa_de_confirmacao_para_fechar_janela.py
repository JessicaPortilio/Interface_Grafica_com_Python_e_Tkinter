from tkinter import *
from tkinter import messagebox

# Função para verificar se o usuário deseja fechar a janela
def verificar_fechar_janela():
    # Exibe uma caixa de diálogo askquestion com a pergunta
    resposta = messagebox.askquestion("Fechar Janela", "Deseja realmente fechar a janela?")
    
    # Verifica a resposta do usuário
    if resposta == 'yes':
        janela.quit()  # Fecha a janela se o usuário escolher 'Sim'

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de askquestion()")

# Texto informativo na janela
texto = Label(janela, text="Pressione o botão 'Fechar' para ver a caixa de diálogo askquestion.")
texto.pack(padx=20, pady=20)

# Botão para fechar a janela
botao_fechar = Button(janela, text="Fechar", command=verificar_fechar_janela)
botao_fechar.pack(pady=10)

# Loop principal da aplicação
janela.mainloop()
