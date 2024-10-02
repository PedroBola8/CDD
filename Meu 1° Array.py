nomes = ["Talita", "Eduarda" , "Milenna", "Bruno", "Pedro"]
for i in nomes:
    print(i)


nomes2 = []
for x in range (5):
    nome = str(input("Digite um nome : "))
    nomes2.append(nome)
print(nomes2)


"""OU"""


no = ["", "","", "",""]
tamanho = len(no)
for i in range(tamanho):
    no[i]=input("Digite o nome : ")

print(no, end= " ")

print()
for z in range(tamanho):
    print(no[z], end=" ")