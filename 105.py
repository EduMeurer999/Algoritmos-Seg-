maior = 0
nMaior = 0
for x in range(10):
    n=x+1
    valor = float(input('Informe o '+str(n)+'º valor: '))
    while valor < 0:
        print("O valor deve ser positivo!\n")
        valor = float(input('Informe o '+str(n)+'º valor novamente: '))
    if valor > maior:
        maior = valor
        nMaior = n
print("O maior valor é o "+str(nMaior)+"º: "+str(maior))
    
