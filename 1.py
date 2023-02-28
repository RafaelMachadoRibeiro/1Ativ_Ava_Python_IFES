#Entrada de dados dos usuários
nome = str(input("Digite o nome do aluno(a): "))
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))

#Calculos matemáticos
med3 = (nota1 + nota2 + nota3)/3

#Condição
if (med3 >= 70):
    print(nome, "foi aprovado no primeiro trimestre sem precisar de realizar a 4º prova, pois sua média foi:", med3)

else:
    print(nome, "deverá realizar a 4º avaliação pois sua média é: ", med3)
    nota4 = float(input("Digite a nota do 4º bimestre: "))
    med4 = (nota1 + nota2 + nota3 + nota4)/4
    if(med4 >= 70):
        print(nome, "foi aprovado pois sua média é: ", med4)
    elif(med4 >= 50):
        print(nome, "ficou de recuperação pois sua média é: ", med4)
    else:
        print(nome, "ficou de reprovado pois sua média é: ", med4)