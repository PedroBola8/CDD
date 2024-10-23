nomes = ["Pedro", "Talita" , "Augusto"]
senhas = ["123","1234","12345"]
tamanho = len(nomes)

'''cadastro'''
for x in range(1):
    nome1 = str(input("Digite seu nome : "))
    senha1 = int(input("Digite sua senha : "))
'''login'''
if nome1 == nomes[0]:
        print("Olá Pedro!")
        if senha1 == senhas[0]:
            print("Acesso Liberado")
        elif senha1 != senhas[0]:
            print("Acesso Negado")

    elif nome1 == nomes[1]:
            print("Olá Talita")
            for y in range(1):
                senha1 = int(input("Digite sua senha : "))
                if senha1 == senhas[1]:
                    print("Acesso liberado Talita!")
                else:
                    print("Acesso Negado")

    elif nome1 == nomes[2]:
            print("Olá Augusto")
            for t in range(1):
                senha1 = int(input("Digite sua senha : "))
                if senha1 == senhas[2]:
                    print("Acesso Liberado Augusto")
                else:
                    print("Acesso negado")
    else:
        print("Nome Inválido")
