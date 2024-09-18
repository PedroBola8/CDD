n1 = int(input("Digite um N° : "))

if n1%2 == 0:
    print(f"N° digitado é par :{n1}")
    if n1 > 0:
        print("positivo")
    else:
        print("negativo")

else:
    print(f"N° digitado é ímpar :{n1} ")

    if n1 < 0:
        print("negativo")
    else:
        print("positivo")
