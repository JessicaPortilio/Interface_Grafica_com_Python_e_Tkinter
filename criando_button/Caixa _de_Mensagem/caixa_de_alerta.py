from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de Caixa de Mensagem")

def mostrar_alerta():
    messagebox.showwarning("Alerta", "Este é um exemplo de mensagem de alerta.")

botao_alerta = Button(janela, text="Mostrar Alerta", command=mostrar_alerta)
botao_alerta.pack(pady=20)


# Loop principal da aplicação
janela.mainloop()