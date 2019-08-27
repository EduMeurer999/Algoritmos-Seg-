qtdA = float(input('Informe quantidade atual em estoque: '))
qtdMax = float(input('Informe quantidade máxima de estoque: '))
qtdMin = float(input('Informe quantidade mínima de estoque: '))
qtdMedia = (qtdMax+qtdMin)/2
if qtdA >= qtdMedia:
    print('Não efetuar compra')
else:
    print('Efetuar compra')

    