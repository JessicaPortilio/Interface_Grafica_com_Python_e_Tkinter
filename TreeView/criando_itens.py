from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()

janela.geometry('815x250')

janela.title('Janela Principal')

estiloDaTreeView = ttk.Style()
estiloDaTreeView.theme_use('alt')
estiloDaTreeView.configure('.', font=('Arial', 14))

treeViewDados = ttk.Treeview(janela, columns=(1,2,3,4), show='headings')
treeViewDados.column('1', anchor=CENTER)
treeViewDados.heading('1', text='ID')

treeViewDados.column('2', anchor=CENTER)
treeViewDados.heading('2', text='Nome')

treeViewDados.column('3', anchor=CENTER)
treeViewDados.heading('3', text='Idade')

treeViewDados.column('4', anchor=CENTER)
treeViewDados.heading('4', text='Sexo')

treeViewDados.insert('', 'end', text='1', values=('1','Allan', 29, 'Masculino'))
treeViewDados.insert('', 'end', text='2', values=('2','Ana', 41, 'Feminino'))
treeViewDados.insert('', 'end', text='3', values=('3','Vanessa', 64, 'Feminino'))
treeViewDados.insert('', 'end', text='4', values=('4','Pedro', 19, 'Masculino'))
treeViewDados.insert('', 'end', text='5', values=('5','Thiago', 32, 'Masculino'))
treeViewDados.pack()

janela.mainloop()