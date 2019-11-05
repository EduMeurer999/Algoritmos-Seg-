vz = int(input('Informe quantos numeros você quer digitar: '))
soma = 0
for x in range(0, vz):
    val = float(input("Informe o "+str(x+1)+"º valor: "))
    soma = soma+val
print("Soma total: ", soma)