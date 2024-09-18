peso = float(input("Digite seu peso : "))
altura= float(input("Digite sua altura : "))

imc = peso / (altura)**2

if imc <= 16.5:
        print(f"Imc abaixo do peso : {imc}")

elif imc >= 16.6 and imc <= 24.9:
    print(f"Imc com peso ideal, Parabéns : {imc}")

elif imc >=25.0 and imc <= 29.9:
    print(f"Levimente acima do peso : {imc}")

elif imc >=30.0 and imc <= 34.9:
    print(f"Obesidade grau I : {imc}")

elif imc >=35.0 and imc <= 39.9:
    print(f"Obesidade grau II : {imc}")

elif imc >=40:
    print(f"Obesidade grau III : {imc}")



