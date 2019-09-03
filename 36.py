v1 = float(input('Informe o valor1: '))
v2 = float(input('Informe o valor2: '))
v3 = float(input('Informe o valor3: '))

if v1 > v2:
    if v1 > v3:
        print("Valor 1 é o maior!")
    else:
        if v3 > v2:
            print("Valor 3 é o maior!")
        else:
            if v2 > v3:
                print("Valor 2 é o maior!")
else:
    if v2 > v3:
        print("Valor 2 é o maior!")
    else:
        print("Valor 3 é o maior!")