def menu():
    print("Menu: \nPrograma seu sálario com acréscimo, seja bem vindo!: \nNossa empresa fornece um acrescimo de 50%, para as horas extras (acima de 160h ao mês). \nPara realizar um calculo: digite '1' \nPara Sair: aperte qualquer tecla que não seja o numero '1'")
    opt = input("")
    if opt == '1':
        return True
    else:
        return False

def continuar():
    opt = input("Executar novamente: (S/N): ")
    if opt == 'S' or opt == 's':
        a = menu()
    else:
        a= False
    return a


a = menu()
while a:
    try:
        acr = 50 #Porcentagem de acréscimo
        horaTrab = int(input("Informe o total de horas trabalhadas: "))
        salHora = float(input('Informe salário/hora: '))
        if horaTrab> 160:
            salParc = salHora*160
            salTotal = salParc+((horaTrab-160)*(salHora+(salHora*(acr/100))))
        else:
            salTotal = horaTrab*salHora
        print("Salário total: %.2f" % salTotal)
        a = continuar()
    except:
        print("Erro: ")
        a = continuar()
        


