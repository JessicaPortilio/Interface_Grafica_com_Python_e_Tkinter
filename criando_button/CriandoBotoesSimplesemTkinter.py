# A classe Button é utilizada para criar botões em Tkinter. 
# A sintaxe básica para criar um botão é:
# botao = Button(master, options)
# master: É o widget pai onde o botão será colocado, 
# geralmente a janela principal (janela).
# options: São opções de configuração para personalizar o botão, 
# como texto (text), cor de fundo (bg), cor do texto (fg), 
# entre outros.

from tkinter import *

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title("Exemplo de Botões")

# Função para mostrar uma mensagem ao clicar no botão
def botao_clicado():
    print("Botão Clicado!")

# Criando botão simples com texto "Clique Aqui"
# command - executa uma ação
botao1 = Button(janela, text="Clique Aqui", command=botao_clicado)
botao1.pack(pady=10)  # Adiciona o botão à janela com um espaço de 10 pixels acima e abaixo

# Criando outro botão com texto personalizado e cor de fundo
botao2 = Button(janela, text="Clique-me", bg="blue", fg="white", command=botao_clicado)
botao2.pack(pady=10)  # Adiciona o botão à janela com um espaço de 10 pixels acima e abaixo

# Loop principal da aplicação
janela.mainloop()
