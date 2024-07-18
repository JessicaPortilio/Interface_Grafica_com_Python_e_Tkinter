from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.geometry('500x500')

janela.title('Janela Principal')

informacao = Label(janela, text='Mensagens', font=50)
informacao.pack()

messagebox.showinfo('Informação', 'Bem-vindo(a) ao curso Tkinter')
messagebox.showwarning('Aviso', 'Você está apreendendo Tkinter')
messagebox.showerror('Erro', 'Erro ao carregar o sistema')
messagebox.askquestion('Questão', 'Tkinter é com Python?')
messagebox.askokcancel('Ok ou Cancelar', 'Deseja continuar?')
messagebox.askyesno('Sim ou Não', 'Quer procurar o valor?')
messagebox.askretrycancel('Repetir ou Cancelar', 'Quer tentar novamente?')

janela.mainloop()