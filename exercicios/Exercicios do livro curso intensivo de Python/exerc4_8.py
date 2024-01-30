#Exercicio 4.8
#Lista de cubos de 1 a 10
cubos=[]
for value in range(1,11):
    cubos.append(value**3)
print('Lista de cubos de 1 a 10:')
print(cubos)

#Exercicio 4.10
#Exibir a mensagem para os três primeiros itens da lista
print('Os três primeiros números da lista são:')
for value in cubos[:3]:
    print(value)

#Exibir os três números do meio da lista
print('Os três números do meio da lista são:')
for value in cubos[5:8]:
    print(value)

#Exibir os três últimos números da lista
print('Os três últimos números da lista são:')
for value in cubos[-3:]:
    print(value)


