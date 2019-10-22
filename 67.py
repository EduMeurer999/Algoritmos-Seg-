a = int(input("Informe um numero entre 1 e 10: "))
while a < 1 or a > 10:
    a = int(input('Digite novamente: '))
print("Valor digitado: ",a)