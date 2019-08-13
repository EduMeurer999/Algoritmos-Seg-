n1 = float(input('Informe nota 1: '))
n2 = float(input('Informe nota 2: '))
media = (n1+n2)/2
print('\nMédia aritmética: %.2f' % media)
if media >= 6:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')