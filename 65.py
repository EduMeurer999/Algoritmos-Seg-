anoAtual = 2019
codF = input('Código do funcionário: ')
anoNasc = int(input('Informe ano de nascimento: '))
ingresso = int(input('Ano de ingresso na empresa: '))
tempoTrab = anoAtual-ingresso
idade = anoAtual-anoNasc
print('-------------------------\nTempo de trabalho: {} anos\nIdade: {} anos'.format(tempoTrab, idade))
if idade >= 65 or tempoTrab >= 30 or idade >=60 and tempoTrab >= 25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")