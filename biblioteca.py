from array import array

N = int(input("Digite um N° : "))

def tampa (N):
    for x in range(1,N+1):
        for i in range(1,x+1):
            print(x, end=" ")
        print()

N = int(input("Digite um N° : "))

def tempa (N):
    for x in range(1,N+1,1):
        for i in range(1,x+1):
            print(i, end=" ")
        print()



def vogais (texto):

    cont=0
    for x in texto:
        if x in "aeiou":
            cont = cont +1
    print(cont)


