
def gravar():
    with open("Nome.txt", "a") as arquivo:
        for x in range(2):
            arquivo.write(f"{x}\n")

def mostrar():
    with open("Nome.txt" , "r") as arquivo3:
        conteudo = arquivo3.read()
        print(conteudo)

