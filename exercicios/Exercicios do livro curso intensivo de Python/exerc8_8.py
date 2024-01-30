# Exercício 8.8 - Laço while, fornecer nome de um artista e o título de um álbum

def make_album(artista, titulo):
    discos = {'Artista': artista, 'Título': titulo}
    return discos

active = True
while True:
        artista = input("Nome do artista: ")
        titulo = input("Digite o título do album: ")
        album = make_album(artista, titulo)
        print(album)
        perg = input("Gostaria de inserir um novo registro? (s/n)")
        if perg == 'n':
            active = False
            break