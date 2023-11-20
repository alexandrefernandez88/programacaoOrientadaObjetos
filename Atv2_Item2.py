# Escreva uma classe em Python para representar um Horário. Esta classe deve conter dois atributos do tipo inteiro denominados de hora e minuto. Faça também:
# Um método para incrementar o horário em uma hora, note que se a hora for 23, passamos para o próximo dia, portanto a hora deverá ser 0.
# Método para decrementar o horário em uma hora, note que se a hora for 0 ela deverá voltar às 23 horas.
# Método para decrementar o horário em um minuto. Faça as consistências necessárias.
# Método para incrementar o horário em um minuto. Faça as consistências necessárias.
# Método para retornar o horário na forma de string (hh:mm).
# Método que verifica se o horário representa um valor “antes do meio dia” ou “após o meio dia”. O método retorna “AM” ou “PM”
#---------------------------------------------------------------------------------
# Atividade 2 de Programação Orientada a Objeto
# Item 01/03
# Alexandre Fernandez - RA10482120706

class horarioAtual():
    def __init__(self, hora: int, minuto: int):
        self.hora = hora
        self.minuto = minuto


    def agora(self):
        print('A hora é1:', self.hora,':', self.minuto)


    def incremetarUmaHora(self):
        if self.hora == 23:
                self.hora = 00
                print('A hora é2:', self.hora, ':', self.minuto)
        else:
            self.hora + 1
            print('A hora é3:', self.hora + 1, ':', self.minuto)


    def decremetarUmaHora(self):
        print('A hora é4:', self.hora - 1, ':', self.minuto)


    def incremetarUmMinuto(self):
        if self.minuto == 59:
            self.minuto = 00
            print('A hora é5:', self.hora + 1, ':', self.minuto)
        else:
            self.minuto + 1
            print('A hora é6:', self.hora, ':', self.minuto + 1)


    def decremetarUmMinuto(self):
        print('A hora é7:', self.hora, ':', self.minuto - 1)


    def retornaHoraEmString(self):
        print('Em string fica8: ', '%d e %d'%(self.hora, self.minuto))


    def AmPm(self):
        if self.hora < 12:
            print('O período9 é AM')
        else:
            print('O período10 é PM')


horario = horarioAtual(hora=20, minuto=49)
horario.agora()
horario.incremetarUmaHora()
horario.decremetarUmaHora()
horario.incremetarUmMinuto()
horario.decremetarUmMinuto()
horario.retornaHoraEmString()
horario.AmPm()