v1 = float(input('Informe o valor1: '))
v2 = float(input('Informe o valor2: '))
v3 = float(input('Informe o valor3: '))

if v1 > v2: #v1
    if v2 > v3: #v2 
        soma = v2 + v1
    else: #v3 
        soma = v3 + v1
      
else: #v2
    if v3 > v1: #v3
        soma = v3 + v2
    else: #v1
        soma = v2 + v1

print(soma)