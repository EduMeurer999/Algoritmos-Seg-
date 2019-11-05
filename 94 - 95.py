num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))
soma  = 0
while num1 > num2:
    print("O 1º valor deve ser < que o 2º: ")
    print("Informe o 1º valor novamente: ")
    num1 = int(input())
for x in range(num1, num2+1):
    soma = soma +x 
print("Soma: ", soma)

