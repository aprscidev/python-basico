#Desafio 60 - Faça um programa que leia um número qualquer e mostre seu fatorial.


n = int(input('Digite um número: '))
c = n
f = 1
print(f'Calculando {n}!')
while c > 0:
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f = f * c
    c = c - 1
print(f)