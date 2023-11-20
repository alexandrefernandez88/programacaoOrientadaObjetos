# Atividade 2 de Programação Orientada a Objeto
# Item 01/03
# Alexandre Fernandez - RA10482120706

import random

class Voar():
    def __init__(self, numVoo: int, horarioVoo: str, assentoLouO:None):
        self.numVoo = numVoo
        self.horarioVoo = horarioVoo
        self.assentoLouO = assentoLouO
        self.geraAssentos()



    def vooAtual(self):
        print('O voo atual é1', self.numVoo, 'no horário de ', self.horarioVoo, 'e o assento é o ', self.assentoLouO, '.')

    def geraAssentos(self):
        assentoLouO = random.randint(0, 100)

    def assentosLivres(self):
        for l, c in enumerate(self.assentoLouO):
            if l > 0:
                return print('O lugar mais próximo é2 nº', l)

    def getVoo(self):
        print('O voo atual é3', self.numVoo)

    def getHoraVoo(self):
        print('O horário do voo é4', self.horarioVoo)

#---------------------------------------
    def getProximoAssento(self):
        for assento, fileira in enumerate(self.assentoLouO): 
            if fileira == 0:
                return print('O lugar mais próximo é5 o ', assento)
#---------------------------------------
    def veficarAssento(self,numassento):
        if self.veficarAssento[numassento] == 0:
            return True
        else:
            return False
#---------------------------------------
    def ocupar(self, numassento, flag=None):
        if self.assentoLouO[numassento] == 0:
            if flag == None:
                print('Assento Livre', numassento)
        else:
            if flag == None:
                print('Assento Ocupado', numassento)

for i in range(30):
    numero = random.randint(0,99)
    
    def getVagas(self, assentoLouO):
        quantificar = assentoLouO
        for assento in self.assentoLouO:
            assento += 1
            return print('Há ', quantificar, ' lugares desocupados')



    def getMapaAssentos(self, assentoLivres):
        print('X', self.assentosLivres[0:100])
        



print('---------')
primeiroVoo = Voar(numVoo=1247, horarioVoo='14:45', assentoLouO='Ocupado')
primeiroVoo.vooAtual()
print('---------')
primeiroVoo.geraAssentos()
primeiroVoo.assentosLivres()
print('---------')
primeiroVoo.getVoo()
print('---------')
primeiroVoo.getHoraVoo()
print('---------')
#---------------------------------------
primeiroVoo.getProximoAssento()
print('---------')
#---------------------------------------

print('---------')
#---------------------------------------
primeiroVoo.ocupar(5)
print('---------')
# primeiroVoo.getMapaAssentos()
print(getMapaAssentos)