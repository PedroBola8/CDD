hora1 = int(input("Digite a hora"))
min1 = int(input("Digite os minutos"))
hora2 = int(input("Digite a hora"))
min2 = int(input("Digite os minutos"))

if hora1 > 12:
    hora1 = hora1 - 12
if hora2 > 12:
    hora2 = hora2 - 12


somahora = hora1 + hora2
somaminuto = min1 + min2

if somaminuto >= 60:
    somaminuto = somaminuto - 60
    somahora =  somahora + 1


if somahora >12:
    somahora = somahora - 12

print(f"{somahora} h {somaminuto :02d} ")


