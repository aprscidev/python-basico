#Exercicio 5.8
#Exibir saudação a cada usuário
users = ['admin', 'user1', 'user2', 'user3', 'user4']
logins = ['admin']

for login in logins:
    if login in users and login == 'admin':
        print("Olá admin, gostaria de ver um relatório de status?")
    else:
        print("Olá, " + login + " obrigado por fazer login novamente")