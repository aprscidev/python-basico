# Exercício 8.7 - Album contendo nome do artista e o título de um album

def make_album(artista, titulo, faixas=''):
    disco = {'Artista': artista, 'Título': titulo}
    if faixas:
        disco['Faixas'] = faixas
    return disco

album = make_album('Jimi Hendrix', 'Disco 1', faixas=15)
print(album)
