pReq = 18
pLampada = float(input('Informe a potência da lâmpada (em Watts): '))
largura = float(input('Informe a largura do cômodo (em metros): '))
comprimento = float(input('Informe o comprimento do cômodo (em metros): '))
area = largura*comprimento
qtdWatts = area*18
qtdLampadas = qtdWatts/pLampada
print('Você vai precisar de ', qtdLampadas, " lâmpadas")
