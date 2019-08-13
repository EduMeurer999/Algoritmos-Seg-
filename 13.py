pImp = 45 #em porcentagem (ex: 45% = 45)
pDist = 28 #em porcentagem (ex: 28% = 28)
cFab = float(input('Informe o custo de fábrica do carro R$'))
custoCarro = cFab+(cFab*(pImp/100))+(cFab*(pDist/100))
print("Valor Final (com impostos e percentual de distribuição) \nR$",custoCarro)

