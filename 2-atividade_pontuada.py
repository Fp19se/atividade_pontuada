import os
os.system('cls')

nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo (F) ou (M): ')).upper()
est = str(input('Digite seu estado civil: ')).upper()

if sexo == 'F' and est == 'CASADA':
    tempo = input('Informe o tempo de casada: ')
else:
    exit() # FIM DO PROGRAMA.

print('\nSeu nome: ', nome)
print('Seu sexo: ', sexo)
print('Seu estado civil: ', est)
print('Tempo de casada: ', tempo)