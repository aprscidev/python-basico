#Desafio 48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.

soma = 0
print('Soma entre todos os números ímpares que são múltiplos de 3 entre 1 e 500: ')
for impares in range(0, 500, 3):
    if (impares % 2 == 1):
        soma = soma + impares
print(soma)