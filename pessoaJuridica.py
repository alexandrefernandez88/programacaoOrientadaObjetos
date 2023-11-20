# Atividade 4 de Programação Orientada a Objeto
# Alexandre Fernandez - RA10482120706





from contribuinte import Contribuinte


class PessoaJuridica(Contribuinte):
    def __init__(self, nome, documento, rendaBruta, ano_fundacao):
        super().__init__(nome, documento, rendaBruta)
        self.__ano_fundacao = ano_fundacao

    def calcImposto(self, rendaBruta):
        return rendaBruta * 0.10