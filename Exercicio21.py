opcao = 1

while opcao !=2:
    num = 0
    soma = 0
    nome = int(input("Quantos alunos a na sala ? "))

    while num < nome:
        n1 = float(input("Digite a Nota : "))
        soma = soma + n1
        num = num + 1

    soma2= soma / nome
    print(f"Média final da turma: {soma2}")

    opcao = int(input("Digite (1) para recomeçar \n"
                      " e (2) para encerrar!"))
