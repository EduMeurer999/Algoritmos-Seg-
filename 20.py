pComb = 4.90
kmI = float(input("Informe quilometragem do início do dia: "))
kmF = float(input("Informe quilometragem do fim do dia: "))
combustivel = float(input("Informe os litros de combustível gastos no dia: "))
valorTotal = float(input("Informe o valor recebido por passageiros: R$"))
kmTotal = kmF -kmI
kmL = kmTotal/combustivel
valComb = combustivel *pComb
lucro = valorTotal-valComb
print('\nLucro líquido: R$',lucro, "\nKm/L: ", kmL)
