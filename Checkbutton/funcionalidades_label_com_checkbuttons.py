from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()
janela.title("Exemplos de Checkbuttons")
janela.geometry("700x900")

# Função de exemplo para ser chamada quando o estado do checkbutton mudar.
def exemplo_funcao():
        print("Estado do Checkbutton mudou!")

# Atualiza o label de acordo com o valor da variável.
def atualizar_label(var, label):
        label.config(text=f"Valor: {var.get()}")


# 15. Offvalue - Valor quando o checkbutton está desmarcado.
var15 = StringVar(value="No")
cb15 = Checkbutton(janela, text="Offvalue", variable=var15, onvalue="Yes", offvalue="No", 
        command=lambda: atualizar_label(var15, label15))
cb15.pack(pady=5)
label15 = Label(janela, text=f"Valor: {var15.get()}")
label15.pack(pady=5)

# 16. Onvalue - Valor quando o checkbutton está marcado.
var16 = StringVar(value="No")
cb16 = Checkbutton(janela, text="Onvalue", variable=var16, onvalue="Yes", offvalue="No",
        command=lambda: atualizar_label(var16, label16))
cb16.pack(pady=5)
label16 = Label(janela, text=f"Valor: {var16.get()}")
label16.pack(pady=5)

# 25. Variable - Variável de controle que rastreia o estado do checkbutton.
var25 = IntVar()
cb25 = Checkbutton(janela, text="Variable", variable=var25, 
        command=lambda: atualizar_label(var25, label25))
cb25.pack(pady=5)
label25 = Label(janela, text=f"Valor: {var25.get()}")
label25.pack(pady=5)

# Inicia o loop principal da aplicação.
janela.mainloop()