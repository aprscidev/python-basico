#Desafio 70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000
#Qual é o nome do produto mais barato

total = 0
cont1000 = 0
maisbarato = ' '
contador = 0
menorpreco = 0

while True:
    nome_produto = str(input('Digite o nome do produto: ')).upper().strip()
    preco_produto = float(input('Digite o preco do produto: '))
    total = total + preco_produto
    contador = contador + 1
    if contador == 1:
        menorpreco = preco_produto
    elif not contador == 1 and preco_produto < menorpreco:
        menorpreco = preco_produto
        maisbarato = nome_produto
    if preco_produto > 1000:
        cont1000 = cont1000 + 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Produto cadastrado. Deseja realizar novo cadastro? [S/N]')).upper().strip()
        if opcao == 'N':
            break
print(f'Total gasto na compra: R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {cont1000}')
print(f'Nome do produto mais barato: {maisbarato}, custando R${menorpreco:.2f}')