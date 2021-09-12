from NodeYear import NodeYear


class ListCircularDobleYear:
    def __init__(self):
        self.first = None
        self.end = None

    def AddListYear(self, Year):
        newYear = NodeYear(Year)
        if self.first is None:
            self.first = newYear
            self.end = self.first
            self.first.sig = None
            self.first.ant = None
        else:
            self.end.sig = newYear
            newYear.ant = self.end
            newYear.sig = None
            self.end = newYear

    def showListYear(self):
        aux = self.first
        while aux is not None:
            print('Este compa es del año ' + str(aux.Year))
            aux = aux.sig

    # buscar e insertar el mes
    def search_insert(self, year, mes):  # recibe el mes y anio
        aux = self.first

