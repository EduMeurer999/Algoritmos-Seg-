v1 = float(input('Informe o valor 1: '))
v2 = float(input('Informe o valor 2: '))

while (v2 == 0):
    
    print("VALOR INVÁLIDO")
    v2 = float(input('Informe um valor diferente de 0: '))

print("Divisão: ",v1/v2)