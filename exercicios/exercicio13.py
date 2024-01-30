#Exercício 4 - Tomada de decisão - Womakerscode

#Solicitando digitação do valor para usuário

while True:
    nota = int(input('Digite a nota do exame do aluno entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Valor inválido!')
    else:
        break

if nota >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')

#Finalizando
print('---')
  