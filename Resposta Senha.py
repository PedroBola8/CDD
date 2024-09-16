pin = 2213

senha = int(input("Digite a senha : "))
tentativas  = 1

while senha != pin or tentativas <3:
    senha = int(input("Senha Incorreta, tente novamente"))

tentativas = tentativas + 1

if tentativas == 3 and senha!=pin:
        print("Bloqueado")
else:
        print("Acesso liberado")

