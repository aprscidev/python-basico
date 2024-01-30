#Exercicio 3.10
idiomas = ['Ingles', 'Espanhol', 'Japones', 'Alemao', 'Mandarim', 'Frances', 'Arabe', 'Russo']
print(idiomas)

#utilizando funcao sorted
print("Lista Ordenada temporariamente:")
print(sorted(idiomas))
print("Lista original:")
print(idiomas)

#utilizando sorted e reverse
print("Lista Ordenada reversa:")
print(sorted(idiomas, reverse=True))
print("Lista original:")
print(idiomas)

#utilizando reverse
print("Lista reversa:")
idiomas.reverse()
print(idiomas)

#utilizando reverse novamente
print("Lista reversa:")
idiomas.reverse()
print(idiomas)

#utilizando sort
print("Lista ordenada em definitivo:")
idiomas.sort()
print(idiomas)

#utilizando sort e reverse
print("Lista ordenada reversa:")
idiomas.sort(reverse=True)
print(idiomas)



