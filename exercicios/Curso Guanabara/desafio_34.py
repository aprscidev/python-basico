#Desafio 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o valor do salário do funcionário: '))
if salario > 1250:
    aumento = (salario * 0.1) + salario
    print(f'Valor do salário com aumento de 10%: R${aumento:.2f}')
else:
    aumento = (salario * 0.15) + salario
    print(f'Valor do salário com aumento de 15%: R${aumento:.2f}')
print('--FIM--')