c:int = 0
num:int = 0
soma:int = 0
while num > 0 or c == 0:
    num = int(input('Informe números positivos: '))
    soma = num+soma
    c = c+1
print("Você informou um numero negativo. \nVocê digitou "+str(c)+" vezes\nSoma dos numeros positivos digitados: "+str(soma-(-1)))