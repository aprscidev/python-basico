#Exercício 3 - Tomada de decisão - Womakerscode

#Solicitando digitação do valor para usuário

while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Valor inválido!')
    else:
        break

print(f'Valor válido! Valor da nota: {nota}.')

#Finalizando
print('---')