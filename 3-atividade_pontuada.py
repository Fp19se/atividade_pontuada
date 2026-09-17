import os
os.system('cls')

A = int(input('Digite um valor: '))
B = int(input('Digite outro valor: '))

C = A + B
D = A * B

if A == B:
    print('Os valores são iguais: ', C)
else:
    print('Os valores não são iguais: ', D)
