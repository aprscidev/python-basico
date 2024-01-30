#Exercício 3.8 - Pensar em cinco  lugares do mundo que gostaria de ir
mundo = ['Canadá', 'Irlanda', 'Alemanha', 'Japão', 'Estados Unidos']
print(mundo)

#utilizando sorted
print('Lista ordenada:') 
print(sorted(mundo))
print('Lista original:') 
print(mundo)

#utilizando sorted e reverse
print('Lista ordenada reversa:')
print(sorted(mundo, reverse=True))
print('Lista original:') 
print(mundo)

#utilizando reverse
print('Lista reversa:')
mundo.reverse()
print(mundo)

#utilizando reverse novamente
print('Lista reversa original:')
mundo.reverse()
print(mundo)

#utilizando sort
print('Lista ordenada definita:')
mundo.sort()
print(mundo)

#utilizando sort e reverse
print('Lista ordenada reversa definitiva:')
mundo.sort(reverse=True)
print(mundo)

