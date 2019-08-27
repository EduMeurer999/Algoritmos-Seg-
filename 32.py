comissao = 3
comissao2 = 5
salFixo = float(input('Informe o salário Fixo: R$'))
valVendas = float(input('Informe o valor total em vendas: R$'))
if valVendas > 1500:
    subTotal = 1500 + (1500*(comissao/100))
    restTotal = valVendas-1500
    total = subTotal+(restTotal+(restTotal*(comissao2/100)))
else:
    subTotal = valVendas + (valVendas*(comissao/100))
    total = subTotal
print("Salario Total: R$",total+salFixo)