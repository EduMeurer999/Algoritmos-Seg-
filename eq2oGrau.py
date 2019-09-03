import math
a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))
delta = (b**2)+(0-4*a*c)
if(delta < 0):
    print("Não há solução no conjunto dos numero reais! Não é possível realizar a operação √")
else:
    xPos =  (0-b+(delta**(1/2)))/(2*a)
    xNeg = (0-b-(delta**(1/2)))/(2*a)
    print("x1: ",xPos)
    print("x2: ",xNeg)



