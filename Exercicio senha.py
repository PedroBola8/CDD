soma = 1

while soma <= 3:
    s = int(input("Digite sua senha : "))

    if s == 1917:
        print("Destravado! ")
        break

    print("Senha Incorreta, tente novamente ")
    soma = soma + 1

    if (soma == 4):
        print("Trancado")

