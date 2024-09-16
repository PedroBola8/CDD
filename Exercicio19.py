
quant = 0
quant2Fora = 0
for x in range(1,11):
    N1 = int(input("Digite um número :"))
    if N1 >=10 and N1 <=20:
        quant = quant + 1
        quant2 = 10 - quant
print(f"N° entre 10 e 20 : {quant} , N° que não estão entre 10 e 20 : {quant2Fora}")