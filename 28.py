v1 = float(input('Informe valor 1: '))
v2 = float(input('Informe valor 2: '))
stringfy = "%.2f "
if v1>v2:
    print(stringfy*2 % (v2, v1))
else:
    print(stringfy*2 % (v1, v2))

