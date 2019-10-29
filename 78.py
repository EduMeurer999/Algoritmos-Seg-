senhaCorreta = "12345"
senha = input('Informe a senha: ')
c=1
while senha != senhaCorreta:
    c = c+1
    print("Senha inválida\n")
    senha = input('Informe a senha novamente: ')

print("Você errou a senha "+str(c-1)+" vezes")
