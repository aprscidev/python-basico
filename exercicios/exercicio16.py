#Exercício 7 - Tomada de decisão - Womakerscode

#Solicitando a digitação da idade do usuário
idade = int(input('Digite sua idade: '))

#Realizando verificações
if idade >= 0 and idade <= 12:
    print('Criança!')
elif idade > 12 and idade < 18:
    print('Adolescente!')
elif idade >= 18 and idade < 60:
    print('Adulto!')
elif idade >= 60:
    print('Idoso!')

#Finalização
print('---')
