import os
os.system('cls')

print('''
===Tabela de Preços===
FRUTAS            5KG                     ACIMA DE 5KG
Morango           R$ 2,50 por Kg          R$ 2,20
Maçã              R$ 1,80 por Kg          R$ 1,50
''')

qtd1 = int(input('Digite a quantidade em Kg de Morango: '))
qtd2 = int(input('Digite a quantidade em Kg de Maça: '))

if qtd1 <= 5:
    preco_morango = qtd1 * 2.50
else:
    preco_morango = qtd1 * 2.20

if qtd2 <= 5:
    preco_macas = qtd2 * 1.80
else:
    preco_macas = qtd2 * 1.50

total_kg = qtd1 + qtd2
total_pagar = preco_morango + preco_macas

if total_kg >= 10 or total_pagar > 15.00:
    desconto = total_pagar * 0.10
    total_pagar = total_pagar - desconto

print('Valor total a pagar: R$', total_pagar)