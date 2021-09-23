from NodeMatrix import NodeHeadboard
from NodeMatrix import NodeData
from NodeMatrix import NodeMatrix
from Analizadores import Analyzer

analisis = Analyzer()


class HeadBoard:
    def __init__(self):
        self.first = None
        self.end = None

    # Insertar Cabecera
    def Insert_Headboard(self, day_hora):
        if self.valHeadBoard(day_hora) is False :
            headboard = NodeHeadboard(day_hora)
            if self.first is None:
                self.first = headboard
                self.end = self.first
            else:
                if self.first.number == self.end.number:
                    if int(day_hora) > int(self.first.number):
                        self.end.sig = headboard
                        headboard.ant = self.end
                        self.end = headboard
                    else:
                        headboard.sig = self.first
                        self.first.ant = headboard
                        self.first = headboard
                else:
                    cond_headboard = False
                    aux = self.first
                    while (aux is not None) and cond_headboard is False:
                        if int(day_hora) == 1:
                            headboard.sig = self.first
                            self.first.ant = headboard
                            self.first = headboard
                            cond_headboard = True
                        elif int(day_hora) > int(aux.number):
                            aux = aux.sig
                        else:
                            headboard.ant = aux.ant
                            aux.ant.sig = headboard
                            aux.ant = headboard
                            headboard.sig = aux
                            cond_headboard = True
                    if (aux is None) and (cond_headboard is False):
                        self.end.sig = headboard
                        headboard.ant = self.end
                        self.end = headboard

    # Validaciones Cabeceras
    def valHeadBoard(self, day_hora):
        aux = self.first
        i = False
        if self.first is not None:
            while (aux is not None) and i is False:
                if aux.number == day_hora:
                    return True
            return False
        else:
            return False

    # Printear
    def show(self):
        aux = self.first
        while aux is not None:
            print(aux.number)
            aux = aux.sig


class Data:
    def __init__(self):
        self.headData = None
        self.sigListData = None
        self.antListData = None
        self.upListData = None
        self.downListData = None

    def insert_nodeData(self, x, y, listX, listY, node):
        x_aux = listX.first
        y_aux = listY.first

        while int(x_aux.number) != x:
            x_aux = x_aux.sig
        listX = x_aux

        while int(y_aux.number) != y:
            y_aux = y_aux.sig
        listY = y_aux

        if listX and listY:
            fin_x = listX
            fin_y = listY
            while fin_x.down is not None:
                fin_x = fin_x.down
            while fin_y.down is not None:
                fin_y = fin_y.down
            fin_x.down = node
            fin_y.down = node
            node.up = fin_x
            node.izq = fin_y
        else:
            listX = node
            listX.down = node
            listY = node
            listY.down = node

    def show(self, listX, listY, x, y):
        headboardX = listX.first
        headboardY = listY.first
        while int(headboardX.number) != int(x):
            headboardX = headboardX.sig
        print("X es :", headboardX.number)

        while int(headboardY.number) != int(y):
            headboardY = headboardY.sig
        print("Y es: ", headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.downData
        aux = headboardY.down
        cond_data = False
        while (aux is not None) and (cond_data is False):
            if (aux.rowData == x) and (aux.columnData == y):
                print(aux.data, end="->")
                cond_data = True
            else:
                aux = aux.down

    def find_Home(self, listX, listY, x, y):
        headboardX = listX.first
        headboardY = listY.first
        while int(headboardX.number) != int(x):
            headboardX = headboardX.sig
        print("X es :", headboardX.number)

        while int(headboardY.number) != int(y):
            headboardY = headboardY.sig
        print("Y es: ", headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.downData
        aux = headboardY.down
        cond_data = False
        while (aux is not None) and (cond_data is False):
            if (aux.rowData == y) and (aux.columnData == x):
                analisis.llenado()
                aux.data += 1
                cond_data = True
            else:
                aux = aux.down

    def get_Tarea(self, cabeceraX, cabeceraY, x, y, id):
        headboardX = cabeceraX.first
        headboardY = cabeceraY.first


