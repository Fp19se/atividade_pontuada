import os
os.system('cls')

A = int(input('Digite um número: '))
B = int(input('Digite o sengundo número: '))
C = int(input('Digite o terceiro número: '))

D = A + B

if D < C:
    print('A + B é menor que C')
else:
    print('A + B é maior que C')