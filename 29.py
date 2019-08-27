horaI = int(input('Informe hora início Xadrez: ')) 
horaF = int(input('Informe hora fim Xadrez: '))
maxHora = 24
if horaI >= horaF:
    duracao = (maxHora-horaI)+horaF
else:
    duracao = horaF-horaI
print('Duração: %.0dh' % duracao)

