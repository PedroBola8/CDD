from itertools import filterfalse


class pessoa:

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comer = False
        self.falar = False
        self.dormir = False


    def falar(self):

        if self.falar == False:
            if self.comer == False:
                if self.dormir == False:
                    print(f"{self.nome} está falando ")
                    self.falar=True
                else:
                    print(f"{self.nome} não pode falar pois está dormindo")
            else:
                print(f"{self.nome} não pode falar pois está comendo")
        else:
            print(f"{self.nome} não pode falar pois já está falando")

    def comer(self):
        if self.comer == False:
            if self.falar == False:
                if self.dormir == False:
                    print(f"{self.nome} está comendo ")
                    self.comer=True
                else:
                    print(f"{self.nome} não pode falar pois está falando")
            else:
                print(f"{self.nome} não pode falar pois está dormindo")
        else:
            print(f"{self.nome} não pode falar pois está comendo")

    def dormir(self):
        if self.dormir == False:
            if self.comer == False:
                if self.falar == False:
                    print(f"{self.nome} está falando ")
                    self.dormir = True
                else:
                    print(f"{self.nome} não pode falar pois está dormindo")
            else:
                print(f"{self.nome} não pode falar pois está comendo")
        else:
            print(f"{self.nome} não pode falar pois está falando")
        print(f"{self.nome} foi dormir ")





class animal:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f" O {self.nome} foi comer")


class gato(animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O {self.nome} foi miar...")


class vaca(animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def rugir(self):
        print(f"O {self.nome} fez MOOOOHHHHH...")

class cachorro(animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def late(self):
        print(f" O {self.nome} está latindo...")

class porquinhodaIndia(animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def arrulho(self):
        print(f"O {self.nome} faz Cui,cuii...")






