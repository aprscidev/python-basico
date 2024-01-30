#Desafio 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

num = 0
while num >= 0:
    num = int(input('Digite um número para mostrar sua tabuada: '))
    if num < 0:
        break
    else:
        for n in range (0, 10):
            tabuada = n * num
            print(f'{n} x {num} = {tabuada}')
print('--FIM--')
