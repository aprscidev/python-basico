#Desafio 39 - Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é hora de se alistar.
#Se já passou o tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = int(date.today().year - ano)
if idade < 18:
    tempo = 18 - idade
    print(f'Faltam {tempo} anos para efetuar o alistamento. Idade: {idade} anos.')
elif idade == 18:
    print(f'É hora de se alistar! Idade: {idade} anos.')
elif idade > 18:
    tempo = idade - 18
    print(f'Já passou {tempo} anos do prazo de alistamento. Idade: {idade} anos.')
print('--FIM--')
