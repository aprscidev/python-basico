# Exercício 8.9

def show_magicians(nomes):
    for nome in nomes:
        msg = "Nome do mágico:" + nome.title()
        print(msg)

magicos = ['mister M', 'Houdinni', 'mágico 3']
show_magicians(magicos)