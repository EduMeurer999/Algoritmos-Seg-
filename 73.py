op = True
while(op):
    try:
        n1 = float(input('Informe 1ª avaliação: '))
        n2 = float(input('Informe 2ª avalização: '))
        n1Verify = n1 >= 0 and n1 <= 10
        n2Verify = n2 >= 0 and n2 <= 10
        op = False
    except:
        op = True
        print("Valor inválido: ")   



while(not n1Verify or not n2Verify):
    if(not n1Verify):
        n1 = float(input('Nota 1 inválida, informe novamente: '))
        n1Verify = n1 >= 0 and n1 <= 10
    if(not n2Verify):
        n2 = float(input('Nota 2 inválida, informe novamente: '))
        n2Verify = n2 >= 0 and n2 <= 10
print("Média: ", (n1+n2)/2)