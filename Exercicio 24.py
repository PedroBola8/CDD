
nome = str(input("Digite o nome do estudante : "))
n1 = float(input("Digite a nota 01 : "))


while n1 <0 or n1 >10 :
    n1 = float(input("Digite a nota 01 novamente : "))


n2 = float(input("Digite a nota 02 : "))

while n2 <0 or n2 >10 :
    n2 = float(input("Digite a nota 02 novamente : "))
soma = n1 + n2
media = soma / 2

print(f"Média final de {nome} é {media}")










