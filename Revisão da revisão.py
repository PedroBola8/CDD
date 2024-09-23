'''
nome = str(input("Digite seu nome : "))
idade = int(input("Digite sua idade : "))
salario = float(input("Digite seu salário : "))

print(nome , idade , salario)'''
from Doidera import retorna

'''
print(",\n"
      "\n"
      "\n"
      "\n"
      "\n"
      ".")'''

'''Pede um N° e impreme de 1 até ele'''

'''
n1 = int(input("Digite um número : "))

for x in range (1,n1+1,1):
    print(x)
    '''


'''alunos = int(input("Digite o número de alunos: "))
soma = 0

# Solicita as notas dos alunos
for x in range(1, alunos + 1):
    nota = float(input(f"Digite a nota do aluno {x}: "))
    soma= soma + nota

media = soma / alunos
print(f"A média aritmética da turma é: {media:.2f}")'''

'''som = 0
alu = int(input("Digite quantos alunos a na sala : "))

for x in range (1,alu+1,1):
    nt = float(input("Digite a nota : "))
    som = som + nt

media = som/alu
print(media)'''

'''soma = 0
n1 = int(input("Digite um N° inteiro ou 0 para encerrar : "))
while n1 > 1:
    n2 = int(input("Digite um N° : "))
    if n2 ==0 :
        break
    soma = + n1 + n2

print(soma)'''



'''n1 = int(input("Digite um N° : "))
n2 = int(input("Digite outro N° : "))

if n1 > n2:
    print(f" {n1} , {n2}")
else:
    print(f" {n2} , {n1}")

'''

"""opcao = 1
while opcao !=2:

    nome = str(input("Digite o nome do estudante : "))
    nota1 = float(input("Digite a nota : "))
    nota2 = float(input("Digite a nota : "))
    nota3 = float(input("Digite a nota : "))


    media = (nota1+nota2+nota3)/3

    if media >= 7:
        print(f"O estudante {nome} foi  Aprovado! por média {media}")

    elif media <= 6.9 and media > 4:
        print(f"O estudante {nome} está em Recuperação! {media }")

    else:
        print(f"O estudante {nome} foi  Reprovado! por média {media}!")

    opcao = int(input("Digite 1 para recomeçar \n"
                      "2 para encerrar : "))
"""

retorno = "Sim" and "sim" and "SIM"
while retorno!= "Não" and retorno !="NÂO" and retorno!="não" and retorno!="nao" and retorno!="Não" and retorno!= "Nao":
    time1 = str(input("Digite o nome do time da casa : "))
    time2= str(input("Digite o nome do time Visitante : "))

    gols1 = int(input("Digite o N° de gols feitos pelo time da Casa ; "))
    gols2 = int(input("Digite o N° de gols feitos pelo time Visitante ; "))


    if gols1 > gols2:
        print(f"O Vencedor é {time1} com {gols1} gols")
    elif gols1==gols2:
        print(f"Empate!")
    else:
        print(f"O vencedor é {time2} com {gols2} gols")

    retorno = str(input("Digite Sim para recomeçar \n"
                        "Não para encerrar : "))