import os
os.system('cls')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um segundo número: '))
carac = input('Digite um caracter: ')

soma = num1 + num2
subtracacao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print('\nPrimeiro Número: ', num1)
print('Segundo Número: ', num2)
print('Caracter: ', carac)
match carac:
    case '+':
        print('Resultado: ', soma)
    case '-':
        print('Resultado: ', subtracacao)
    case '*':
        print('Resultado: ', multiplicacao)
    case '/':
        print('Resultado: ', divisao)
        