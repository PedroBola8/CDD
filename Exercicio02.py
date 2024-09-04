nome = input("Nome do aluno (a)? : ")
numbers = float(input("Digite nota01 N°:"))
numbers2 = float(input("Digite nota02 N°:"))


'''
Outra maneira é: 

números = (numbers, numbers2)
soma = sum(números)
media = soma / len(números)
print("Nome: ", nome)
print("A média de notas é:", media)


'''


media02 = ( (numbers + numbers2) / 2)
print(f"Olá aluno {nome} sua media foi {media02} ")
