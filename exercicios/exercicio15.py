#Exercício 6 - Tomada de decisão - Womakerscode

#Solicitando informação de usuário e senha
login = input('Digite o login: ')
senha = input('Digite a senha: ')

#Realizando verificações
if login == "admin" and senha == "admin123":
   print('Acesso permitido')
else:
   print('Acesso negado. Credenciais inválidas!')

#Finalização
print('---')

