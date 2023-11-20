# Desenvolva em Python a classe de nome CodigoPostal, cujo objetos sejam capazes de guardar o código postal de uma dada rua. Note que cada Código Postal é constituído por dois números inteiros, que designaremos respectivamente por "indicativo" e "extensão" e o nome da rua (Ex: 38408-046 Armando Lombardi).
# Implemente também o método mostra(), cuja evocação, permita visualizar a informação relativa a um determinado código postal no formato:  CEP: 38408 - 046 Armando Lombardi.
# Escreva um programa de teste para a classe CodigoPostal. Crie várias instâncias da classe e teste o objeto.
#----------------------------------------------------------------------------------------------------------
# Atividade 2 de Programação Orientada a Objeto
# Item 01/03
# Alexandre Fernandez - RA10482120706

class CodigoPostal():
    def __init__(self, indicativo: int, extensao: int, nomeRua: str):
        self.indicativo = indicativo
        self.extensao = extensao
        self.nomeRua = nomeRua

    def mostra(self):
        print('Endereçamento postal CEP:', self.indicativo, '-', self.extensao, self.nomeRua, '!')

print('---------------------------')
primeiroEndereco = CodigoPostal(indicativo=1900, extensao=100, nomeRua='Avenida Central')
segundoEndereco = CodigoPostal(indicativo=27804, extensao=274, nomeRua='Rua Esquerda Fica ao Lado')
terceiroEndereco = CodigoPostal(indicativo=1900, extensao=100, nomeRua='Alameda Yolanda')
primeiroEndereco.mostra()
segundoEndereco.mostra()
terceiroEndereco.mostra()