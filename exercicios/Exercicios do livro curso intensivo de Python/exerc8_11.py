# Exercício 8.11

def show_magicians(nomes):
    for nome in nomes:
        msg = "Nome do mágico:" + nome.title()
        print(msg)

def make_great(nomes):
    novas_listas = []
    while magicos:
        nome_novo = magicos.pop()
        novas_listas.append(nome_novo)
    for nova_lista in novas_listas:
        print("O Grande " + nova_lista)

magicos = ['mister M', 'Houdinni', 'mágico 3']

show_magicians(magicos)
make_great(magicos)