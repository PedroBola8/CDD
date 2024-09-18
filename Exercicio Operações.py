opcao = 1
while opcao !=2:

    n1 = int(input("Digite o 1° N : "))
    n2 = int(input("Digite o 2° N : "))

    op = int(input("Digite a operação que deseja realizar \n"
                   "1 para adição\n"
                   "2 para subtração \n"
                   "3 para multiplicão\n"
                   "4 para divisão"))

    if op == 1 :
        valor = n1 + n2
        print(valor)

    elif op == 2:
        valor2 =n1 - n2
        print(valor2)

    elif op == 3:
        valor3 = n1 * n2
        print(valor3)

    elif op == 4:
        valor4 = n1 / n2
        print(valor4)



    opcao = int(input("Digite 1 para recomeçar \n"
                      "ou 2 para encerrar!"))