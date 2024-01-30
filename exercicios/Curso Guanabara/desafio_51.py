#Desafio 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.

print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for n in range (1, 11):
    progressao = termo + ((n - 1) * razao)
    print(progressao)

print('--FIM--')