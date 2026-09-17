import os
os.system('cls')

valor_total = float(input('Digite o valor do emprestimo: '))
renda = float(input('Digite sua renda mensal: '))
parcela = int(input('Digite o número de prestações: '))


prestacao = valor_total / parcela
max_emprestimo = renda * 10
max_prestacao = renda * 0.3

if valor_total <= max_emprestimo and prestacao <= max_prestacao:
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')
