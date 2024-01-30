#Desafio 32 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano (AAAA): '))
if (ano % 4 == 0):
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
print('--FIM--')