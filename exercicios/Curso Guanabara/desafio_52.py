#Desafio 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
tot = 0
for c in range (1, num+1):
    if num % c == 0:
        tot = tot +1

if tot == 2:
    print('Número PRIMO.')
else:
    print('Não é número PRIMO.')
print('--FIM--')