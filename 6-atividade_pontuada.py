import os
os.system('cls')

nota1 = int(input('Digite uma nota: '))
nota2 = int(input('Digite uma sugunda nota: '))

media = (nota1 + nota2) / 2

print('\nSua média:', media )
if media >= 6:
    print('Parabéns')
elif media >= 4.1 and media <= 5.9:
    print('Recuperação')
else:
    print('Reprovado')

