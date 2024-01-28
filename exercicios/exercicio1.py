#Exercício 1 - Conceitos Básicos - WomakersCode

#Pedindo dois números
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#Saída com as operações
print(f'A soma entre os dois números é: {num1+num2}')
print(f'A subtração entre os dois números é: {num1-num2}')
print(f'A multiplicação entre os dois números é: {num1*num2}')

#Verificação de exceção para caso de divisão por zero
if (num1 == 0) or (num2 == 0):
    print(f'Não é possível realizar a operação. Um dos números é ZERO.')
else:
    print(f'A divisão entre os dois números é: {num1//num2}')

#Finalizando
print('---')