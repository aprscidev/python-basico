#Desafio 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO"

cid = str(input('Digite a cidade que vocÊ nasceu: ')).strip()
if cid[:5].title() == 'Santo':
    print('O nome da cidade começa com SANTO.')
else:
    print('O nome da cidade não começa com SANTO.')


