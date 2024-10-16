try:
    nome = [0]*2
    senha = ["0066"]
    tamanho = len(nome)


    for cadastro in range(tamanho):
        nome[cadastro]= str(input("Digite o usuario : "))
        senha[cadastro] = int(input("Digite sua senha : "))

    for login in range(tamanho):
        nome[login] = str(input("Digite seu usuario : "))

except IndexError:
    print("Deu erro boy")