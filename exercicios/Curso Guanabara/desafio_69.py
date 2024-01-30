#Desafio 69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostrar:
#Quantas pessoas tem mais de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 anos

idade = 0
contmaior18 = 0
contmenos20f = 0
contmasc = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo (M/F): ')).upper().strip()[0]
    if idade >= 18:
        contmaior18 = contmaior18 + 1
    elif idade < 20 and sexo == 'F':
        contmenos20f = contmenos20f + 1
    elif sexo == 'M':
        contmasc = contmasc + 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Cadastro efetuado. Deseja realizar um novo cadastro? (S/N)')).upper().strip()[0]
    if opcao == 'N':
            break
print(f'Quantidade de pessoas com mais de 18 anos: {contmaior18}')
print(f'Quantidade de homens cadastrados: {contmasc}')
print(f'Quantidade de mulheres com menos de 20 anos: {contmenos20f}')
print('--FIM--')
