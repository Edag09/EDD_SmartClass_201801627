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

    # insertar mes si existe estudiante
    def insertM(self, year, mes, node):
        i = False
        while (node is not None) and i is False:
            if node.Year != year:
                node = node.sig
            else:
                node.mes.AddListMeses(mes)
                i = True
        node.mes.showListMeses()

    # insertar semestre si existe el estudiante
    def insertSemester(self, year, semester, node):
        i = False
        while (node is not None) and i is False:
            if node.Year != year:
                node = node.sig
            else:
                node.semester.addListSemester(semester)
                i = True
        node.semester.showList()


