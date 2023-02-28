n = 1
c1 = 0
c2 = 0
c3 = 0
i = 1

while n > 0:
    n = int(input("Digite um número: "))
    if n >= 1 and n <=29:
        c1 = c1 + 1
    elif n >= 30 and n <=100:
        c2 = c2 + 1
    elif n <= 0 or n >100:
        c3 = c3 + 1
    i = i + 1
    if(i==11):
        break
print("A quantidade de números entre 1 à 29 é: ", c1, ". A quantidade de números entre 30 à 100 é: ", c2, ". A quantidade de números menor ou igual a 0 e maiores que 100 é: ", c3, ".")