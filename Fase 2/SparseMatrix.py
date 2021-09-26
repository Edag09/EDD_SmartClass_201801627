from LCD_Homeworks import ListCircularDoubleHomeworks


class NodeHeadboard:
    def __init__(self, num):
        self.number = num
        self.sig = None
        self.ant = None
        self.up = None
        self.down = None


class NodeData:
    def __init__(self, data, row, column):
        self.data = data
        self.rowData = row
        self.columnData = column
        self.ListHomework = ListCircularDoubleHomeworks()
        self.sigData = None
        self.antData = None
        self.upData = None
        self.downData = None


class HeadBoard:
    def __init__(self):
        self.first = None
        self.end = None

    # Insertar Cabecera
    def Insert_Headboard(self, day_hora):
        if self.valHeadBoard(day_hora) is False:
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

    # insertar el nodo y crea el espacio en la matriz
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

    # Solo para ver si, si esta guardadno la informacion
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

    # ------------------------------------- // Insertar tareas // -------------------------
    # Busca la posicion donde se creo el espacio e inserta la tarea
    def find_Home(self, listX, listY, x, y, carnet, nombre, descripcion, materia, fecha, hora, estado):
        id = 1
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
                aux.data += 1
                aux.ListHomework.AddHomeworks(id, carnet, nombre, descripcion, materia, fecha, hora, estado)
                id += 1
                cond_data = True
            else:
                aux = aux.down

    def find_pos_and_insert_homework_a_manita(self, listX, listY, x, y, task):
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
                aux.data += 1
                aux.ListHomework.AddHomeworks(task['ID'], task['Carnet'], task['Nombre'], task['Descripcion'], task['Materia'], task['Fecha'], task['Hora'], task['Estado'])
                cond_data = True
            else:
                aux = aux.down

    # --------------------------------------- // Fin del insertar las tareas// ---------------------------------------

    # ----------------------------------------------- Obtine y/o elimina la informacion de la tarea --------------------
    def get_Tarea(self, cabeceraX, cabeceraY, x, y, id, peticion):
        headboardX = cabeceraX.first
        headboardY = cabeceraY.first

        while headboardX.number != x:
            headboardX = headboardX.sig
        print("X es: ", headboardX.number)

        while headboardY.number != y:
            headboardY = headboardY.sig
        print('Y es:', headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.downData
        aux = headboardY.down
        i = False
        while (aux is not None) and i is False:
            if aux.rowData == y and aux.columnData == x:
                if peticion == 'Obtener':
                    return aux.ListHomework.Get_Homework(id)
                elif peticion == 'Eliminar':
                    return aux.Delete_homework(id)
                i = True
            else:
                aux = aux.down

    def update_Tarea(self, cabeceraX, cabeceraY, x, y, id, peticion, taskJ):
        headboardX = cabeceraX.first
        headboardY = cabeceraY.first

        while headboardX.number != x:
            headboardX = headboardX.sig
        print("X es: ", headboardX.number)

        while headboardY.number != y:
            headboardY = headboardY.sig
        print('Y es:', headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.downData
        aux = headboardY.down
        i = False
        while (aux is not None) and i is False:
            if aux.rowData == y and aux.columnData == x:
                if peticion == 'Actualizar':
                    return aux.ListHomework.Update(taskJ)
                i = True
            else:
                aux = aux.down

    # ----------------------------------------------- FIN CRUD HOMEWORK ------------------------------------------------

    # Valida que la tarea exista
    def val_tar(self, Lx, Ly, x, y):
        headboardX = Lx.first
        headboardY = Ly.first
        i = False

        while headboardX.number != x:
            headboardX = headboardX.sig
        print("X es: ", headboardX.number)

        while headboardY.number != y:
            headboardY = headboardY.sig
        print('Y es:', headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.downData
        aux = headboardY
        while (aux is not None) and i is False:
            if (aux.rowData == y) and (aux.columnData == x):
                return True
        return False

    # mostrar tareas
    def showH(self, lx, ly, x, y):
        headboardX = lx.first
        headboardY = ly.first
        i = False
        while headboardX.number != x:
            headboardX = headboardX.sig
        print("X es: ", headboardX.number)

        while headboardY.number != y:
            headboardY = headboardY.sig
        print('Y es:', headboardY.number)

        aux = headboardX.down
        while aux is not None:
            aux = aux.downData
        aux = headboardY
        while (aux is not None) and i is False:
            if (aux.rowData == y) and (aux.columnData == x):
                aux.ListHomework.showList()
            else:
                aux = aux.down
