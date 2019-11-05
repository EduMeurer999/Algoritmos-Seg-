def ex1():
    soma = 0
    for x in range(0,100):
        num = float(input('Informe um número: '))
        if num >=35 and num <=60:
            soma = soma+1
    print("QTD numeros entre 35 e 60: ",soma)

def ex2():
    qtdA = int(input('Informe o total de alunos na turma: '))
    media=0; qtdN_m_8 = 0; soma=0
    for x in range(0, qtdA):
        nota = float(input('Informe a nota do '+str(x+1)+"º aluno: "))
        soma = soma+nota
        if nota < 8.0:
            
            qtdN_m_8= qtdN_m_8+1
    print("Média geral: ", (soma/qtdA))
    print("QTD de notas < 8: ", qtdN_m_8)
# ex1()
ex2()
