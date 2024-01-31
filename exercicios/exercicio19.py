#Exercício 10 - Tomada de decisão - Womakerscode

#Solicitando os valores ao usuário
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#Realizando verificações para exibir os números em ordem crescente
if num1 < num2 and num2 < num3:
    print(f'Ordem crescente: {num1}, {num2}, {num3}')
elif num1 < num3 and num3 < num2:
    print(f'Ordem crescente: {num1}, {num3}, {num2}')
elif num2 < num1 and num1 < num3:
    print(f'Ordem crescente: {num2}, {num1}, {num3}')
elif num2 < num3 and num3 < num1:
    print(f'Ordem crescente: {num2}, {num3}, {num1}')
elif num3 < num1 and num1 < num2:
    print(f'Ordem crescente: {num3}, {num1}, {num2}')
elif num3 < num2 and num2 < num1:
    print(f'Ordem crescente: {num3}, {num2}, {num1}')

#Finalizando
print('--')

#Faça um programa que lê três números inteiros e os mostra em ordem crescente. 