nConta = input('Informe numero da conta: ')
saldo = float(input('Informe saldo: R$'))
credito =  float(input('Informe Crédito: R$'))
debito = float(input('Informe Débito: R$'))
saldoA = saldo-debito+credito
if saldoA >= 0:
    print("Saldo Positivo!")
else:
    print("Saldo Negativo!")
