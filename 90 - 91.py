num = int(input('Informe um numero: '))
soma = 0
while num < 0:
    print("Informe um valor > 0: ")
    num = int(input(''))
for x in range(1, num+1):
    soma = soma+(x)
print("Soma: ",soma)