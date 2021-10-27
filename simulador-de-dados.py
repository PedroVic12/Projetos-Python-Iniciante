# Simular o uso de um dado, gerando um valor de 1 ate 6

import random
import os
import PySimpleGUI as sg


os.system('cls')
class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce gostaria de gerar um novo valor para o dado?"
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]


    def Iniciar(self):
        #Criar uma janela
        self.janela = sg.Window('Simulador de Dados', layout = self.layout)
        
        #Ler os valores da tela
        self.eventos, self.valores = self.janela.read()
        
        # Fazer alguma coisa com esses valores
        if(self.eventos):
            resposta = input(self.mensagem)
        
            try:
                    if self.eventos == 'Sim' or self.eventos == 's':
                        self.GerarValorDoDado()
                    elif self.eventos == 'Não' or self.eventos == 'n':
                        print('Obrigado pela sua participação!')
                    else:
                        print('Favor digitar sim ou nao')
            except:
                print('Ocorreu um erro ao receber sua resposta.')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador=SimuladorDeDado()
simulador.Iniciar()
