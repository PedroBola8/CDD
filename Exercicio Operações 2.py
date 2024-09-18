opcao = 1
while opcao !=2:

    n1 = int(input("Digite o 1° N : "))
    n2 = int(input("Digite o 2° N : "))

    op = int(input("Digite a operação que deseja realizar \n"
                   "1 para adição\n"
                   "2 para subtração \n"
                   "3 para multiplicão\n"
                   "4 para divisão : "))

    if op == 1 :
        valor = n1 + n2
        print(f"Resultado da soma entre {n1} e {n2} é  = {valor}")

    elif op == 2:
        valor2 =n1 - n2
        print(f"Resultado subtração entre {n1} e {n2} é = {valor2}")

    elif op == 3:
        valor3 = n1 * n2
        print(f"Resultado da multiplicão entre {n1} e {n2} é = {valor3}")

    elif op == 4:
        valor4 = n1 / n2
        print(f" Resultado da divisão entre {n1} e {n2} é  = {valor4}")

    elif op !=1 or op !=2 or op !=3 or op !=4:
        print("Escolha de operação inválida, tente novamente")


    opcao = int(input("Digite 1 para recomeçar \n"
                      "ou 2 para encerrar!"))