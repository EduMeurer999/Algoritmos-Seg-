acr = 50#Porcentagem de acréscimo
horaTrab = int(input("Informe o total de horas trabalhadas: "))
salHora = float(input('Informe salário/hora: '))

if horaTrab> 160:
    salParc = salHora*160
    salTotal = salParc+((horaTrab-160)*(salHora+(salHora*(acr/100))))
else:
    salTotal = horaTrab*salHora
print("Salário total: %.2f" % salTotal)

