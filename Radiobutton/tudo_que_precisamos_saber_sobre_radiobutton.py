from tkinter import *

# Função que será chamada quando o valor do RadioButton mudar
def mostrar_selecao():
    selecao = var.get()
    label_selecao.config(text=f'Seleção: {selecao}')

# Inicializa a janela principal da aplicação
janela = Tk()
janela.title('Exemplo de RadioButtons')

# Variável que armazenará o valor dos RadioButtons
var = StringVar(value='1')  # Define um valor padrão inicial

# RadioButton com activebackground
# activebackground: Cor de fundo quando o mouse está sobre o RadioButton.
rb_activebackground = Radiobutton(janela, text='Opção 1', variable=var, value='1', activebackground='lightblue', command=mostrar_selecao)
rb_activebackground.grid(row=0, column=0, sticky='w', padx=5, pady=5)

# RadioButton com activeforeground
# activeforeground: Cor do texto quando o mouse está sobre o RadioButton.
rb_activeforeground = Radiobutton(janela, text='Opção 2', variable=var, value='2', activeforeground='red', command=mostrar_selecao)
rb_activeforeground.grid(row=1, column=0, sticky='w', padx=5, pady=5)

# RadioButton com anchor
# anchor: Posição do RadioButton em um espaço maior.
rb_anchor = Radiobutton(janela, text='Opção 3', variable=var, value='3', anchor='w', command=mostrar_selecao)
rb_anchor.grid(row=2, column=0, sticky='w', padx=5, pady=5)

# RadioButton com bg
# bg: Cor de fundo normal.
rb_bg = Radiobutton(janela, text='Opção 4', variable=var, value='4', bg='yellow', command=mostrar_selecao)
rb_bg.grid(row=3, column=0, sticky='w', padx=5, pady=5)

# RadioButton com bitmap
# Nota: bitmaps são imagens monocromáticas fornecidas pelo Tkinter (como "error", "info", "questhead", "hourglass", etc.)
# bitmap: Imagem monocromática no RadioButton.
rb_bitmap = Radiobutton(janela, text='Opção 5', variable=var, value='5', bitmap='info', command=mostrar_selecao)
rb_bitmap.grid(row=4, column=0, sticky='w', padx=5, pady=5)

# RadioButton com borderwidth
# borderwidth: Largura da borda do RadioButton.
rb_borderwidth = Radiobutton(janela, text='Opção 6', variable=var, value='6', borderwidth=5, command=mostrar_selecao)
rb_borderwidth.grid(row=5, column=0, sticky='w', padx=5, pady=5)

# RadioButton com command
# command: Função chamada quando o estado do RadioButton muda.
rb_command = Radiobutton(janela, text='Opção 7', variable=var, value='7', command=mostrar_selecao)
rb_command.grid(row=6, column=0, sticky='w', padx=5, pady=5)

# RadioButton com cursor
# cursor: Tipo de cursor do mouse ao passar sobre o RadioButton.
rb_cursor = Radiobutton(janela, text='Opção 8', variable=var, value='8', cursor='hand2', command=mostrar_selecao)
rb_cursor.grid(row=7, column=0, sticky='w', padx=5, pady=5)

# RadioButton com font
# font: Fonte usada para o texto.
rb_font = Radiobutton(janela, text='Opção 9', variable=var, value='9', font=('Helvetica', 16), command=mostrar_selecao)
rb_font.grid(row=8, column=0, sticky='w', padx=5, pady=5)

# RadioButton com fg
# fg: Cor do texto.
rb_fg = Radiobutton(janela, text='Opção 10', variable=var, value='10', fg='blue', command=mostrar_selecao)
rb_fg.grid(row=9, column=0, sticky='w', padx=5, pady=5)

# RadioButton com height
# height: Número de linhas de texto.
rb_height = Radiobutton(janela, text='Opção 11', variable=var, value='11', height=3, command=mostrar_selecao)
rb_height.grid(row=10, column=0, sticky='w', padx=5, pady=5)

# RadioButton com highlightbackground
# highlightbackground: Cor do destaque quando o RadioButton não tem foco.
rb_highlightbackground = Radiobutton(janela, text='Opção 12', variable=var, value='12', highlightbackground='green', command=mostrar_selecao)
rb_highlightbackground.grid(row=11, column=0, sticky='w', padx=5, pady=5)

# RadioButton com highlightcolor
# highlightcolor: Cor do destaque quando o RadioButton tem foco.
rb_highlightcolor = Radiobutton(janela, text='Opção 13', variable=var, value='13', highlightcolor='purple', command=mostrar_selecao)
rb_highlightcolor.grid(row=12, column=0, sticky='w', padx=5, pady=5)

