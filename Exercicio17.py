n1 = int(input("Quantos alunos tem na sala ? "))

soma = 0

for x in range(n1):
    n2 = float(input("Digite a nota :"))
    soma = soma + n2

soma2 = soma / n1
print(f"Média da sala : {soma2}")
