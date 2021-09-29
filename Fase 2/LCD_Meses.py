from NodeMes import NodeMes
from SparseMatrix import NodeData
import os


class ListCircularDoubleMeses:
    def __init__(self):
        self.first = None
        self.end = None

    # insertar meses
    def AddListMeses(self, Meses):
        newMes = NodeMes(Meses)
        if Meses == 1 or Meses == 2 or Meses == 3 or Meses == 4 or Meses == 5 or Meses == 7 or Meses == 8 or Meses == 9 or Meses == 10 or Meses == 11:
            if self.first is None:
                self.first = newMes
                self.end = self.first
                self.first.sig = None
                self.first.ant = None
            else:
                buscarme = self.buscarme(Meses)
                if buscarme is False:
                    self.end.sig = newMes
                    newMes.ant = self.end
                    newMes.sig = None
                    self.end = newMes
                    self.end = newMes
            print('Mes Fine')
        else:
            print('Mes incorrecto')

    # visualisar lista
    def showListMeses(self):
        aux = self.first
        while aux is not None:
            print('Este es el mes Nº ' + str(aux.Mes))
            aux = aux.sig

    # Grafo
    def ShowGraph(self):
        aux = self.first
        data = ""
        pointer = ""
        cont = 1
        graph = "digraph List {\nrankdir=LR;\nnode [shape = circle, color=black , style=filled, fillcolor=gray93];\n"
        while aux is not None:
            data += "Node" + str(cont) + "[label=\"" + "Mes : " + str(aux.Mes) + "\"];\n"
            if aux.sig is not None:
                pointer += "Node" + str(cont) + "->Node" + str(cont + 1) + ";\n"
                pointer += "Node" + str(cont + 1) + "->Node" + str(cont) + ";\n"
            cont += 1
            aux = aux.sig

        graph += data
        graph += pointer
        graph += "\n}"

        try:
            file = open("Meses.dot", "w", encoding='UTF-8')

            file.write(graph)

            file.close()

            os.system("dot -Tpng Meses.dot -o Meses.png")
            os.startfile("Meses.png")
        except:
            print("No se genero :)")

    # mostrar tareas
    def Go_Graph_HomeworksM(self, mes, day, hora, node):
        while node is not None:
            if node.Mes != int(mes):
                node = node.sig
            else:
                return node.matrix.data.showH(node.matrix.columnM, node.matrix.rowM, day, hora)

    # Validar mes
    def buscarme(self, mes):
        aux = self.first
        i = False
        while (aux is not None) and i is False:
            if aux.Mes != mes:
                aux = aux.sig
            else:
                i = True
        if aux is None:
            return False
        elif aux.Mes == mes:
            return True

    # validar e insertar cabecera
    def insert_headboard(self, mes, day, hora, node):
        i = False
        while (node is not None) and i is False:
            if node.Mes != int(mes):
                node = node.sig
            else:
                node.matrix.rowM.Insert_Headboard(hora)
                node.matrix.columnM.Insert_Headboard(day)
                i = True

    # ----------- recorrido para poder retornar la informacion de la tarea desde el inicio hasta la lista --------------
    # ---------------------------- Delete and Get of Homework from Mes -------------------------------------------------
    def get_Homework_M(self, mes, x, y, Id, peticion):  # elimina y obtiene la informacion de las tareas
        aux = self.first
        while aux is not None:
            if aux.Mes != int(mes):
                aux = aux.sig
            else:
                return aux.matrix.data.get_Tarea(aux.matrix.columnM, aux.matrix.rowM, x, y, Id, peticion)

    def update_Homework_M(self, mes, x, y, Id, peticion, taskJ):   # actualiza los datos de la tarea
        aux = self.first
        while aux is not None:
            if aux.Mes != int(mes):
                aux = aux.sig
            else:
                return aux.matrix.data.update_Tarea(aux.matrix.columnM, aux.matrix.rowM, x, y, Id, peticion, taskJ)

    # --------------------------------------- FIN CRUD HOMEWORKS FROM MES ----------------------------------------------

    # ---------------------------------------------- // insersion de la tarea // ----------------------------------
    # insertar tarea
    def insertH(self, task, node):
        i = False
        while (node is not None) and i is False:
            if node.Mes != int(task.dispersa[1]):
                node = node.sig
            else:
                hora = task.Hora.split(':')
                tarea = NodeData(0, hora[0], task.dispersa[0])
                if node.matrix.rowM.valHeadBoard(hora[0]) is False:
                    node.matrix.rowM.Insert_Headboard(hora[0])
                    self.insertH(task, node)
                elif node.matrix.columnM.valHeadBoard(task.dispersa[0]) is False:
                    node.matrix.columnM.Insert_Headboard(task.dispersa[0])
                    self.insertH(task, node)
                else:
                    node.matrix.data.insert_nodeData(task.dispersa[0], hora[0], node.matrix.columnM, node.matrix.rowM, tarea)
                    i = True

    # insertar la tarea a manita desde meses
    def insertH_a_manita(self, task, node, enlaces):
        i = False
        while (node is not None) and i is False:
            if node.Mes != int(enlaces[1]):
                node = node.sig
            else:
                hora = task['Hora'].split(":")
                tarea = NodeData(0, hora[0], enlaces[0])
                if node.matrix.rowM.valHeadBoard(hora[0]) is False:
                    node.matrix.rowM.Insert_Headboard(hora[0])
                    self.insertH_a_manita(task, node, enlaces)
                elif node.matrix.columnM.valHeadBoard(enlaces[0]) is False:
                    node.matrix.columnM.Insert_Headboard(enlaces[0])
                    self.insertH_a_manita(task, node, enlaces)
                else:
                    node.matrix.data.insert_nodeData(enlaces[0], hora[0], node.matrix.columnM, node.matrix.rowM, tarea)
                    i = True

    # Insertar los elementos de la tarea desde Meses
    def insert_HomeworkM(self, task, node, carnet, nombre, descripcion, materia, fecha, hora, estado):
        i = False
        while (node is not None) and i is False:
            if node.Mes != int(task.dispersa[1]):
                node = node.sig
            else:
                hor = task.Hora.split(':')
                node.matrix.data.find_Home(node.matrix.columnM, node.matrix.rowM, task.dispersa[0], hor[0], carnet, nombre, descripcion, materia, fecha, hora, estado)
                i = True

    # insertar los elementos de la tarea desde Meses a manita
    def insert_a_manita_HomeworkM(self, task, node, enlaces):
        i = False
        while (node is not None) and i is False:
            if node.Mes != int(enlaces[1]):
                node = node.sig
            else:
                hora = task['Hora'].split(':')
                node.matrix.data.find_pos_and_insert_homework_a_manita(node.matrix.columnM, node.matrix.rowM, enlaces[0], hora[0], task)
                i = True
