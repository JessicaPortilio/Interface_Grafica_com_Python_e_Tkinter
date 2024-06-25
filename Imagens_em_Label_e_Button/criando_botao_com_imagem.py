from tkinter import *
from PIL import ImageTk, Image

# Inicializa a janela principal da aplicação
janela = Tk()
# Define o título da janela
janela.title('Interface Gráfica')

# Cria um rótulo de texto com fonte Times New Roman, tamanho 16, em negrito, e adiciona à janela
texto1 = Label(janela, text='Imagem', font=('Times New Roman', 16, 'bold'))
texto1.pack()  # Adiciona o rótulo à janela

# Carrega a imagem original do arquivo 'sair.jpg'
imagem_original = Image.open('sair.jpg')
# Redimensiona a imagem para 150x50 pixels usando o método LANCZOS para uma alta qualidade de redimensionamento
imagem_redimensionada = imagem_original.resize((150, 50), Image.LANCZOS)
# Converte a imagem redimensionada para um objeto PhotoImage do Tkinter
imagem = ImageTk.PhotoImage(imagem_redimensionada)

# Cria um botão com a imagem redimensionada
# O comando associado ao botão é janela.destroy, que fecha a janela quando o botão é clicado
botaoComImagem = Button(image=imagem, command=janela.destroy)
botaoComImagem.pack()  # Adiciona o botão à janela

# Inicia o loop principal da aplicação, mantendo a janela aberta até que seja fechada
janela.mainloop()
