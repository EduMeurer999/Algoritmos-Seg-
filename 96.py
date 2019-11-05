negativos = 0
for x in range(0, 10):
    num = int(input('Informe o '+str(x+1)+"º valor: "))
    if num <0 :
        negativos = negativos +1
    
print("QTD de valores negativos: ", negativos)
    