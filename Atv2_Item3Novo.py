# Atividade 2 de Programação Orientada a Objeto
# Item 01/03
# Alexandre Fernandez - RA10482120706

import random
from sre_constants import CATEGORY_SPACE

class Voo():
    def __init__(self, numVoo: int, horarioVoo: str, assentoLouO:str):
        self.numVoo = numVoo
        self.horarioVoo = horarioVoo
        self.assentoLouO = assentoLouO
        self.geraAssentos()



    def vooAtual(self):
        print('O voo atual é1', self.numVoo, 'no horário de ', self.horarioVoo, 'e o assento é o ', self.assentoLouO, '.')



    def assentoLouO(self):
        for l, c in enumerate(self.assentoLouO):
            if l > 0:
                return print('O lugar mais próximo é', l)


    def getVagas(self):
        contador = 0
        for i in self.assentoLouO:
            if i == 0:
                contador+=1
        return print(contador, 'lugares livres')









    def veficarAssento(self,numAssento):
        if self.assentoLouO[numAssento]==0:
            return True
        else:
            return False
print(primeiroVoo.verificarAssentoLivre(45))
primeiroVoo = primeiroVoo(1234, '22:30')
    for i in range(50):
        numero = random.randint(1,100)
        primeiroVoo.ocuparAssento(numero,flag=0)

    def getMapaAssentos(self):
        print('X',self.assentoLouO[1:100])
        
    def getVoo(self):
        print('O número do voo é ', self.numVoo)

    def getHoraVoo(self):
        print('O horário do voo é ', self.horarioVoo)



print('---------')
primeiroVoo = Voo(numVoo=1247, horarioVoo='14:45', assentoLouO='Ocupado')
primeiroVoo.vooAtual()
primeiroVoo.geraAssentos()
# primeiroVoo.assentoLouO()
print('---------')

primeiroVoo.getMapaAssentos()
primeiroVoo.getVagas()
print(primeiroVoo.verificarAssentoLivre(45))
primeiroVoo.getVoo()
primeiroVoo.getHoraVoo()
primeiroVoo.getProximoAssento()
primeiroVoo.ocuparAssento(3)
primeiroVoo.getMapaAssentos()