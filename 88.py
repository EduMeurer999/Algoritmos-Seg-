ENV = "DEV"
vz = 300 if ENV == "PROD" else 5
soma = 0
for x in range(0,vz):
    num = float(input("Informe um numero: "))    
    soma = soma+num
print("Soma total: ", soma)
