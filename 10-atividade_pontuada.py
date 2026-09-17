import os
os.system("cls")

gasolina = "G"
alcool = "A"

combustivel = input('Informe o tipo de combustivel (A - Alcool / G - Gasolina): ').upper()
quantidade = float(input('Informe a quantidade de litros que deseja: '))

litro_gasolina = 6.59
litro_alcool = 3.79

if combustivel == alcool:
    if quantidade <= 25:
        desconto = 0.10
    else:
        desconto = 0.20

    total = quantidade * litro_alcool

elif combustivel == gasolina:
    if quantidade <= 25:
        desconto = 0.15
    else:
        desconto = 0.30

    total = quantidade * litro_gasolina

valor_desconto = total * desconto
valor_a_pagar = total - valor_desconto

print('\nValor total: R$', total)
print('Desconto: R$', valor_desconto)
print('Valor a pagar: R$', valor_a_pagar)
