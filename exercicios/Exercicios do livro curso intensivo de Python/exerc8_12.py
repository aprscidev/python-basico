# Exercicio 8.12 - Lista de itens num sanduiche. Apresentar resumo do sanduiche feito.

def make_sandwich(*toppings):
    print("\nFazendo o sanduíche com os seguintes ingredientes: ")
    for topping in toppings:
        print("- " + topping)

make_sandwich('presunto')
make_sandwich('presunto', 'queijo')
make_sandwich('mortadela', 'presunto', 'queijo')