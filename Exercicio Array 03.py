notas = [0.0] *5

tamanho = len(notas)
soma = 0
contador = 0

for x in range(tamanho):
    notas[x]=float(input("Digite a nota : "))

for i in range(tamanho):
    soma = soma + notas[i]

media = soma / tamanho


for y in range(tamanho):
    if notas[y] > media:
        contador = contador + 1

print(f"Existem {contador} dentro da média da sala que é {media}")


