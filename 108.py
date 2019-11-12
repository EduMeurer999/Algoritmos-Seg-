menor = 1000
maior = 0
nMaior = ""
nMenor = ""
for x in range(10):
    n= str(x+1)
    valor = float(input('Informe '+n+'º valor (de 1 até 1000): '))
    while valor < 1 or valor > 1000:
        print("Valor inválido!")
        valor = float(input('Informe o '+n+'º valor novamente: '))
    if valor > maior:
        maior = valor
        nMaior = n
    if valor < menor:
        menor = valor
        nMenor = n
print("Maior | "+nMaior+"º valor: "+str(maior))
print("Menor | "+nMenor+"º valor: "+str(menor))