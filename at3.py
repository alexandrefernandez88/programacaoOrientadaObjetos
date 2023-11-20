import random

class Voo():
    def __init__(self, numVoo: int, horarioVoo: str, assentoVO:str):
        self.numVoo = numVoo
        self.horarioVoo = horarioVoo
        self.assentoVO = assentoVO

    def verificarAssento(self,numAssento):
        if self.assentoVO[numAssento]==0:
            return True
        else:
            return False

    def ocuparAssento(self, numAssento, flag=0):
        if self.assentoVO[numAssento] == 0:
            self.assentoVO[numAssento]=1
            if flag == 0:
                print('Assento ', numAssento, 'ocupado.')
        else:
            if flag == 0:
                print('tente o próximo')


    def geraAssento(self):
        numAssento = random.randint(0, 100)


primeiroVoo = Voo(numVoo=1247, horarioVoo='14:45', assentoVO='Ocupado')
print('----verificarAssento----')
primeiroVoo.verificarAssento(45)
print('----ocuparAssento----')
primeiroVoo.ocuparAssento(45)
primeiroVoo.geraAssento()

# print('----getProximoAssento----')





# primeiroVoo.getProximoAssento()
# print('----veficarAssento----')
# primeiroVoo.verificarAssento(45)
#     def getProximoAssento(self):
#         for l, c in enumerate(self.assentoVO):
#             if l == 0:
#                 return print('O assento liberado é ', c)
