#Desafio 50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado por ímpar, desconsidere-o

somapar = 0

for n in range (0, 7):
    print(f'Número {n} de 6.')
    num = int(input('Digite um número inteiro: '))
    if (num % 2 == 0):
        somapar = somapar + num
    else:
        print(f'Número {n} digitado é ímpar e não será somado.')
print(f'Soma dos números pares digitados: {somapar}')

