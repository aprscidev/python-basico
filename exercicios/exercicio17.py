#Exercício 8 - Tomada de decisão - Womakerscode

#Solicitando os números para o usuário
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#Realizando as verificações
if num1 > num2 and num1 > num3:
    print(f'O maior valor é: {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é: {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior número é: {num3}')

#Finalizando
print('---')
  

