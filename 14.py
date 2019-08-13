pVendas = 5
carroVend = int(input('Informe o total de carros vendidos: '))
totalVendas = float(input('Informe o valor total de vendas: R$'))
salFixo = float(input('Informe o salário fixo: R$'))
pCarVendido = float(input('Informe a comissão fixa (por carro vendido): R$'))
salarioFinal = salFixo+(pCarVendido*carroVend)+(totalVendas*(pVendas/100))
print('Salário Final: R$', salarioFinal)