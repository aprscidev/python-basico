#Desafio 73 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética
#D) Em que posição na tabela está o time da Chapecoense

tabela = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Fortaleza', 'São Paulo', 'Internacional', 'Cuiabá', 'Corinthians', 'Santos', 'Bahia', 'Vasco da Gama', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')

print(f'Times do Brasileirão: {tabela}.')
print(f'Os primeiros 5 colocados: {tabela[0:5]}.')
print(f'Os últimos quatro colocados na tabela: {tabela[-4:]}')
print(f'Lista dos times em ordem alfabética: {sorted(tabela)}')
#print(f'Posição na tabela do time da Chapecoense: {tabela.index('Chapecoense').}')