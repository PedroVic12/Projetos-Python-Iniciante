import os
import random
from colorama import Fore, Back, Style

jogar_novamente = 's'
jogadas = 0
quem_joga = 2  # somos o player 2 e a CPU o player 1
max_jogadas = 9
vit = 'n'
velha = [
        [' ', ' ', ' '], #l[0] c[0]     l[0] c[1]      l[0] c[2]  
        [' ', ' ', ' '], #l[1] c[0]     l[1] c[1]      l[1] c[2]
        [' ', ' ', ' ']  #l[2] c[0]     l[2] c[1]      l[2] c[2]
]


def tela():
    global velha
    global jogadas
    os.system('cls')
    print("Bem vindo ao JOGO DA VELHA!\n")
    print('Digite apenas os numeros [0, 1 ou 2]\n')
    print('     0   1   2')
    print('0:   ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('   ------------')
    print('1:   ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('   ------------')
    print('2:   ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print('   ------------')
    print('Jogadas: ' + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogador_joga():
    global jogadas
    global quem_joga
    global max_jogadas
    if quem_joga == 2 and jogadas < max_jogadas:
        
        # Verificar se é uma jogada valida
        try:
            l = int(input("Digite a linha que voce quer jogar...: "))
            c = int(input("Digite a coluna que voce quer jogar...: "))
            
            # Loop para validar a jogada(lugar ja preenchido nao da pra jogar)
            while velha[l][c] != " ":
                l = int(input("Digite e linha que voce quer jogar...: "))
                c = int(input("Digite a coluna que voce quer jogar...: "))

            velha[l][c] = "X"
            quem_joga = 1
            jogadas += 1
        except:
            print("Linha e ou coluna invalida!")
            os.system('pause')


def cpu_joga():
    global jogadas
    global quem_joga
    global max_jogadas
    if quem_joga == 1 and jogadas < max_jogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)

        # Loop para validar a jogada(lugar ja preenchido nao da pra jogar)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        jogadas += 1
        quem_joga = 2


# Existem duas formas de verificar vitoria.
    #1) Usando If 
        #[0][0] = "x" [0][1] = "x" [0][2] = "x". O Jogador X ganhou.Fazendo isso para TODAS as possibilidades
            
    #2) Usando for (loop):
        # [0][0] = "x" entao soma = 1
        # [0][1] = "x" entao soma = 2 
        # [0][2] = "x" entao soma = 3
        # Se soma = 3, entao houve vitoria.

def verificar_vitoria():
    global velha
    vitoria = 'n'
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = 'n'
        # 3 possibilidades de victoria em linha
        indice_linhas = indice_colunas = 0
        while indice_linhas < 3:
            soma = 0
            indice_colunas = 0
            while indice_colunas < 3:
                 if (velha[indice_linhas][indice_colunas] == s):
                     soma +=1
                 indice_colunas += 1
            
            if soma == 3:
                vitoria = s
                break
            indice_linhas +=1
        if vitoria != "n":
            break
        
         # 3 possibilidades de victoria em coluna
        indice_linhas = indice_colunas = 0
        while indice_colunas < 3:
            soma = 0
            indice_linhas = 0
            while indice_linhas  < 3:
                 if (velha[indice_linhas][indice_colunas] == s):
                     soma +=1
                 indice_linhas += 1
            
            if soma == 3:
                vitoria = s
                break
            indice_colunas +=1
            
        if vitoria != "n":
            break          
          
        # 2 possibilidades de victoria em diagonal
        # Diagonal Principal:
        soma = 0
        indice_diagonal = 0
        while indice_diagonal < 3:
            if (velha[indice_diagonal][indice_diagonal] == s):
                soma +=1  
            indice_diagonal += 1
        if soma == 3:
            vitoria = s
            break

        # Diagonal Secundaria:
        soma = 0
        indice_diagonal_linha = 0
        indice_diagonal_coluna = 2
        while indice_diagonal_coluna >=0 :
            if (velha[indice_diagonal_linha][indice_diagonal_coluna] == s):
                soma +=1  
            indice_diagonal_linha += 1
            indice_diagonal_coluna -= 1
        if soma == 3:
            vitoria = s
            break             
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quem_joga
    global max_jogadas
    global vit
    jogadas = 0
    quem_joga = 2  # somos o player 2 e a CPU o player 1
    max_jogadas = 9
    vit = 'n'
    velha = [
        [' ', ' ', ' '], #l[0] c[0]     l[0] c[1]      l[0] c[2]  
        [' ', ' ', ' '], #l[1] c[0]     l[1] c[1]      l[1] c[2]
        [' ', ' ', ' ']  #l[2] c[0]     l[2] c[1]      l[2] c[2]
    ]
    # 8 Verificaçoes para o Player 1
        
            
    # 8 Verificaçoes para o Player 2
while(jogar_novamente == "s"):
    while True:
        tela()
        
        # Jogada do jogador
        jogador_joga()
        
        # Jogador do Cpu
        cpu_joga()
        tela()
        
        # Verificar victoria do jogo
        vit = verificar_vitoria()
        if vit != "n" or jogadas >= max_jogadas:
            break
        
    print( Fore.RED + 'FIM DO JOGO' + Fore.YELLOW)
    if vit == "X" or vit == "O":
        print(f"Resultado: O Jogador {vit} venceu!")
    else:
        print("Resultado: EMPATE!!! ")
    jogar_novamente = input( Fore.BLUE + 'Jogar novamente? [s/n]' + Fore.RESET)
    redefinir()
            
