# Escreva uma classe em Python que represente um voo. O voo possui no máximo 100 passageiros e a classe deve controlar a ocupação das vagas. Os dados do voo devem ser: o número do voo, o horário do voo (pode ser uma string) e uma forma para representar os assentos livres e ocupados (pode ser lista, string ou alguma outra estrutura). Faça ainda os seguintes métodos:
# getProximoAssento() – retorna o número do assento livre mais próximo, a partir do assento número 1;
# veficarAssento(numassento) – verifica se o número do assento recebido como parâmetro está ocupado, retorna um booleano;
# ocupar(numassento) – ocupa determinado assento do voo cujo número é recebido como parâmetro e retorna o resultado – se o assento ainda não estiver ocupado retorna verdadeiro indicando operação bem sucedida, caso contrário retorna falso;
# getVagas() – retorna o número de assentos vagos disponíveis (não ocupados) no voo;
# getVoo() – retorna o número do voo;
# getHoraVoo() – retorna a data do voo;
# getMapaAssentos() – retorna uma string representando todos os 100 assentos do avião. Os assentos ocupados deverão ser representados por ‘X’ e os livres por ‘-‘. Considere que os assentos estão disponibilizados em 4 fileiras com 25 assentos cada uma. No exemplo abaixo podemos verificar que o avião está com pouca lotação, somente 13 assentos estão ocupados e a fileira 4 está totalmente desocupada.
#---------------------------------------------------------------------------------
# Atividade 2 de Programação Orientada a Objeto
# Item 01/03
# Alexandre Fernandez - RA10482120706

import random
from sre_constants import CATEGORY_SPACE

class Voar():
    def __init__(self, numVoo: int, horarioVoo: str, assentoLouO:int):
        self.numVoo = numVoo
        self.horarioVoo = horarioVoo
        self.assentoLouO = assentoLouO



    def vooAtual(self):
        print('O voo atual é1', self.numVoo, 'no horário de ', self.horarioVoo, 'e o assento é o ', self.assentoLouO, '.')

    def geraAssentos(self):
        numassento = random.randint(0, 100)

    def assentosLivres(self):
        for l, c in enumerate(self.assentoLouO):
            if l > 0:
                return print('O lugar mais próximo é', l)

            



    # getProximoAssento(): retorna o número do assento livre mais próximo, a partir do assento número 1
    # veficarAssento(numassento): verifica se o número do assento recebido como parâmetro está ocupado, retorna um booleano;
    # ocupar(numassento): ocupa determinado assento do voo cujo número é recebido como parâmetro e retorna o resultado – se o assento ainda não estiver ocupado retorna verdadeiro indicando operação bem sucedida, caso contrário retorna falso;
    # getVagas() retorna o número de assentos vagos disponíveis (não ocupados) no voo;
    # getVoo() retorna o número do voo;
    # getHoraVoo() retorna a data do voo
    # getMapaAssentos() retorna uma string representando todos os 100 assentos do avião. Os assentos ocupados deverão ser representados por ‘X’ e os livres por ‘-‘. Considere que os assentos estão disponibilizados em 4 fileiras com 25 assentos cada uma. No exemplo abaixo podemos verificar que o avião está com pouca lotação, somente 13 assentos estão ocupados e a fileira 4 está totalmente desocupada.

print('---------')
primeiroVoo = Voar(numVoo=1247, horarioVoo='14:45', assentoLouO='Ocupado')
primeiroVoo.vooAtual()
primeiroVoo.geraAssentos()
primeiroVoo.assentosLivres()
print('---------')





# print('---------')
# proximoVoo = Voar(numVoo=1247, horarioVoo='14:45', assento='Livre 2')
# proximoVoo.vooProximo()





x e - procura o risco ou X e 
prof deixei o número ao invés dos "-" para referenciar a poltrona, deixei no exercício anotado ok.
get vagas   conta os x e diz os numeros de vagas 
get mapa de assento com a string
