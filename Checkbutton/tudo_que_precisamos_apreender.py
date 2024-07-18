from tkinter import *
from PIL import ImageTk, Image

# Inicializa a janela principal da aplicação.
janela = Tk()
janela.title("Exemplos de Checkbuttons")
janela.geometry("700x900")

# Função de exemplo para ser chamada quando o estado do checkbutton mudar.
def exemplo_funcao():
    print("Estado do Checkbutton mudou!")

# 1. Activebackground - Cor de fundo quando o cursor está sobre o checkbutton.
# Activebackground: Muda a cor de fundo para azul claro quando o cursor está sobre o checkbutton.
# cb1 = Checkbutton(janela, text="Activebackground", activebackground="lightblue")
# cb1.pack(pady=5)

# 2. Activeforeground - Cor do texto quando o cursor está sobre o checkbutton.
# Activeforeground: Muda a cor do texto para vermelho quando o cursor está sobre o checkbutton.
# cb2 = Checkbutton(janela, text="Activeforeground", activeforeground="red")
# cb2.pack(pady=5)

# 3. Bg - Cor de fundo normal do checkbutton.
# Bg: Define a cor de fundo do checkbutton como amarelo.
# cb3 = Checkbutton(janela, text="Bg", bg="yellow")
# cb3.pack(pady=5)

# 4. Bitmap - Exibe uma imagem monocromática no checkbutton.
# Bitmap: Exibe uma imagem monocromática (ícone de informação) no checkbutton.
# cb4 = Checkbutton(janela, text="Bitmap", bitmap="info")
# cb4.pack(pady=5)

# 5. Bd - Tamanho da borda ao redor do indicador.
# Bd: Define uma borda de 5 pixels ao redor do checkbutton.
# cb5 = Checkbutton(janela, text="Bd", bd=5, relief=SOLID)
# cb5.pack(pady=5)

# 6. Command - Função a ser chamada quando o estado do checkbutton mudar.
# Command: Chama a função exemplo_funcao quando o estado do checkbutton muda.
# cb6 = Checkbutton(janela, text="Command", command=exemplo_funcao)
# cb6.pack(pady=5)

# 7. Cursor - Muda o cursor do mouse quando está sobre o checkbutton.
# Cursor: Muda o cursor do mouse para uma mão quando está sobre o checkbutton.
# cb7 = Checkbutton(janela, text="Cursor", cursor="hand2")
# cb7.pack(pady=5)

# 8. Disabledforeground - Cor do texto quando o checkbutton está desabilitado.
# Disabledforeground: Define a cor do texto como cinza quando o checkbutton está desabilitado.
# cb8 = Checkbutton(janela, text="Disabledforeground", disabledforeground="gray", state=DISABLED)
# cb8.pack(pady=5)

# 9. Font - Define a fonte do texto do checkbutton.
# Font: Define a fonte do texto como Arial de tamanho 16.
# cb9 = Checkbutton(janela, text="Font", font=("Arial", 16))
# cb9.pack(pady=5)

# 10. Fg - Cor do texto.
# Fg: Define a cor do texto como verde.
# cb10 = Checkbutton(janela, text="Fg", fg="green")
# cb10.pack(pady=5)

# 11. Height - Número de linhas de texto no checkbutton.
# Height: Define o número de linhas de texto no checkbutton como 3.
# cb11 = Checkbutton(janela, text="Height", height=3)
# cb11.pack(pady=5)

# 12. Highlightcolor - Cor do destaque quando o checkbutton tem foco.
# Highlightcolor: Define a cor de destaque como azul quando o checkbutton tem foco.
# cb12 = Checkbutton(janela, text="Highlightcolor", highlightcolor="blue")
# cb12.pack(pady=5)

# 13. Image - Exibe uma imagem no checkbutton.
# Certifique-se de ter uma imagem chamada "imagem.png" no mesmo diretório que o script.
# Image: Exibe uma imagem no checkbutton.
# Carrega a imagem original do arquivo 'sair.jpg'
imagem_original = Image.open('sair.jpg')
# Redimensiona a imagem para 150x50 pixels usando o método LANCZOS para uma alta qualidade de redimensionamento
imagem_redimensionada = imagem_original.resize((150, 50), Image.LANCZOS)
# Converte a imagem redimensionada para um objeto PhotoImage do Tkinter
imagem = ImageTk.PhotoImage(imagem_redimensionada)
# cb13 = Checkbutton(janela, image=imagem)
# cb13.pack(pady=5)

