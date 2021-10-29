# Projeto 3 - Chute o número
# objetivo: Criar um algorítimo que gera um valor aleatório e eu tenho que ficar tentando o número até eu acertar
import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(50, 1))],
            [sg.Input(size=(50, 50), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(50, 50))]
        ]
        # criar uma janela
        janela = sg.Window('Chute o numero!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # receber os valores
                self.evento, self.valores = janela.read()
                # Fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!')
                            break
            if self.evento == sg.WINDOW_CLOSED or self.evento == 'Cancel':
                    
                print('You entered', self.valores[0])
            janela.close()
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()