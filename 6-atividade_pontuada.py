import os
os.system('cls')

produto = str(input('Qual o produto você deseja comprar: '))
quant = int(input('Qual a quantidade adquirida: '))
preco = float(input('Qual o preço do produto: '))

total = quant * preco

if quant <= 5:
    desconto = total * 0.02
elif quant > 5 and quant <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

total_a_pagar = total - desconto

print('\nSeu produto é: ', produto)
print('A quantidade escolhida: ', quant)
print('O preco do produto: R$', preco)
print('O total deu: R$', total)
print('O desconto é: R$', desconto)
print('O valor a pagar é: R$', total_a_pagar)
