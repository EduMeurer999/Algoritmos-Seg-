entre_10_20_i = 0
fora = 0
for x in range(0, 10):
    num = int(input('Informe o '+str(x+1)+"º valor: "))
    if num >=10 and num <=20:
        entre_10_20_i = entre_10_20_i+1
    else:
        fora = fora+1
print("Qtd de numeros entre 10 e 20: ", entre_10_20_i)
print('QTD d enumeros fora do intervalo 10 e 20: ', fora)
