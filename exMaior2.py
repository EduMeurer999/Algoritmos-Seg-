valor = int(input('Informe o 1º valor: '))
maior = valor
nMaior = 0
for x in range(1,10):
    valor = int(input('Informe o '+ str(x+1)+"º valor: "))
    if valor > maior:
        maior = valor
        nMaior = x+1
    
print("O maior valor é o "+str(nMaior)+"º : "+str(maior))