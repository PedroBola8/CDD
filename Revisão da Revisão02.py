
'''n1 = int(input("Digite um N° : "))

while n1 > 1:
    if n1 %2==0:
        print(n1, end=" ")
    n1-=1


print(".\n"
          "\n"
          ".")

for x in range(10,1,-1):
    print(x)'''


soma=0
for e in range(1,12):
    soma = soma + e
print(soma)


n1 = int(input("Digite um N° :"))

for x in range(1,11):
    mult = n1 * x
    print(f" {n1} X {x} = {mult}")




n2 = int(input("Digite um N°: "))

while n2!=0:
    if n2%2!=0:
        print(n2)
    n2-=1


opcao = 1
while opcao!=2:
    '''pedi um N° ao usuario'''
    n3 = int(input("Digite um N° : "))
    '''usando a função for posso resolver a questão aplicando a regra (inicio , final, de quanto em quanto)\n
     e para contornar o erro do for com o ultimo N°, é só add um +1 na tag final \n
      Obs: parta inverter os N° no for, basta colocar o -1 na tag de quanto em quanto'''
    for i in  range (1,n3 + 1 ,1):
        soma = n3 + i
        print( i )
    print(f"A soma dos N° anteriores é {soma}")
    '''o print nesse caso sempre remete ao for'''

    opcao=int(input("Digite 1 para recomeçar \n"
                    "2 para encerrar : "))




