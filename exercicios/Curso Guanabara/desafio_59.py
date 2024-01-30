#Desafio 59 - Crie um programa que leia dois valores e mostre um menu na tela: [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while not opcao == 5:
    opcao = int(input('Digite a opcao: [1] SOMAR, [2] MULTIPICAR, [3] MAIOR, [4] NOVOS NÚMEROS, [5] SAIR DO PROGRAMA '))
    if opcao == 1:
        soma = n1 + n2
        print(f'Soma dos dois valores: {soma}')
    elif opcao == 2:
        produto = (n1 * n2)
        print(f'Multiplicação dos dois valores: {produto}')
    elif opcao == 3:
        maior = max(n1, n2)
        print(f'Maior valor: {maior}')
    elif opcao == 4:
        n1 = int(input('Digite um novo primeiro valor: '))
        n2 = int(input('DIgite um segundo novo valor: '))
    else:
        print('Opção inválida. Tente novamente!')
print('--FIM--')
