nTime1 = input('Informe nome do time 1: ')
nGolT1 = int(input('Informe o numero de gols do time '+nTime1+' na partida: '))
nTime2 = input('Informe nome do time 2: ')
nGolT2 = int(input('Informe o numero de gols do time '+nTime2+' na partida: '))
if nGolT1 > nGolT2:
    print(nTime1, " ganhou!!!")
else:
    if nGolT2 > nGolT1:
        print(nTime2, " ganhou!!!")
    else:
        print("EMPATE!")

