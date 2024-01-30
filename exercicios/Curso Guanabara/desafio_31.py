#Desafio 31 - Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando
#R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas.

km = int(input('Digite a distância da viagem em KM: '))
if km <= 200:
    passagem = km * 0.5
    print(f'Preço da passagem: R${passagem:.2f}')
else:
    passagem = km * 0.45
    print(f'Preço da passagem: R${passagem:.2f}')
print('--FIM--')