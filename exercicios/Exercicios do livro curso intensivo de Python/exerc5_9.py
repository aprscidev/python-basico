#Exercicio 5.9
#Exibir saudação a cada usuário
users = ['admin', 'user1', 'user2', 'user3', 'user4']
logins = []

if not logins:
    print ("Precisamos encontrar alguns usuários.")
else:
    for login in logins:
        if login in users and login == 'admin':
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print("Olá, " + login + " obrigado por fazer login novamente")