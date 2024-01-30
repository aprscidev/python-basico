#Desafio 68 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
#que ele conquistou no final do jogo.

from random import randint

n = 0
soma = 0
contador_vitoria = 0

while True:
    print('VAMOS JOGAR PAR OU IMPAR?')
    n = int(input('Digite um número (0 a 10): '))
    nmaq = randint(0, 10)
    opcao = str(input('PAR OU IMPAR? (P/I) ')).upper().strip()
    soma = nmaq + n
    if opcao == 'P':
        if soma % 2 == 0:
            print('VOCÊ ESCOLHEU PAR E GANHOU!')
            print(f'Você escolheu {n} e eu escolhi {nmaq} e a soma deu {soma}.')
            contador_vitoria = contador_vitoria + 1
        else:
            print(f'VOCÊ ESCOLHEU PAR E PERDEU! Você escolheu o número {n} e eu escolhi {nmaq} e a soma deu {soma}.')
            break
    if opcao == 'I':
        if not soma % 2 == 0:
            print('VOCÊ ESCOLHEU ÍMPAR E GANHOU!')
            print(f'Você escolheu {n} e eu escolhi {nmaq} e a soma deu {soma}.')
            contador_vitoria = contador_vitoria + 1
        else:
            print(f'VOCÊ ESCOLHEU ÍMPAR E PERDEU! Você escolheu o número {n} e eu escolhi {nmaq} e a soma deu {soma}.')
            break

print(f'Número de vítorias consecutivas: {contador_vitoria}')
print('--FIM--')


