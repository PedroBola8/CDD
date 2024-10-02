num = [0]*10
tamanho = len(num)
cont = 0
num2 = 0

for x in range(tamanho):
    num[x]= int(input("Digite um N° : "))

num2 = int(input("Digite mais um N° : "))

for i in range(tamanho):
    if num2 == num[x]:
        cont +=1
print(cont)

