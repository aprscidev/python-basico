#Desafio 58 - Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
#palpites foram necessários para vencer.

from random import randint

tentativas = 0

computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        tentativas = tentativas + 1


print(f'Você conseguiu! Pensei no número {computador}. Você precisou de {tentativas} tentativas para acertar!')