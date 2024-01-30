#Desafio 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
#o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
qtde_anos = int(input('DIgite a quantidade de anos para o pagamento: '))

qtde_meses = int(qtde_anos / 12)
prestacao = valor_casa / qtde_meses
30_salario = salario * 0.30

if prestacao > 30_salario:
    print('Valor da parcela excede 30% do valor do salário!')
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
    print(f'Valor da casa: R${valor_casa:.2f}')
    print(f'Valor do salário: R${salario}')
    print(f'Valor da prestação: R${prestacao}')]
    print(f'Quantidade de parcelas: R${qtde_meses}')
print('--FIM--')