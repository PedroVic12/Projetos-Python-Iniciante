from tkinter import *
from tkinter import ttk

# Cores
cor0 = '#ffffff'
cor1 = '#444466'
cor2 = '#4065a1'

janela = Tk()
janela.title('')
janela.geometry('350x230')
janela.configure(bg=cor0)

# Dividindo A janela em duas partes

frame_cima = Frame(janela, width=350, height=50, bg=cor0,
                   pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=350, height=180,
                    bg=cor0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# configurando o frame de cima
app_nome = Label(frame_cima, text='Calculadora de Imc', width=23, height=1,
                 padx=0, relief='flat', anchor='center', font=('Ivy 18 bold'), bg=cor0, fg=cor1)
app_nome.place(x=0, y=0)


app_linha = Label(frame_cima, text='', width=400, height=1, padx=0,
                  relief='flat', anchor='center', font=('Ivy 1'), bg=cor2, fg=cor1)
app_linha.place(x=0, y=35)

# Calculo do IMC
# -------Parte logica----------
def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2
    resultado = '{:.1f}'.format(imc)

    if imc < 18.5:
        l_resultado_texto['text'] = 'Você esta ABAIXO DO PESO'
    elif imc >= 18.5 and imc < 25:
        l_resultado_texto['text'] = 'Você esta na categoria NORMAL'
    elif imc >= 25 and imc < 30:
        l_resultado_texto['text'] = 'Você esta em SOBREPESO'
    else:
        l_resultado_texto['text'] = 'Você esta na OBSESIDADE'
    l_resultado['text']= resultado

# configurando o frame de baixo
# Peso
l_peso = Label(frame_baixo, text='Insira seu peso:', height=1, padx=0,
               relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor0, fg=cor1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_peso = Entry(frame_baixo, width=5, relief='solid',
               font=('Ivy 12 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

# Altura
l_altura = Label(frame_baixo, text='Insira sua Altura:', height=1, padx=0,
                 relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor0, fg=cor1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_altura = Entry(frame_baixo, width=5, relief='solid',
                 font=('Ivy 12 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


# resultado
l_resultado = Label(frame_baixo, text='', width=5, height=1, padx=6, pady=12,
                    relief='flat', anchor='center', font=('Ivy 24 bold'), bg=cor2, fg=cor0)

l_resultado.place(x=220, y=10)

# Botao
b_calcular = Button(frame_baixo, command=calcular,  text='Calcular!', width=40, height=1,
                    overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor0)

b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=10, columnspan=20)

# Janela de resultado
l_resultado_texto = Label(frame_baixo, text='', width=37, height=1,
                          padx=5, pady=12, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor0, fg=cor1)

l_resultado_texto.place(x=0, y=90)


janela.mainloop()
