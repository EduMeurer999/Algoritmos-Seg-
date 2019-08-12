compPista = float(input('Escreva o comprimento da pista (em metros): '))
numeroVoltas = int(input('Escreva o numero de voltas: '))
numAbas = int(input('Escreva o numero de abastecimento desejado: '))
consumo = float(input('Escreva o consumo do carro (em Km/L): '))
kmR = numeroVoltas*(compPista/1000)
minAbas = kmR/consumo
print('Mínimo de litros por reabastecimento: ', minAbas, "\n")

