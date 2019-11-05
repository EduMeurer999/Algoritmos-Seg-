val = int(input('Informa um valor: '))
print("Tabuada do "+str(val))
while (val < 0 or val >10):
    print("Valor inválido, informe um numero de 1 a 10: ")
    val = int(input(''))
for x in range(0,10+1):
    print(str(val)+ "x"+str(x)+" = "+str(val*x))
