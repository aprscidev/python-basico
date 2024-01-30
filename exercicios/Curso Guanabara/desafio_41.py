#Desafio 41 - A Confederação Nacional de natação precisa de um pograma que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = int(date.today().year - ano)

if idade <= 9:
    print(f'MIRIM. Idade: {idade} anos. ')
elif idade > 9 and idade <= 14:
    print(f'INFANTIL. Idade: {idade} anos.')
elif idade > 14 and idade <= 19:
    print(f'JUNIOR. Idade: {idade} anos.')
elif idade > 19 and idade <= 20:
    print(f'SENIOR. Idade: {idade} anos.')
else:
    print(f'MASTER. Idade: {idade} anos.')
print('--FIM--')