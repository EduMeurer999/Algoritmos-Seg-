nMenor = ""
menor = 1000
for x in range(10):
    n = str(x+1)
    valor = float(input('Informe o '+n+'º valor (de 1 até 1000): '))
    while valor < 1 or valor > 1000:
        print("Valor inválido!\n")
        valor = float(input('Informe o '+n+'º valor novamente: '))
    if valor < menor:
        menor = valor
        nMenor = n
print("O maior valor é o "+nMenor+"º valor: "+str(menor))