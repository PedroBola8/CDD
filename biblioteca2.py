def somar(n1,n2,n3,n4,n5):
    soma = n1+n2+n3+n4+n5
    print(soma)

def soma (*numero):
    print(numero)
    for i in numero:
        res = res + x
    print(res)

def vogais (texto):

    '''
    cont=0
    for x in texto:
        if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cont = cont +1
    print(f"Letras maiusculas : {cont}")'''


    cont2=0
    for i in texto:
        if i not in " ":
            cont2= cont2+1
    print(f"Letras minusculas : {cont2}")
    tamanho = len(texto)
    for t in range(tamanho-1, -1, -1):
        print(texto[t], end=" ")


somar = [0]*5
tam = len(somar)
soma = 0

for x in range(tam):
    somar[x] = int(input("Digite um N° : "))


print(somar)