nMaior = ""
for x in range(10):
    n = str(x+1)
    valor = float(input('Informe o '+n+'º valor: '))
    if x == 0:
        maior = valor
    elif valor > maior:
        maior = valor
        nMaior = n
print("Maior | "+nMaior+"º valor: "+str(maior))