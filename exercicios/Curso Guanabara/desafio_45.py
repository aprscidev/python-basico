#Desafio 45 - Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? 0 - PEDRA, 1 - PAPEL, 2 - TESOURA '))

if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print('EMPATE!')
    elif jogador == 1:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print(f'Você GANHOU! PAPEL ganha de PEDRA.')
    elif jogador == 2:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print(f'Você PERDEU! PEDRA ganha da TESOURA.')
    else:
        print('OPÇÃO INVÁLIDA!')

if computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print(f'Você PERDEU! PAPEL ganha de PEDRA.')
    elif jogador == 1:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print('EMPATE!')
    elif jogador == 2:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print(f'Você GANHOU! TESOURA ganha do PAPEL.')
    else:
        print('OPÇÃO INVÁLIDA!')

if computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print('Você GANHOU! PEDRA ganha da TESOURA!')
    elif jogador == 1:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print('Você PERDEU! TESOURA ganha do PAPEL!')
    elif jogador ==2:
        print(f'Computador jogou {itens[computador]} e jogador jogou {itens[jogador]}')
        print('EMPATE!')
    else:
        print('OPÇÃO INVÁLIDA!')

print('--FIM--')

