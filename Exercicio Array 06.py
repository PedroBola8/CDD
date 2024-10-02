nome = [0]*5
senha = [0]*5
tamanho = len(nome)

for x in range(tamanho):
    nome[x]= str(input("Digite seu nome : "))
    senha[x] = int(input("Digite sua senha : "))


for x in range(5):
    print(f"{x}: nome: {nome[x]}, senha: {senha[x]}")


