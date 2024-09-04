time01 = input("Nome do time 01 : ")
time02 = input("Nome do time 02 : ")

gols01 = int(input(f"Quantos gols foram marcados pelo {time01} ? "))
gols02 = int(input(f"Quantos gols foram marcados pelo {time02} ? "))

if gols01 == gols02:
    print("EMPATE!")

else:
    if gols01 > gols02:
     print(f"{time01} é o VENCEDOR!")

    else:
     print(f" {time02} é o VENCEDOR!")

