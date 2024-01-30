#Exercício 7.2
pessoas = input("Digite a quantidade de pessoas em seu grupo para jantar: ")
pessoas = int(pessoas)
if pessoas > 8:
    print("Mais do que 8 pessoas. Vocês deverão aguardar por uma mensa.")
else:
    print("Menos do que 8 pessoas. Sua mesa está pronta.")