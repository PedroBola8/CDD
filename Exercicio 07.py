nota = float(input("Digite Nota 1 : "))
nota02 = float(input("Digite Nota 2 : "))
nota03 = float(input("Digite Nota 03 : "))

soma = (nota + nota02 + nota03)

if soma >= 21:
    print("Aprovado!")

else:
    print("Reprovado!")

soma02 = (nota + nota02 + nota03)/3
print(soma02)

# Assim também funciona, mas da para fazer dessa forma4:



# Outro execicio!:

soma02 = (nota + nota02 + nota03)/3
print(soma02)

if soma02 >= 7:
    print("Aprovado!")

else:
    if soma02 >4 :
        print("Recuperação")

    else:

        print("Reprovado")



