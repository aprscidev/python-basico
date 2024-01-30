#Exercicio 4.11
pizzas = ['Calabresa', 'Portuguesa', 'Marguerita']
friend_pizzas = pizzas[:]

print("Minhas pizzas favoritas são:")
print(pizzas)
print("As pizzas favoritas do meu amigo são:")
print(friend_pizzas)

#Adicionando uma nova pizza à lista original
pizzas.append('Presunto')

#Adicionando uma pizza diferente à lista friend_pizzas
friend_pizzas.append('Muçarela')

print("Minhas pizzas favoritas são:")
print(pizzas)
print("As pizzas favoritas do meu amigo são:")
print(friend_pizzas)