def interface(width, height, content):
    maxLength = len(max(content))
    if height == "AUTO":
        y = "|"
        x = "--"
        strI = ""
        strI += (x*width)+"\n"
        for l in content:
            strI += y+" "+l+" "+y+ "\n"
        strI += x*width
        return strI   



d = [2, 3, 5]
desc = input('Nome do produto: ')
qtd = int(input('Quantidade: '))
preco = float(input('Preço: '))
total = qtd*preco
if qtd <= 5:
    desconto = total - (total*(d[0]/100))
elif qtd > 5 and qtd <= 10:
    desconto = total - (total*(d[1]/100))
else:
    desconto = total -(total*(d[2]/100))


strS = ["Produto: "+desc, "Total: R${:.2f}".format(total), "Total com desconto: R${:.2f}".format(desconto), "Desconto: R${:.2f}".format(total-desconto)]
a = max(strS)
print(a)
print(interface(100, "AUTO", strS))



