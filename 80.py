c = 1
valorTotal = 0
continuar = True
while continuar:
    valor = float(input('Informe o valor da '+str(c)+ "ª mercadoria: R$"))
    valorTotal = valorTotal+valor
    c=c+1
    opt = input('MAIS MERCADORIAS (S/N)? ')
    continuar = None
    while continuar == None:
        if opt == "S" or opt == "s":
            continuar = True
        elif opt == "N" or opt == "n":
            continuar = False
        else:
            opt = input('Opção inválida, informe (S/N): ')
            continuar = None
print("Valor total em estoque: R$", valorTotal/2)
print("Média de valores das mercadorias: R$"+str(valorTotal/2))
