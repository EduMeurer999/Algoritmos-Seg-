a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))
delta = (b**2)-4*a*c
xPos = -b+(delta**(1/2))


print(xPos)


print(xPos)
def getVars(eq, var):
    
    if var == 'x²':
        indexVar = eq.find(var)
        count = 0
        variavel = ""
        while count<indexVar:
            variavel = str(variavel+eq[count])
            count = count+1
    elif var == 'x':
        count = eq.find('x²')+1
        
        verify = eq[count+1]
       
            
        print(count)
        print(indexVar)
        variavel = ""
        while count<indexVar:
            variavel = str(variavel+eq[count])
            count = count+1
    else:
        indexVar = eq.find("=")
        count = eq.find('x')+1
        variavel = ""
        while count<indexVar:
            variavel = str(variavel+eq[count])
            count = count+1

    
    return variavel

