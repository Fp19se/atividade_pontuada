import os
os.system('cls')

produto = str(input('Qual o produto você deseja comprar: '))
quant = int(input('Qual a quantidade adquirida: '))
preco = int(input('Qual o preço do produto: '))


if quant <= 5:
    desconto = preco * 0.02
elif quant > 5 and quant <= 10:
    desconto = preco * 0.03
else:
    desconto = preco * 0.05


total = quant * preco
total_a_pagar = total - desconto

print('\nSeu produto é: ', produto)
print('A quantidade escolhida: ', quant)
print('O preco do produto: ', preco)
print('O total deu: ', total)
print('O desconto é: ', desconto,'%')
print('O valor descontado é: ', total_a_pagar)
