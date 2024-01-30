#Exercício 4.12
#Laços para exibir cada lista de comidas
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#Laço para imprimir listas originais
print("Minhas comidas são:")
for food in my_foods:
    print(food)

print("As comidas do meu amigo são:")
for ffood in friend_foods:
    print(ffood)

#Acrescentando dados às listas
my_foods.append('cannoli')
friend_foods.append('ice cream')

#Laço para imprimir listas modificadas
print("Agora minhas comidas são:")
for food in my_foods:
    print(food)

print("Agora as comidas do meu amigo são:")
for ffood in friend_foods:
    print(ffood)