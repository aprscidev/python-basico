#Desafio 55 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maiorpeso = 0

for p in range (1, 6):
    print(f'Pessoa {p} de 5')
    peso = int(input('Digite seu peso em QUILOS: '))
    if p == 1:
        menorpeso = peso
    elif peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print(f'Maior peso: {maiorpeso}')
print(f'Menor peso: {menorpeso}')