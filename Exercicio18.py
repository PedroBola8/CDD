N1 = int(input("Digite um número :"))
soma = 0
quant = 0
for x in range(1,10):
    N1 = int(input("Digite um número :"))
    if N1 < 0:
        soma = N1 + soma
        quant = quant + 1
print(f"Quantidade de N° negativos : {quant} , soma desses números : {soma}")