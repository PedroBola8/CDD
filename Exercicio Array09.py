numeros = [0]*3
tamanho = len(numeros)

for x in range(tamanho):
    numeros[x] = int(input("Digite um N° : "))

for t in range(tamanho):
    if t %2==0:
        print()

print(f"Existem {x} N°s pares")

m=0
if m < numeros[0]:
    print(numeros[0])
elif numeros[0] < numeros[1]:
    print(numeros[1])
elif numeros[1] <  numeros[2]:
    print(numeros[2])




