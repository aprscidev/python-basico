#Exercicio 5.10
current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['user5', 'user1', 'user6', 'user7', 'user2']

#Verificando disponibilidade do nome de usuário - Rever
for new_user in new_users:
    if new_user in current_users:
        if ((new_user.islower()) == True) or ((new_user.isupper()) == True):
            print("Nome em uso: " + new_user + ". Deverá fornecer um novo nome.")
    else:
        print("Nome de usuário disponível: " + new_user)