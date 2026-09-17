import os
os.system("cls")



gasolina = "G"
alcool = 'A'
combustivel = input('Informe o tipo de combustivel (A - Alcool / G - Gasolina): ')
quantidade = float(input('Infome a quantidade de litros vendidos: '))
litro_gasolina = 6.59
litro_alcool = 3.79

if 'A' == combustivel:
    if quantidade <= 25:
        desconto = litro_alcool * 0.10
else:
    desconto = litro_alcool * 0.10

if 'G' == combustivel:
    if quantidade <= 25:
        desconto = litro_gasolina * 0.15
else:
    desconto = litro_gasolina * 0.30