# RadioButton com image
# Nota: A imagem precisa ser um objeto PhotoImage
# image: Imagem gráfica em vez de texto.
# img = PhotoImage(file='example_image.png')  # Certifique-se de ter uma imagem 'example_image.png' no mesmo diretório
# rb_image = Radiobutton(janela, image=img, variable=var, value='14', command=mostrar_selecao)
# rb_image.grid(row=13, column=0, sticky='w', padx=5, pady=5)

# RadioButton com justify
# justify: Justificação do texto em várias linhas.
rb_justify = Radiobutton(janela, text='Opção\ncom\nmúltiplas\nlinhas', variable=var, value='15', justify=LEFT, command=mostrar_selecao)
rb_justify.grid(row=14, column=0, sticky='w', padx=5, pady=5)

# RadioButton com padx
# padx: Espaçamento horizontal.
rb_padx = Radiobutton(janela, text='Opção 16', variable=var, value='16', padx=20, command=mostrar_selecao)
rb_padx.grid(row=15, column=0, sticky='w', padx=5, pady=5)

# RadioButton com pady
# pady: Espaçamento vertical.
rb_pady = Radiobutton(janela, text='Opção 17', variable=var, value='17', pady=20, command=mostrar_selecao)
rb_pady.grid(row=16, column=0, sticky='w', padx=5, pady=5)

# RadioButton com relief
# relief: Aparência da borda decorativa.
rb_relief = Radiobutton(janela, text='Opção 18', variable=var, value='18', relief=RIDGE, command=mostrar_selecao)
rb_relief.grid(row=17, column=0, sticky='w', padx=5, pady=5)

# RadioButton com selectcolor
# selectcolor: Cor do RadioButton quando selecionado.
rb_selectcolor = Radiobutton(janela, text='Opção 19', variable=var, value='19', selectcolor='yellow', command=mostrar_selecao)
rb_selectcolor.grid(row=18, column=0, sticky='w', padx=5, pady=5)

# RadioButton com selectimage
# Nota: A imagem precisa ser um objeto PhotoImage
# selectimage: Imagem quando o RadioButton está selecionado.
# select_img = PhotoImage(file='example_select_image.png')  # Certifique-se de ter uma imagem 'example_select_image.png' no mesmo diretório
# rb_selectimage = Radiobutton(janela, image=img, selectimage=select_img, variable=var, value='20', command=mostrar_selecao)
# rb_selectimage.grid(row=19, column=0, sticky='w', padx=5, pady=5)

# RadioButton com state
# state: Estado do RadioButton (NORMAL ou DISABLED).
rb_state = Radiobutton(janela, text='Opção 21', variable=var, value='21', state=DISABLED, command=mostrar_selecao)
rb_state.grid(row=20, column=0, sticky='w', padx=5, pady=5)

# RadioButton com text
# text: Texto exibido ao lado do RadioButton.
rb_text = Radiobutton(janela, text='Opção 22', variable=var, value='22', command=mostrar_selecao)
rb_text.grid(row=21, column=0, sticky='w', padx=5, pady=5)

# RadioButton com textvariable
# textvariable: Variável de controle para o texto.
var_text = StringVar(value='Texto Dinâmico')
rb_textvariable = Radiobutton(janela, textvariable=var_text, variable=var, value='23', command=mostrar_selecao)
rb_textvariable.grid(row=22, column=0, sticky='w', padx=5, pady=5)

# RadioButton com underline
# underline: Sublinha a n-ésima letra do texto.
rb_underline = Radiobutton(janela, text='Opção 24', variable=var, value='24', underline=1, command=mostrar_selecao)
rb_underline.grid(row=23, column=0, sticky='w', padx=5, pady=5)

# RadioButton com value
# value: Valor associado ao RadioButton.
rb_value = Radiobutton(janela, text='Opção 25', variable=var, value='25', command=mostrar_selecao)
rb_value.grid(row=24, column=0, sticky='w', padx=5, pady=5)

# RadioButton com variable
# Nota: Já estamos usando uma variável 'var' para controlar os RadioButtons
# variable: Variável de controle compartilhada com outros RadioButtons.

# RadioButton com width
# width: Largura do texto em caracteres.
rb_width = Radiobutton(janela, text='Opção 27', variable=var, value='27', width=20, command=mostrar_selecao)
rb_width.grid(row=25, column=0, sticky='w', padx=5, pady=5)

# RadioButton com wraplength
# wraplength: Limita o número de caracteres por linha.
rb_wraplength = Radiobutton(janela, text='Opção\ncom\nquebra\nautomática\nde\nlinha', variable=var, value='28', wraplength=50, command=mostrar_selecao)
rb_wraplength.grid(row=26, column=0, sticky='w', padx=5, pady=5)

# Label para exibir a seleção atual
label_selecao = Label(janela, text='Seleção: ')
label_selecao.grid(row=27, column=0, sticky='w', padx=5, pady=5)

# Entra no loop principal da aplicação
janela.mainloop()
