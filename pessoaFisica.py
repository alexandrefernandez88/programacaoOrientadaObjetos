# Atividade 4 de Programação Orientada a Objeto
# Alexandre Fernandez - RA10482120706
# Hugo Botter Zarpelão - RA10482120760



from contribuinte import Contribuinte


class PessoaFisica(Contribuinte):
    def __init__(self, nome, documento, rendaBruta, sexo):
        super().__init__(nome, documento, rendaBruta)
        self.__sexo = sexo

    def calcImposto(self, rendaBruta):
        if rendaBruta <= 1400.00:
            return 0
        elif rendaBruta >= 1400.01 and rendaBruta <= 2100.00:
            return rendaBruta * 0.10 - 100
        elif rendaBruta >= 2100.01 and rendaBruta <= 2800.00:
            return rendaBruta * 0.15 - 270
        elif rendaBruta >= 2800.01 and rendaBruta <= 3600.00:
            return rendaBruta * 0.25 - 500
        else:
            return rendaBruta * 0.30 - 700

    