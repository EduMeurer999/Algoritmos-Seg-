ENV = "DEV"
vz = 50 if ENV == "PROD" else 5
soma = 0
for x in range(0,vz):
    num = float(input('Informe o '+str(x+1)+"º valor: "))
    soma = soma+num
print("Média aritmética: ", soma/vz)