from tkinter import *

# Inicializa a janela principal da aplicação.
janela = Tk()
janela.title("Exemplos de Checkbuttons")
janela.geometry("400x500")

# Função para atualizar o label com o valor atual da variável.
def atualizar_label(var, label):
    label.config(text=f"Valor: {var.get()}")

# 1. Método deselect() - Desmarca o checkbutton.
def exemplo_deselect():
    cb.deselect()
    atualizar_label(var, label)

# 2. Método flash() - Pisca o checkbutton entre suas cores ativa e normal.
def exemplo_flash():
    cb.flash()
    atualizar_label(var, label)

# 3. Método invoke() - Invoca o callback do checkbutton.
def exemplo_invoke():
    cb.invoke()
    atualizar_label(var, label)

# 4. Método select() - Marca o checkbutton.
def exemplo_select():
    cb.select()
    atualizar_label(var, label)

# 5. Método toggle() - Alterna o estado do checkbutton.
def exemplo_toggle():
    cb.toggle()
    atualizar_label(var, label)

# Variável de controle para o checkbutton.
var = IntVar()

# Checkbutton com a variável de controle.
cb = Checkbutton(janela, text="Exemplo de Checkbutton", variable=var, command=lambda: atualizar_label(var, label))
cb.pack(pady=10)

# Label para mostrar o valor atual da variável.
label = Label(janela, text=f"Valor: {var.get()}")
label.pack(pady=10)

# Botões para demonstrar os métodos do Checkbutton.
# deselect(): Desmarca o Checkbutton e atualiza o Label.
btn_deselect = Button(janela, text="deselect()", command=exemplo_deselect)
btn_deselect.pack(pady=5)

# flash(): Pisca o Checkbutton entre suas cores ativa e normal e atualiza o Label.
btn_flash = Button(janela, text="flash()", command=exemplo_flash)
btn_flash.pack(pady=5)

# invoke(): Simula um clique no Checkbutton, acionando seu comando e atualizando o Label.
btn_invoke = Button(janela, text="invoke()", command=exemplo_invoke)
btn_invoke.pack(pady=5)

# select(): Marca o Checkbutton e atualiza o Label.
btn_select = Button(janela, text="select()", command=exemplo_select)
btn_select.pack(pady=5)

# toggle(): Alterna o estado do Checkbutton entre marcado e desmarcado e atualiza o Label.
btn_toggle = Button(janela, text="toggle()", command=exemplo_toggle)
btn_toggle.pack(pady=5)

# Inicia o loop principal da aplicação.
janela.mainloop()
