from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome do Usuario'), sg.Input(key='usuario', size=(200, 100))],
    [sg.Text('Senha:'), sg.Input(key='senha', password_char='*')],
    # [sg.CheckBox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de login', layout)

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Pedro' and valores['senha'] == '12345':
            print('Bem vindo a minha Primeira interface grafica!')
