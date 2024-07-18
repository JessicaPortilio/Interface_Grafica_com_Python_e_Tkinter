from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.geometry('500x500')

janela.title('Janela Principal')

informacao = Label(janela, text='Mensagens', font=50)
informacao.pack()

def mensagemInformacao():
    messagebox.showinfo('Informação', 'Bem-vindo(a) ao curso Tkinter')

def mensagemAviso():
    messagebox.showwarning('Aviso', 'Você está apreendendo Tkinter')

def mensagemErro():
    messagebox.showerror('Erro', 'Erro ao carregar o sistema')

def mensagemQuestao():
    resposta = messagebox.askquestion('Questão', 'Tkinter é com Python?')
    
    if resposta == 'yes':
        messagebox.showinfo('Informação', 'Você aceitou!')
    else:
        messagebox.showerror('Erro', 'Você errou!')
        
def mensagemOk_ou_Cancelar():
    resposta = messagebox.askokcancel('Ok ou Cancelar', 'Deseja continuar?')

    if resposta:
        messagebox.showinfo('Informação', 'Continuando...')
    else:
        messagebox.showwarning('Aviso', 'Você cancelou!')

def mensagemSim_ou_Nao():
    resposta = messagebox.askyesno('Sim ou Não', 'Quer procurar o valor?')
    
    if resposta:
        messagebox.showinfo('Informação', 'Procurando...')
    else:
        messagebox.showinfo('Informação', 'Procura cancelada!')


def mensagemRepetir_ou_Cancelar():
    resposta = messagebox.askretrycancel('Repetir ou Cancelar', 'Quer tentar novamente?')

    if resposta:
        messagebox.showinfo('Informação', 'Tentando...')
    else:
        messagebox.showinfo('Informação', 'Cancelado com Sucesso!')
botaoInformaco = Button(janela, text='Informação', font=('Arial, 20'), command=mensagemInformacao).pack()
botaoAviso = Button(janela, text='Aviso', font=('Arial, 20'), command=mensagemAviso).pack()
botaoErro = Button(janela, text='Erro', font=('Arial, 20'), command=mensagemErro).pack()
botaoQuestao = Button(janela, text='Questão', font=('Arial, 20'), command=mensagemQuestao).pack()
botaoOk_ou_Cancelar = Button(janela, text='Ok ou Cancelar', font=('Arial, 20'), command=mensagemOk_ou_Cancelar).pack()
botaoSim_ou_Nao = Button(janela, text='Sim ou Não', font=('Arial, 20'), command=mensagemSim_ou_Nao).pack()
botaoRepetir_ou_Cancelar = Button(janela, text='Repetir ou Cancelar', font=('Arial, 20'), command=mensagemRepetir_ou_Cancelar).pack()

janela.mainloop()