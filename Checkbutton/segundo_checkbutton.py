from tkinter import *

janela = Tk()

janela.geometry('950x400')

janela.title('Janela Principal')

informacao = Label(janela, text='Selecione a opção desejada', fg='blue', font=('Arial', 20))
informacao.pack()
total = 0
valorAntigo = 0
def soma():
    global total
    global valorAntigo
    
    valorAntigo = total
    total += varNumero.get()
    print(f'{valorAntigo} + {varNumero.get()} = {total}')

varNumero = IntVar()

checkNumero5 = Checkbutton(janela, text='5', variable= varNumero, font=('Arial', 20),
                    onvalue=5, offvalue=0, height=2, width=10, command=soma)
checkNumero5.pack()

checkNumero10 = Checkbutton(janela, text='10', variable= varNumero, font=('Arial', 20),
                    onvalue=10, offvalue=0, height=2, width=10, command=soma)
checkNumero10.pack()

checkNumero15 = Checkbutton(janela, text='15', variable= varNumero, font=('Arial', 20),
                    onvalue=15, offvalue=0, height=2, width=10, command=soma)
checkNumero15.pack()

janela.mainloop()