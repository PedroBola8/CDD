

''' for = para, para algo'''
for a in range (125 , 0 ,-2):
    ''' estrutura for ( inicio, final, de quanto em quanto)'''
    if a > 0:
        ''' meior que '''
        print(f" Os números são positivos {a}")



'''while'''

n1 = int(input("Digite um N° : "))
''' recebo um N° e dele vou puxar o while'''

while n1 > 1:
    ''' enquanto o valor digitado for maior que 1, o código repete'''
    if n1%2==0:
        print(n1 , end=" ")
    n1-=1



print(".\n"
      "\n"
      "\n"
      "\n"
      ".\n")
'''Gaby e Matheus'''


a = float(input("Digite sua nota : "))
'''float trabalha N° decimais, ex: 8,1425;'''
b = float(input("Digite sua nota :"))

soma = a + b
media = soma /2
print(f"Média final {media}")

print("\n"
      "\n"
      "\n"
      "\n"
      "\n")


'''Repetição'''

retorna = "Sim" and "SIM" and "sim"

while retorna != "Não" and retorna != "NÃO" and retorna != "não" and retorna != "nao" and retorna != "NAO":
    a = float(input("Digite sua nota : "))

    b = float(input("Digite sua nota :"))

    soma = a + b
    media = soma / 2
    print(f"Média final {media}")

    retorna = str(input("Digite sim repetir e \n"
                        "não para encerrar : "))


