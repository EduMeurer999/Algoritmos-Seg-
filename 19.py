cxAzulejo = 1.5
comprimento	= float(input('Informe comprimento da cozinha: '))
largura = float(input('Informe largura da cozinha: '))
altura = float(input('Informe altura da cozinha: '))
areaParede = (comprimento*altura)*2+(largura*altura)*2
qtdCxs = areaParede/cxAzulejo
print('Total de caixas de azulejos: ', qtdCxs)