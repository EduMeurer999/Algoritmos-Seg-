num = int(input('Informe um numero: '))
result = 1
while num < 0:
    print("Numero < 0!")
    num = int(input('Informe um numero: '))

if num == 0:
    result = 1
else:
    for x in range(1, num+1):
        result = result*x
print("Resultado: ",result)