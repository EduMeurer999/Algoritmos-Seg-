anoAtual = int(input('Informe o ano atual: '))
anoNasc = int(input('Informe o ano de nascimento: '))
idadeAnos = anoAtual - anoNasc
if idadeAnos >=18:
    print('Você pode votar!')
elif idadeAnos<18 and idadeAnos> 0:
    print('Você não pode votar!')
else:
    print('Idade inválida')
