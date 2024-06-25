from tkinter import *
from PIL import ImageTk, Image

# Funções de exemplo para os botões
def exemplo_command():
    print("Botão clicado!")

# Inicializa a janela principal da aplicação.
janela = Tk()

# Define o título da janela.
janela.title('Exemplos de Botões Tkinter')

# Define o tamanho da janela.
janela.geometry("600x800")

# Cria um label de título.
titulo = Label(janela, text="Exemplos de Botões Tkinter", font=('Arial', 20, 'bold'))
titulo.pack(pady=10)

# 1. Activebackground
# Activebackground: Muda a cor de fundo do botão quando o mouse está sobre ele.
botao1 = Button(janela, text="Activebackground", activebackground="lightblue")
botao1.pack(pady=5)

# 2. Activeforeground
# Activeforeground: Muda a cor do texto do botão quando o mouse está sobre ele.
botao2 = Button(janela, text="Activeforeground", activeforeground="red")
botao2.pack(pady=5)

# 3. Bd
# Bd: Define a largura da borda do botão em pixels.
botao3 = Button(janela, text="Bd", bd=5)
botao3.pack(pady=5)

# 4. Bg
# Bg: Define a cor de fundo normal do botão.
botao4 = Button(janela, text="Bg", bg="yellow")
botao4.pack(pady=5)

# 5. Command
# Command: Especifica uma função a ser chamada quando o botão é clicado.
botao5 = Button(janela, text="Command", command=exemplo_command)
botao5.pack(pady=5)

# 6. Fg
# Fg: Define a cor do texto normal do botão.
botao6 = Button(janela, text="Fg", fg="green")
botao6.pack(pady=5)

# 7. Font
# Font: Define a fonte do texto no botão.
botao7 = Button(janela, text="Font", font=('Comic Sans MS', 16))
botao7.pack(pady=5)

# 8. Height
# Height: Define a altura do botão em linhas de texto (para texto) ou pixels (para imagens).
botao8 = Button(janela, text="Height", height=3)
botao8.pack(pady=5)

# 9. Highlightcolor
# Highlightcolor: Define a cor do destaque quando o botão tem foco.
botao9 = Button(janela, text="Highlightcolor", highlightcolor="purple")
botao9.pack(pady=5)

# 10. Image
# Image: Exibe uma imagem no botão ao invés de texto.
# Carrega a imagem original do arquivo 'sair.jpg'
imagem_original = Image.open('sair.jpg')
# Redimensiona a imagem para 150x50 pixels usando o método LANCZOS para uma alta qualidade de redimensionamento
imagem_redimensionada = imagem_original.resize((150, 50), Image.LANCZOS)
# Converte a imagem redimensionada para um objeto PhotoImage do Tkinter
imagem = ImageTk.PhotoImage(imagem_redimensionada)

botao10 = Button(janela, text="Image", image=imagem)
botao10.pack(pady=5)

# 11. Justify
#Justify: Alinha múltiplas linhas de texto no botão (esquerda, centro ou direita).
botao11 = Button(janela, text="esquerda\ncentro\ndireita", justify=LEFT)
botao11.pack(pady=5)

# 12. Padx
# Padx: Adiciona preenchimento extra à esquerda e à direita do texto.
botao12 = Button(janela, text="Padx", padx=20)
botao12.pack(pady=5)

# 13. Pady
# Pady: Adiciona preenchimento extra acima e abaixo do texto.
botao13 = Button(janela, text="Pady", pady=20)
botao13.pack(pady=5)

# 14. Relief
# Relief: Especifica o tipo de borda do botão (rebaixada, elevada, etc.).
botao14 = Button(janela, text="Relief", relief=SUNKEN)
botao14.pack(pady=5)

# 15. State
# State: Define o estado do botão (desativado, ativo, normal).
botao15 = Button(janela, text="State", state=DISABLED)
botao15.pack(pady=5)

# 16. Underline
# Underline: Sublinha o caractere especificado do texto no botão.
botao16 = Button(janela, text="Underline", underline=0)
botao16.pack(pady=5)

# 17. Width
# Width: Define a largura do botão em caracteres (para texto) ou pixels (para imagens).
botao17 = Button(janela, text="Width", width=20)
botao17.pack(pady=5)

# 18. Wraplength
# Wraplength: Define o comprimento em pixels para quebra de linha do texto no botão.
botao18 = Button(janela, text="Define o comprimento em pixels para quebra de linha do texto no botão.", wraplength=100)
botao18.pack(pady=5)

# Botão 4: Texto "Desativado", estado desativado (DISABLED), cursor mudado para "watch"
botao19 = Button(janela, text="Desativado, Modificando Cursor", state=DISABLED, cursor="watch")
botao19.pack(pady=5)

# Entra no loop principal da aplicação.
janela.mainloop()
