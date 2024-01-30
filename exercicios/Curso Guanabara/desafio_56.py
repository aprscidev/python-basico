#Desafio 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaidade = 0
contmenos20 = 0
idadehomemvelho = 0
nomehomemvelho = ''

for p in range (1, 5):
    print(f'Pessoa {p} de 4')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).upper()
    somaidade = somaidade + idade
    if p == 1:
        idadehomemvelho = idade
    elif sexo == 'M' and idade < idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
    elif sexo == 'F' and idade < 20:
        contmenos20 = contmenos20 + 1

mediaidade = somaidade / 5

print(f'A média das idades do grupo é: {mediaidade}')
print(f'Nome do homem mais velho: {nomehomemvelho}, com {idadehomemvelho} anos.')
print(f'Quantidade de mulheres com menos de 20 anos: {contmenos20}')




