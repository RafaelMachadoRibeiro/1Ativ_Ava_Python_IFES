sexoF = 1
sexoM = 2
idade = 1
temp= 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
i = 0

while idade > 0:
    i = i + 1
    if(i==21):
        break
    
    idade = int(input("Digite a idade do "+str(i)+"º funcionário: "))
    sexo = int(input("Digite o sexo (1 para Mulher e 2 para Homem) do "+str(i)+"º funcionário: "))
    temp = int(input("Digite o tempo de serviço do "+str(i)+"º funcionário: "))

    if idade >= 60 and sexo == sexoF and temp < 25:
        c1 = c1 + 1
    elif idade >= 65 and sexo == sexoM and temp < 35:
        c2 = c2 + 1
    elif idade < 55 and sexo == sexoF and temp >= 30:
        c3 = c3 + 1
    elif idade < 60 and sexo == sexoM and temp >= 35:
        c4 = c4 + 1
    elif idade >= 60 and temp >= 35:
        c5 = c5 + 1
    else:
        c6 = c6 + 1

apo_id = c1 + c2
apo_te = c3 + c4

print(" ")
print("Funcionários que aposentaram por idade: ", apo_id)
print("Funcionários que aposentaram por tempo de serviço: ", apo_te)
print("Funcionários que aposentaram por idade e tempo de serviço: ", c5)
print("Funcionários que não poderão se aposentar: ", c6)