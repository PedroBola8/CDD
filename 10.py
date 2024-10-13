
num = []
sem = []


for x in range(5):
    N = int(input("Digite um número: "))
    num.append(N)
    '''append serve para add elementos num array/lista'''

for i in num:
    if i not in sem:
        sem.append(i)
'''novamente usando a função append(add), vamos colocar os N°´s dentro de uma nova lista\n
sem não repeti-los, então atraves do for pegamos a lista anterior com od dados fornecidos pelo user e \n
criamos uma condicional, se o N° tal da lista A NÃO estiver na lista B, adicioneo a lista, se estiver,\n
passa pro próx'''

print("Lista original:", num)
print("Lista sem duplicatas:", sem)