notas=["1", "2"]
for x in range(0,len(notas)):
    notas.append(float(input(str("Informe nota {}: ".format(notas[x])))))
soma = 0
for x in range(2, len(notas)):
    soma+=notas[x]
print("Média: ", soma/2)
if soma/2 >=6:
    print("PARABÉNS! Você foi aprovado!")
else:
    print("Você foi REPROVADO! Estude mais...")