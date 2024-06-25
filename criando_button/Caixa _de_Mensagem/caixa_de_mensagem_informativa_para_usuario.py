from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de Caixa de Mensagem")

# Função para exibir a caixa de mensagem
def mostrar_mensagem():
    messagebox.showinfo("Mensagem de Informação", "Este é um exemplo de mensagem informativa.")

# Cria um botão para exibir a mensagem
botao_info = Button(janela, text="Mostrar Mensagem", command=mostrar_mensagem)
botao_info.pack(pady=20)

# Loop principal da aplicação
janela.mainloop()
