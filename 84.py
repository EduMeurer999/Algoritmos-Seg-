n = 0
while n <= 0:
    try:
        n = int(input('Informe um número maior que 0: '))
    except:
        print("Você deve digitar um numero inteiro: ")
        n = 0
for x in range(1, n+1):
    print(x)
    