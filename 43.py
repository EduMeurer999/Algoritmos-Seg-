import time
def abastecer(litros, valor, total):
    vazao = 10
    lp = litros/vazao
    for x in range(1, vazao+1):
        print("Abastecendo {0} litros | Valor total: R${1}".format(lp*x,(valor*(lp*x)+valor)), end="\r")
        time.sleep(0.5)
    print("\r")
    
    print("Valor total com desconto: R$%.2f" % total)
        
        



dG20 = 6 # 6%
dA20 = 5 # 5%
dG = 4 # 4%
dA = 3 # 3%
pA = 3.90 # R$
pG = 4.30 # R$
tipoC = input('Informe tipo de Combustível: (A: Alcool | G - Gasolina): ')
l = int(input('Litros a abastecer: '))
if tipoC == "A":
    s = l*pA
    p= pA
    if l > 20:
        total = s - (s*dA20/100)
    else:
        total = s - (s*dA/100)
else:
    p =pG
    s = l*pG
    if l > 20:
        total = s - (s*dG20/100)
    else:
        total = s - (s*dG/100)

abastecer(l, p, total)




