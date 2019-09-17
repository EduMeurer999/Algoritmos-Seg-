A = float(input('Informa lado 1: '))
B = float(input('Informe lado 2: '))
C = float(input('Informe lado 3: '))

if C < A+B: #C
    if A < C+B: #A
        if B < C+A: #B
            print("Forma um triângulo")
        else:
            print("Não forma um triângulo")
    else:
        print("Não forma um triângulo")
else:
    print("Não forma um triângulo")