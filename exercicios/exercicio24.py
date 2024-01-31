#Exercício 4 - Funções - Womakerscode

#Solicitando digitação do usuário
saldo = float(input('Digite o valor da carteira: '))

#Saídas com as conversões
print(f'Para R${saldo:.2f} de saldo na carteira, podem ser convertidos em:')
print(f'{(saldo*4.91):.2f} Dólares Americanos.')
print(f'{(saldo*0.02):.2f} Pesos Argentinos.')
print(f'{(saldo*3.18):.2f} Dólares Australianos.')
print(f'{(saldo*3.64):.2f} Dólares Canadenses.')
print(f'{(saldo*0.42):.2f} Francos Suiços.')
print(f'{(saldo*5.36):.2f} Euros.')
print(f'{(saldo*6.21):.2f} Libras Esterlinas.')

#Finalizando
print('---')
