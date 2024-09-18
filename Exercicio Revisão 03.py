
resp = "Sim" or "sim" or "SIM"

while resp != "NÃO" or "Não" or "não":

    n1 = int(input("Digite um N° :"))
    n2 = int(input("Digite um N° :"))

    if n1 == n2:
        soma = n1 + n2
        c = soma

    else:
        mult = n1 *  n2
        c = mult
    print(c)

    resp = str(input("Digite : Sim para recomeçar e\n"
                     " : Não para parar"))