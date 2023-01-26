from random import randrange
from time import sleep

def jogar_adivinha():

    def funcao1():
        sorteado = randrange(1, 11)
        tentativa = 1
        rodad = 3
        for rodada in range(1,4):
            print('Tentativa {} de {}! '.format(tentativa,rodad))
            numero = int(input(('Digite um numero!: ')))
            tentativa = tentativa + 1
            if numero == sorteado:
                sleep(1)
                print('Acertou mizeravi!')
                break
            else:
                if numero > sorteado:
                    sleep(1)
                    print('O numero é menor')
                if numero < sorteado:
                    sleep(1)
                    print('O numero é maior')

    print('Seja bem vindo ao jogo de adivinhação!')
    sleep(2)
    print('Adivinhe um numero de 1 a 10!')
    sleep(2)
    nivel = int(input('Escolha a dificuldade!\n(1)Facil (2)Medio (3)Dificil: '))
    sleep(2)
    if nivel == 1:
        funcao1()

if (__name__=='__main__'):
    jogar_adivinha()