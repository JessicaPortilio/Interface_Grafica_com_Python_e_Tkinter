from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de Caixa de Mensagem")

def mostrar_erro():
    messagebox.showerror("Erro", "Este é um exemplo de mensagem de erro.")

botao_erro = Button(janela, text="Mostrar Erro", command=mostrar_erro)
botao_erro.pack(pady=20)

# Loop principal da aplicação
janela.mainloop()