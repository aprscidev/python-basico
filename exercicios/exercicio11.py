#Exercício 2 - Tomada de decisão - Womakerscode

#Solicitando informação do turno para o usuário
turno = input('Digite qual turno você estuda: [M] Matutino, [V] Vespertino, [N] Nortuno: ').upper().split()

#Estrutura condicional
if turno == "M":
    print('Bom dia!')
elif turno == "V":
    print('Boa tarde!')
elif turno == "N":
    print('Boa noite!')
else:
    print('Valor inválido!')

#Finalizando
print('---')