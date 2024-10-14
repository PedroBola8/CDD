class Atleta():

    def __init__(self, nome,aposentado, peso):
        self.nome = nome
        self.aposentado = aposentado
        self.peso = peso
        self.aquecer = False
        self.falar = False

class nelson():
    def __init__(self,nome,peso, aposentado):
        self.nome = nome
        self.peso = peso
        self.aposentado = aposentado

    def corredor(self):
        print(f" O {self.nome} foi correr...")

class geh():

    def __init__(self, nome, peso, aposentado):
        self.nome = nome
        self.peso = peso
        self.aposentado = aposentado

    def ciclista(self):
        print(f"O {self.nome} foi pedalar...")

class Mil():
    def __init__(self, nome, peso, aposentado):
        self.nome = nome
        self.peso = peso
        self.aposentado = aposentado

    def nadador(self):
        print(f"{self.nome} foi nadar...")


def corredor(self):
    if self.peso == False:
        if self.aquecer== True:
            print(f"{self.nome} está se exercitando ")
        else:
            print(f"{self.nome} não aqueceu, por isso irá se aposentar")
    else:
        print(f"{self.nome} está acima do peso")



def ciclista(self):
    if self.aquecer == False:
        if self.peso == True:
            print(f"{self.nome} Está se exercitando")
            self.aquecer = True
        else:
            print(f"{self.nome} não pode se exercitar pois está acima do peso")
    else:
        print(f"{self.nome} não começoua se exercitar pois ainda não se aqueceu")

def nadador(self):
    if self.aquecer == False:
        if self.peso == False:
            print(f"{self.nome} Está se exercitando")
            self.aquecer = True
        else:
            print(f"{self.nome} não pode se exercitar pois está acima do peso")
    else:
        print(f"{self.nome} não começoua se exercitar pois ainda não se aqueceu")


class Triatleta(corredor,nadador,ciclista):
    def __init__(self,nome,peso,aposentado):
        super().__init__(nome,peso,aposentado)






'''certo'''