# 14. Justify - Como múltiplas linhas de texto serão alinhadas.
# Justify: Alinha múltiplas linhas de texto à esquerda.
cb14 = Checkbutton(janela, text="Justify\nLeft Aligned", justify=LEFT)
cb14.pack(pady=5)

# 15. Offvalue - Valor quando o checkbutton está desmarcado.
# Offvalue: Define o valor da variável de controle como "No" quando o checkbutton está desmarcado.
var15 = StringVar(value="No")
cb15 = Checkbutton(janela, text="Offvalue", variable=var15, onvalue="Yes", offvalue="No")
cb15.pack(pady=5)


# 16. Onvalue - Valor quando o checkbutton está marcado.
# Onvalue: Define o valor da variável de controle como "Yes" quando o checkbutton está marcado.
var16 = StringVar(value="No")
cb16 = Checkbutton(janela, text="Onvalue", variable=var16, onvalue="Yes", offvalue="No")
cb16.pack(pady=5)

# 17. Padx - Espaço à esquerda e à direita do texto.
# Padx: Adiciona espaço extra à esquerda e à direita do texto.
cb17 = Checkbutton(janela, text="Padx", padx=20)
cb17.pack(pady=5)

# 18. Pady - Espaço acima e abaixo do texto.
# Pady: Adiciona espaço extra acima e abaixo do texto.
cb18 = Checkbutton(janela, text="Pady", pady=20)
cb18.pack(pady=5)

# 19. Relief - Aparência da borda do checkbutton.
# Relief: Define a aparência da borda do checkbutton como "groove" (entalhado).
cb19 = Checkbutton(janela, text="Relief", relief=GROOVE)
cb19.pack(pady=5)

# 20. Selectcolor - Cor do checkbutton quando está marcado.
# Selectcolor: Define a cor do checkbutton como vermelho quando está marcado.
cb20 = Checkbutton(janela, text="Selectcolor", selectcolor="red")
cb20.pack(pady=5)

# 21. Selectimage - Imagem a ser exibida quando o checkbutton está marcado.
# Selectimage: Exibe uma imagem diferente quando o checkbutton está marcado.
# Certifique-se de ter uma imagem chamada "imagem_selecionada.png" no mesmo diretório que o script.
# Carrega a imagem original do arquivo 'sair.jpg'
imagem_original = Image.open('fundo.jpg')
# Redimensiona a imagem para 150x50 pixels usando o método LANCZOS para uma alta qualidade de redimensionamento
imagem_redimensionada = imagem_original.resize((150, 50), Image.LANCZOS)
# Converte a imagem redimensionada para um objeto PhotoImage do Tkinter
imagem_selecionada = ImageTk.PhotoImage(imagem_redimensionada)
cb21 = Checkbutton(janela, image=imagem, selectimage=imagem_selecionada)
cb21.pack(pady=5)

# 22. State - Estado do checkbutton (NORMAL, DISABLED, ACTIVE).
# State: Define o estado do checkbutton como desabilitado (DISABLED).
cb22 = Checkbutton(janela, text="State", state=DISABLED)
cb22.pack(pady=5)

# 23. Text - Texto exibido ao lado do checkbutton.
# Text: Exibe um texto com múltiplas linhas ao lado do checkbutton.
cb23 = Checkbutton(janela, text="Text\nMultiple Lines")
cb23.pack(pady=5)

# 24. Underline - Sublinha o caractere na posição especificada.
# Underline: Sublinha o terceiro caractere do texto.
cb24 = Checkbutton(janela, text="Underline", underline=2)
cb24.pack(pady=5)

# 25. Variable - Variável de controle que rastreia o estado do checkbutton.
# Variable: Define uma variável de controle que rastreia o estado do 
var25 = IntVar()
cb25 = Checkbutton(janela, text="Variable", variable=var25)
cb25.pack(pady=5)

# 26. Width - Largura do checkbutton em caracteres.
# Width: Define a largura do checkbutton em 20 caracteres.
cb26 = Checkbutton(janela, text="Width", width=20)
cb26.pack(pady=5)

# 27. Wraplength - Número máximo de caracteres por linha.
# Wraplength: Quebra o texto em várias linhas se ultrapassar 100 pixels de comprimento.
cb27 = Checkbutton(janela, text="Wraplength: Este texto será quebrado em várias linhas se ultrapassar 100 pixels de comprimento.", wraplength=100)
cb27.pack(pady=5)

# Inicia o loop principal da aplicação.
janela.mainloop()
