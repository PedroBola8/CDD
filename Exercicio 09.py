abasteceu =input("Qual combustivél será utilizado? \n "
                 "Digite G para gasolina e E para Etanol")
litro = float(input(f"Quantos de { abasteceu} você colocou ? "))



if abasteceu == "G" or abasteceu == "g":
    valor = litro * 5.8
    print(f"Total a pagar {valor}")

else:
    if abasteceu == "E" or abasteceu =="e":
        valor3 = litro * 4.9
        print(valor3)

    else:
        print("Inválido")



