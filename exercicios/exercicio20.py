#Exercício 11 - Tomada de decisão - Womakerscode

#Solicitando o salário bruto ao usuário
renda = float(input('Digite o valor do salário bruto (renda): '))

#Realizando verificações
if (renda <= 1903.98):
    print('Isento de imposto de renda.')
elif (renda >= 1903.99) and (renda <=2826.65):
    desconto = (renda * 7.5) / 100
    print(f'Para a renda informada, a alíquota será de 7.5%: R${desconto:.2f}')
elif (renda >= 2826.66) and (renda <= 3751.05):
    desconto = (renda * 15) / 100
    print(f'Para a renda informada, a alíquota será de 15%: R${desconto:.2f}')
elif (renda >= 3751.06) and (renda <= 4664.68):
    desconto = (renda * 22.5) / 100
    print(f'Para a renda informada, a alíquota será de 22.5%: R${desconto:.2f}')
elif (renda > 4664.68):
    desconto = (renda * 27.5) / 100
    print(f'Para a renda informada, a alíquota será de 27.5%: R${desconto:.2f}')

#Finalizando
print('--') 