opcao = 1

while opcao !=2:

    n1 = int(input("Digite um N° :"))
    n2 = int(input("Digite outro N° :"))

    if n2 ==0:
        print("Inválido")
        opcao = int(input("Digite (1) para recomeçar \n"
                          " e (2) para encerrar!"))
    else:
        opcao = int(input("Digite (1) para recomeçar \n"
                          " e (2) para encerrar!"))
        divisao = n1 / n2
        print(f"O resultado da divisão foi {divisao}")





