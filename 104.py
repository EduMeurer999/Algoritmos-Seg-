maior = 0
nMaior = 0
for x in range(10):
    valor = float(input('Informe o '+str(x+1)+'º valor: '))
    if valor > maior:
        maior = valor
        nMaior = x+1
print("O maior valor é o "+str(nMaior)+"º: "+str(maior))
    
