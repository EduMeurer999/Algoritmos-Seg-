arr = ["1", "2", "optativa"]
nota = []
for x in arr:
    nota.append(float(input('Informe nota '+x+": ")))
s = ""
if nota[2] >=0:
    if nota[0]>nota[1]:
        media =nota[0]+nota[2] 
    elif nota[1]>nota[0]:
        media = nota[1]+nota[2]
    else:
        media = nota[1]+nota[2]
else:
    media = nota[1]+ nota[0]
r = media/2
print("Média: %.2f"% r)
if r >=6:
    print("Aprovado!")
elif r <3:
    print("Reprovado!")
else:
    print("Exame!")