import os
repetir = True
while(repetir):
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = float(input('Informe um valor: '))
    
    if valor >=0:
        print('\nÉ positivo!')
    else:
        print('\nÉ negativo!')
    continuar = input("Deseja continuar: \n1 - SIM \nQualquer outra tecla - Não \n")
    if continuar == '1':
        repetir = True
    else:
        repetir= False

