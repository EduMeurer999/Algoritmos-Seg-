eleitores = float(input('Informe o total de eleitores: '))
vBrancos = float(input('Informe o total de votos brancos: '))
vNulos = float(input('Informe o total de votos nulos: '))
vValidos = float(input('Informe o total de votos válidos: '))
pValidos = (vValidos/eleitores)*100
pNulos = (vNulos/eleitores)*100
pBrancos = (vBrancos/eleitores)*100
print(
    'Total de eleitores: ', eleitores,
    "\nVotos Válidos: ", pValidos,"%", 
    "\nVotos nulos: ", pNulos, "%", 
    "\nVotos Brancos: ", pBrancos, "%"
)


