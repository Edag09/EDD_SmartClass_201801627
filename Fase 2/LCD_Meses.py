from NodeMes import NodeMes


class ListCircularDoubleMeses:
    def __init__(self):
        self.first = None
        self.end = None

    def AddListMeses(self, Meses):
        newMes = NodeMes(Meses)
        if Meses == 1 or Meses == 2 or Meses == 3 or Meses == 4 or Meses == 5 or Meses == 7 or Meses == 8 or Meses == 9 or Meses == 10 or Meses == 11:
            if self.first is None:
                self.first = newMes
                self.end = self.first
                self.first.sig = None
                self.first.ant = None
            else:
                self.end.sig = newMes
                newMes.ant = self.end
                newMes.sig = None
                self.end = newMes
                self.end = newMes
        else:
            print('Mes incorrecto')

    def showListMeses(self):
        aux = self.first
        while aux is not None:
            print('Este es el mes Nº ' + str(aux.Mes))
            aux = aux.sig
