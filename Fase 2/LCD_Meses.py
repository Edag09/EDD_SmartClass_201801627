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
    def graphH(self, task, node):
        i = False
        while node is not None and i is False:
            if node.Mes != task.dispersa[1]:
                node = node.sig
            else:
                node.matrix.data.showH(node.matrix.columnM, node.matrix.rowM, task.dispersa[0], task.Hora, task)

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
            if node.Mes != mes:
                node = node.sig
            else:
                node.matrix.rowM.Insert_Headboard(hora)
                node.matrix.columnM.Insert_Headboard(day)
                i = True

    # recorrido para poder retornar la informacion de la tarea desde el inicio hasta la lista
    def get_Homework_M(self, mes, x, y, Id):
        aux = self.first
        while aux is not None:
            if aux.Mes != mes:
                aux = aux.sig
            else:
                return aux.matrix.data.get_Tarea(aux.matrix.columnM, aux.matrix.rowM, x, y, Id)

    # insertar tarea
    def insertH(self, task, node):
        i = False
        while (node is not None) and i is False:
            if node.Mes != task.dispersa[1]:
                node = node.sig
            else:
                tarea = NodeData(0, task.Hora, task.dispersa[0])
                if node.matrix.rowM.valHeadBoard(task.Hora) is False:
                    node.matrix.rowM.Insert_Headboard(task.Hora)
                    self.insertH(task, node)
                elif node.matrix.columnM.valHeadBoard(task.dispersa[0]) is False:
                    node.matrix.columnM.Insert_Headboard(task.dispersa[0])
                    self.insertH(task, node)
                else:
                    node.matrix.data.insert_nodeData(task.dispersa[0], task.Hora, node.matrix.columnM, node.matrix.rowM, tarea)
                    i = True

    # Insertar los elementos de la tarea desde Meses
    def insert_HomeworkM(self, task, node, carnet, nombre, descripcion, materia, fecha, hora, estado):
        i = False
        while (node is not None) and i is False:
            if node.Mes != task.dispersa[1]:
                node = node.sig
            else:
                node.matrix.data.find_Home(node.matrix.columnM, node.matrix.rowM, task.dispersa[0], task.Hora, carnet, nombre, descripcion, materia, fecha, hora, estado)
                i = True
