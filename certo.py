numeros = [0]*10
tamanho = len(numeros)

for x in range(tamanho):
    numeros[x]= int(input("Digite um N° :"))

m = 0
menor=0
soma=0
for i in range(tamanho):
    if numeros[i]%2==0:
        print(numeros[i])

    if numeros[i]>m:
        m = numeros[i]

    if numeros[i] < m:
        menor = numeros[i]

    soma = soma + numeros[i]
media = soma/tamanho

cont=0
for t in range(tamanho):
    if numeros[t]>media:
        cont+=1
print(f"N°´s acima da média {cont}")
print(f"Maior = {m}")
print(f"Menor = {menor}")



numeros = [0]*10
tamanho = len(numeros)

for x in range(tamanho):
    numeros[x]= int(input("Digite um N° :"))

m = 0
menor=0
soma=0
for i in range(tamanho):
    if numeros[i]%2==0:
        print(numeros[i])

    if numeros[i]>m:
        m = numeros[i]

    if numeros[i] < m:
        menor = numeros[i]

    soma = soma + numeros[i]
media = soma/tamanho

cont=0
for t in range(tamanho):
    if numeros[t]>media:
        cont+=1
print(f"N°´s acima da média {cont}")
print(f"Maior = {m}")
print(f"Menor = {menor}")