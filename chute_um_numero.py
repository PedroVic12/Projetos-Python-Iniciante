import random
import os

os.system('cls')


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def PedirValorAleatorio(self):
        self.valor_chutado = input('Chute um numero: ')

    def Iniciar(self):
        self.GerarUmNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_chutado) >= self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valor_chutado) < self.valor_aleatorio:
                    print('Chute um valor mais alto!')
                    self.PedirValorAleatorio()
                if int(self.valor_chutado) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print("PARABENS VOCE ACERTOU O NUMERO!!!")
        except:
            print('Por favor digite apenas numeros')
            self.Iniciar()
    def GerarUmNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()
