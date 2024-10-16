

try:
    a = []*4
    b = 0
    tamanho = len(a)
    contador = 0

    for x in range(tamanho):
        a[x] = int(input("Digite um N° "))
        contador+=1

    print(a[x])
    soma = contador + b
    print(soma)
    divisao = soma/b
    print(divisao)

except NameError:
    print("Não sei...")
except ZeroDivisionError:
    print("Não podemos dividir por zero")


