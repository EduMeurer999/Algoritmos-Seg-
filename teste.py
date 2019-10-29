layla = {'tipo':'cachorro', 'nome_dono':'lucas'}
ratata = {'tipo':'rato', 'nome_dono': 'Dante'}
pikachu = {'tipo': 'furão', 'nome_dono':'Ash'}

pets = [{"layla":layla}, {"ratata": ratata}, {"pikachu":pikachu}]
for animal in pets:
    nome_animal = ""
    for e in animal:
        nome_animal = e
    print("Nome do animal: "+nome_animal)
    p = animal[nome_animal]
    print ("Nome do dono:", p["nome_dono"].title(),"\nEspécie do animal:", p["tipo"].title(), "\n")