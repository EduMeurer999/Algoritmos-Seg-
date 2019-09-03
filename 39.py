# A = float(input('Informa lado 1: '))
# B = float(input('Informe lado 2: '))
# C = float(input('Informe lado 3: '))

# if C < A+B: #C
#     if A < C+B: #A
#         if B < C+A: #B
#             print("Forma um triângulo")
#         else:
#             print("Não forma um triângulo")
#     else:
#         print("Não forma um triângulo")
# else:
#     print("Não forma um triângulo")


print("\n")
def desenharR(A,B):
    dA = "|"
    dB = "-"
    space= " "
    print("+",dB*B, "+")
    for x in range(0, A):
        print(dA,space*B,dA)
    
    print("+",dB*B, "+")

def desenharT(v1, v2, v3):
    dV1 = "--"
    dV2 = "/"
    dV3 = "\\"
    space= " "
    for x in range(0, v1):
        q = x
        print(space*(v1-q),dV2, space*x, dV3)
        if(x == v1-1):
            print(" ",dV1*v1)
        q = q-1



desenharT(2,1,1)
        

        

    