soma = 1

while soma <= 3:
    n1 = int(input("Digite sua senha : "))

    if n1 == 2515:
        print("Acesso liberado")
        break

    print("Senha Incorreta, tente novamente")
    soma =soma + 1

    if (soma == 4):
        print("Deu Zebra")

