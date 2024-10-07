nomes = [0]*5
tamanho = len(nomes)


for x in range(tamanho):
    nomes[x] = str(input("Digite seu nome : "))
print(f"Os nomes digitados foram nessa ordem : {nomes}")

for y in range(tamanho-1,-1,-1):
    print(nomes[y])

'''biblioteca'''
nomes.reverse()
print(nomes)