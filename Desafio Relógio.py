hora1 = int(input("Digite a hora"))
min1 = int(input("Digite os minutos"))
hora2 = int(input("Digite a hora"))
min2 = int(input("Digite os minutos"))

soma = hora1 + hora2
soma2 = min1 + min2

soma3 = soma2 >= 60
somahora = soma + 1
somaminuto = soma2 - 60
alteracao = somahora - 12

if somahora <= 24:
    trocar =  somahora - 12
    print(f"{trocar} h {somaminuto}")
else:
        if somahora > 24:
            alteracao = somahora - 24
            print(f"{alteracao}h {somaminuto}")

        else:
            print("Fudeu")
