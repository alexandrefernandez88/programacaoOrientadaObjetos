# Atividade 4 de Programação Orientada a Objeto
# Alexandre Fernandez - RA10482120706
# Hugo Botter Zarpelão - RA10482120760



from abc import ABC
import abc

class Contribuinte(ABC):
    def __init__(self, nome, documento, rendaBruta):
        self.__nome = nome
        self.__documento = documento #(CPF ou CNPJ)
        self.__rendaBruta = rendaBruta
        self.__contribuintes = []

    def getNome(self):
        return self.__nome

    def getDocumento(self):
        return self.__documento

    @abc.abstractmethod
    def getRendaBruta(self):
        pass

    def addContribuinte(self, contriObj):
        self.__contribuintes.append(contriObj)

    def listaContribuintes(self):
        strContribuintes = ''
        for contribuinte in self.__contribuintes:
            strContribuintes += contribuinte.getNome() +' '+ contribuinte.getDocumento() + ' ' + contribuinte.getRendaBruta() + '\n'
        return strContribuintes

    @abc.abstractmethod
    def calcImposto(self, rendaBruta):
        pass

class TotalImposto():
    def getTotalImposto(self):
        return


# . getTotalImposto(), que retorna a quantidade total de imposto devido (somatório do imposto devido por 
# cada contribuinte)
#--->>>>> fazer um for da lista dos contribuintes e somar



# . getPorcentagemContribuintesFeminino(), que retorna a porcentagem de contribuintes do sexo feminino 
# mantidas na coleção.
# --->>>> precisa fazer um for p/ percorrer e verificar se é CPF ou CNPJ. Se for CPF contar e atribuir mais um contador se for feminino.