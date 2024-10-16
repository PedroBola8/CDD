from bibliotecaM3 import *

while True:
    print("\n--- Menu ---")
    print("1. Gravar")
    print("2. Mostra")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        t = input("Digite um texto : ")
        gravar()
    elif opcao == "2":
        mostrar()
    elif opcao == "3":
        print("saindo...")
        break
    else:
        print("Valor Inválido")


    match opcao:
        case 1:
            t = input("Digite um texto : ")
            gravar(t)
        case 2:
            mostrar(t)
        case 3:
            break
