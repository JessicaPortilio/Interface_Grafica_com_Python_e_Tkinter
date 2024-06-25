from tkinter import *
from tkinter import messagebox

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de Caixa de Mensagem")

def verificar_saida():
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
    if resposta:
        janela.quit()

botao_sair = Button(janela, text="Sair", command=verificar_saida)
botao_sair.pack(pady=20)


# Loop principal da aplicação
janela.mainloop()