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

    # mostrar los años
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
                node.mes.AddListMeses(int(mes))
                i = True

    # insertar semestre si existe el estudiante
    def insertSemester(self, year, semester, node):
        i = False
        while (node is not None) and i is False:
            if node.Year != year:
                node = node.sig
            else:
                node.semester.addListSemester(semester)
                i = True

    # validar year
    def findY(self, year):
        aux = self.first
        i = False
        while (aux is not None) and i is False:
            if aux.Year != year:
                aux = aux.sig
            else:
                i = True
        if aux is None:
            return False
        elif aux.Year == year:
            return True

    # Insert Curse
    def Insert_Curse(self, year, semester, codigo, nombre, creditos, prerequisitos, obligatorio, node):
        i = False
        while node is not None and i:
            if node.Year != year:
                node = node.sig
            else:
                node.semester.CurseB(semester, codigo, nombre, creditos, prerequisitos, obligatorio)
                i = True

    # find mes
    def find_Mes(self, year, mes, day, hora, node):
        i = False
        while node is not None and i:
            if node.Year != year:
                node = node.sig
            else:
                node.mes.insert_headboard(mes, day, hora, node.mes.first)
                i = True

    # recorrido para poder retornar la informacion de la tarea desde el inicio hasta la lista
    def get_Homework_year(self, year, mes, day, hora, Id):
        aux = self.first
        while aux is not None:
            if aux.Year != year:
                aux = aux.sig
            else:
                return aux.mes.get_Homework_M(mes, day, hora, Id)

    # graph homework
    def graph_Homeworks(self, task, node, lex):
        i = False
        while (node is not None) and i:
            if node.Year != task.dispersa[2]:
                node = node.sig
            else:
                if lex == 'insertar':
                    node.mes.insertH(task, node.mes.first)
                    i = True
                elif lex == 'tarea':
                    node.mes.graphH(task, node.mes.first)
                    i = True

    # ---------------------------------------- // Insertar tareas // -------------------------------------------

    # Insertar los elementos de la tarea desde years
    def insert_HomeworkY(self, task, node, lex, carnet, nombre, descripcion, materia, fecha, hora, estado):
        i = False
        while (node is not None) and i:
            if node.Year != task.dispersa[2]:
                node = node.sig
            else:
                if lex == 'insertar':
                    node.mes.insertH(task, node.mes.first)
                elif lex == 'tarea':
                    node.mes.insert_HomeworkM(task, node.mes.first, carnet, nombre, descripcion, materia, fecha, hora, estado)
                    i = True

    # insertar la tarea a manita desde años
    def insert_a_manita_HomeworkY(self, task, node, lex, enlaces):
        i = False
        while node is not None and i:
            if node.Year != enlaces[2]:
                node = node.sig
            else:
                if lex == 'insertar':
                    node.mes.insertH_a_manita(task, node.mes.first, enlaces)
                elif lex == 'tarea':
                    node.mes.insert_a_manita_HomeworkM(task, node.mes.first, enlaces)
                    i = True
