maior = 0; nNota = 0

for x in range(10):
    nota = int(input('Informe a '+str(x+1)+'ª nota: '))
    if nota > maior:
        maior = nota
        nNota = x+1
    
print("A nota maior é a "+str(nNota)+"ª nota: ", maior)