from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()

janela.geometry('500x150')

janela.title('Janela Principal')

Label(janela, text='Selecione um mês: ', font=('Arial', 12)).grid(row=1, column=0)

mesSelecionado = ttk.Combobox(janela, font=('Arial', 12))
mesSelecionado['values'] = ('Janeiro', 
                            'Fevereiro',
                            'Março',
                            'Abril',
                            'Maio',
                            'Junho',
                            'Julho',
                            'Agosto',
                            'Setembro',
                            'Outubro',
                            'Novembro',
                            'Dezembro')

mesSelecionado.grid(row=1, column=1)
mesSelecionado.current(4)

janela.mainloop()