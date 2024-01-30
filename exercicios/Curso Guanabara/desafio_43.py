#Desafio 43 - Desenvolva uma lógia que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela abaixo.
#Abaixo dos 18.5: Abaixo do peso.
#Entre 18.5 e 25: Peso Ideal.
#25 até 30: Sobrepeso
#30 até 40: Obesidade.
#Acima de 40: Obesidade mórbida.

peso = float(input('Digite o peso em quilos: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Abaixo do peso. IMC: {imc:.2f}.')
elif imc >= 18.5 and imc < 25:
    print(f'Peso Ideal. IMC: {imc:.2f}.')
elif imc >= 25 and imc < 30:
    print(f'Sobrepeso. IMC: {imc:.2f}.')
elif imc >= 30 and imc < 40:
    print(f'Obesidade. IMC: {imc:.2f}.')
else:
    print(f'Obesidade mórbida. IMC: {imc:.2f}')
print('--FIM--')
