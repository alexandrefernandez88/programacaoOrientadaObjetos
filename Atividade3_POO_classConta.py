# Atividade 3 de Programação Orientada a Objeto
# Alexandre Fernandez - RA10482120706
#---------------------------------------------------------------------------------
#Conta
#numero : int
#titular : string
#saldo : double
#-------
#+ depositar(valor : double) : void
#+ retirar(valor : double) : double
#-------
class Conta:
    def __init__(self, numero, titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0

    def getNumero(self):
        return self.__numero
	
    def getTitular(self):
        return self.__titular

    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Use outro método.')

    def retirar(self, valor):
        if valor <= self.getSaldo():
            self.__saldo -= valor
        else:
            print('Erro no saque, verifique seu saldo.')



# Professor, fiz os métodos abaixo para entender melhor cada ponto... não apaguei mas deixei comentado ok.


# correntista01 = Conta(123456, 'Alexandre Fernandez', 0)
# print('Titular',correntista01.get_titular())
# print('Número da Conta',correntista01.get_numero())
# print('Seu saldo é de R$',correntista01.get_saldo())
# correntista01.depositar(1000)
# print('Você recebeu um depósito de R$',correntista01.get_saldo())
# correntista01.retirar(150)
# print('Seu saldo é de R$',correntista01.get_saldo())