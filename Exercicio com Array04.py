A = [0] *10
M = [0]*10
tamanho = len(A)
mult = 2

for y in range(tamanho):
    A[y]=int(input("Digite um N° : "))

x = int(input("Digite o valor de X : "))

for i in range(tamanho):
    M[i] =A[i]*x

print(A)
print(x)
print(M)