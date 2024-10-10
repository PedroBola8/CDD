class pessoa:

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso


    def falar(self):
        print(f"{self.nome} foi falar ")

    def comer(self):
        print(f"{self.nome} foi comer ")

    def dormir(self):
        print(f"{self.nome} foi dormir ")

        

class acoes:

    def __init__(self, falar, comer, dormir):
        self.falar = falar
        self.comer = comer
        self.dormir = dormir
