nMac = int(input('Informe o numero de Maçãs compradas: '))
if nMac <12:
    preco = nMac*1.5
elif nMac >0 and nMac>=12:
    preco = nMac*1.2
print('Valor total: R$ %.2f' % preco)