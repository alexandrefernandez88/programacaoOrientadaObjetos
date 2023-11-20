# Atividade 3 de Programação Orientada a Objeto
# Alexandre Fernandez - RA10482120706
#---------------------------------------------------------------------------------
#AgenciaBancaria
#contas : Conta[]
#codigo : int
#-------
#+ addConta(conta : Conta) : void
#+ getConta(numero : int) : Conta
#+ listContas() : string
#-------
from Atividade3_POO_classConta import Conta

class AgenciaBancaria:
    # quantidadeContas = 0

    def __init__(self, codigo):
        self.__codigo = codigo
        self.__contas = []
        # AgenciaBancaria.quantidadeContas += 1

    def addConta(self, contaObj):
        self.__contas.append(contaObj)

    def getConta(self, numero):
        for conta in self.__contas:
            if conta.getNumero()==numero:
                return conta
        return None

    def listContas(self):
        strContas = ''
        for conta in self.__contas:
            strContas += conta.getTitular()+' Saldo R$'+str(conta.getSaldo())+'\n'
        return strContas

#-------FIM


# Professor, fiz os métodos abaixo para entender melhor cada ponto... não apaguei mas deixei comentado ok.
#     def setCodigo(self, codigo):
#         if codigo == str:
#             self.__codigo = codigo

#     def getCodigo(self):
#         return self.__codigo

#     def setConta(self, conta):
#         if conta == str:
#             self.__conta = conta

#     def getConta(self):
#         return self.__conta

# class ContarContas(AgenciaBancaria):
#     def addConta(self, conta:AgenciaBancaria):
#         self.__contas.append(conta)

#     def getContas(self):
#         return self.__contas


# correntista01 = AgenciaBancaria('123456', '001')
# print(correntista01.getConta(),'-', correntista01.getCodigo())
# correntista02 = AgenciaBancaria('654321', '001')
# print(correntista02.getConta(),'-', correntista02.getCodigo())
# correntista03 = AgenciaBancaria('121212', '001')
# print(correntista03.getConta(),'-', correntista03.getCodigo())
# print('Quantidade contas:', AgenciaBancaria.quantidadeContas)