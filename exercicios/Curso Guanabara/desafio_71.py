#Desafio 71 - Crie um programa que simula o funcionamento de um caixa eletrônico. No início, pergunta ao usuário qual será o valor a ser sacado (número inteiro) e o programa
#vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        totalcedula = totalcedula + 1
    else:
        if totalcedula >0:
            print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula == 50:
                cedula = 20
        elif cedula == 20:
                cedula = 10
         elif cedula == 10:
                cedula = 1
        totalcedula=0
        if total == 0:
            break
print('--FIM--')
