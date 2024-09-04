hora1 = int(input("Digite a hora"))
min1 = int(input("Digite os minutos"))
hora2 = int(input("Digite a hora"))
min2 = int(input("Digite os minutos"))

soma = hora1 + hora2
soma2 = min1 + min2

somaminuto = soma2%60
somahora = soma%12
somahora2 = somahora + 1

if soma2 >= 60:
    print(f"{somahora2} h {somaminuto}")

else:
    print(f"{somahora} h {somaminuto}")









