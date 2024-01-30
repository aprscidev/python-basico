#Desafio 37 - Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão
# 1 para binário, 2 para octal, 3 para hexadecimal

num = int(input('Escreva um número inteiro: '))
opcao = int(input('Escolha uma conversão: 1 - Binário, 2 - Octal, 3 - Hexadecimal '))

if opcao == 1:
    binario = bin(num)
    print(f'O número {num} convertido para binário é igual a: {binario}')
elif opcao == 2:
    octal = oct(num)
    print(f'O número {num} convertido para octal é igual a: {octal}')
elif opcao == 3:
    hexa = hex(num)
    print(f'O número {num} convertido para hexadecimal é igual a : {hexa}')
print('--FIM--')