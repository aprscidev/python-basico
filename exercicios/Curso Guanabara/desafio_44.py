#Desafio 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto em R$: '))
condicao = int(input('Digite a condição de pagamento: 1 - À VISTA DINHEIRO/CHEQUE, 2 - À VISTA CARTÃO, 3 - 2X NO CARTÃO, 4 - 3X OU MAIS NO CARTÃO. '))

if condicao == 1:
    total = preco - (preco * 0.10)
    print(f'10% de desconto. Total a pagar: R${total:.2f}')
elif condicao == 2:
    total = preco - ( preco * 0.05)
    print(f'5% de desconto. Total a pagar: R${total:.2f}')
elif condicao == 3:
    print(f'Sem desconto. Total a pagar: R${preco:.2f}')
elif condicao == 4:
    total = preco + (preco * 0.20)
    print(f'20% de juros. Total a pagar: R${total:.2f}')
print('--FIM--')