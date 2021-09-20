from NodeMatrix import NodeHeadboard


class HeadBoard:
    def __init__(self):
        self.first = None
        self.end = None

    def Insert_Headboard(self, day_hora):
        headboard = NodeHeadboard(day_hora)
        if self.first is None:
            self.first = headboard
            self.end = self.first
        else:
            if self.first.number == self.end.number:
                if day_hora > self.first.number:
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
                while (aux is not None) and (cond_headboard is False):
                    if day_hora == 1:
                        headboard.sig = self.first
                        self.first.ant = headboard
                        self.first = headboard
                        cond_headboard = True
                    elif day_hora > aux.number:
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
        self.cond_data = False

    def insert_nodeData(self, x, y, listX, listY, node):
        x_aux = listX.self.first
        y_aux = listY.self.first

        while x_aux.number is not x:
            x_aux = x_aux.sig
        listX = x_aux

        while y_aux.number is not y:
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
        headboardX = listX.self.first
        headboardY = listY.self.first
        while headboardX.number is not int(x):
            headboardX = headboardX.sig
        print("X es :", headboardX.number)

        while headboardY.number is not int(y):
            headboardY = headboardY.sig
        print("Y es: ", headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.down
        aux = headboardY.down
        self.cond_data = False
        while (aux is not None) and (self.cond_data is False):
            if (aux.rowData == x) and (aux.columnData == y):
                print(aux.data, end="->")
                self.cond_data = True
            else:
                aux = aux.down

    def find_Home(self, listX, listY, x, y, node):
        headboardX = listX.self.first
        headboardY = listY.self.first
        while headboardX.number is not int(x):
            headboardX = headboardX.sig
        print("X es :", headboardX.number)

        while headboardY.number is not int(y):
            headboardY = headboardY.sig
        print("Y es: ", headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.down
        aux = headboardY.down
        self.cond_data = False
        while (aux is not None) and (self.cond_data is False):
            if (aux.rowData == y) and (aux.columnData == x):
                # aux.ListHomework.AddHomeworks
                aux.data += 1
                self.cond_data = True
            else:
                aux = aux.down



