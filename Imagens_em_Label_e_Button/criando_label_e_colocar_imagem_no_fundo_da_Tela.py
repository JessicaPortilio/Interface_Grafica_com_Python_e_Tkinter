from tkinter import *
from PIL import ImageTk, Image

# Inicializa a janela principal da aplicação
janela = Tk()

# Define o tamanho da janela
janela.geometry("520x300")

# Define o título da janela
janela.title('Interface Gráfica')

# Carrega a imagem original do arquivo 'fundo.jpg'
imagem_original = Image.open('fundo.jpg')
# Redimensiona a imagem para caber na janela usando o método LANCZOS para uma alta qualidade de redimensionamento
imagem_redimensionada = imagem_original.resize((520, 300), Image.LANCZOS)
# Converte a imagem redimensionada para um objeto PhotoImage do Tkinter
imagem_fundo = ImageTk.PhotoImage(imagem_redimensionada)

# Cria um rótulo com a imagem redimensionada e posiciona-o na janela
label_imagem_fundo = Label(janela, image=imagem_fundo)
label_imagem_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Adiciona outros widgets sobre a imagem de fundo, se necessário
texto1 = Label(janela, text='Texto sobre a imagem', font=('Times New Roman', 16, 'bold'), bg='lightblue')
texto1.pack(pady=20)

# Cria um botão com um comando associado
botao = Button(janela, text='Clique aqui', command=janela.destroy, bg='lightgray')
botao.pack(pady=10)

# Inicia o loop principal da aplicação, mantendo a janela aberta até que seja fechada
janela.mainloop()
