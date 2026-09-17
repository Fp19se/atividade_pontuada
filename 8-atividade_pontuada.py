import os
os.system('cls')

print('''
Cores:

Verde
Azul
Amarelo
Vermelho
''')

cor = str(input('Escreva qual cor você quer: ')).lower()

match cor:
    case 'verde':
        print('\nA cor Verde é: R$ 10,00')
    case 'azul':
        print('\nA cor Azul é: R$ 20,00')
    case 'amarelo':
        print('\nA cor Amarelo é: R$ 30,00')
    case 'vermelho':
        print('\nA cor Vermelho é: R$ 40,00')