from NodeHomework import Nodehomework
import os


class ListCircularDoubleHomeworks:
    def __init__(self):
        self.first = None
        self.end = None

    def AddHomeworks(self, carne, name, description, materia, date, hora, status):
        newHomework = Nodehomework(carne, name, description, materia, date, hora, status)
        if self.first is None:
            self.first = newHomework
            self.end = self.first
            self.first.sig = None
            self.first.ant = None
        else:
            self.end.sig = newHomework
            newHomework.ant = self.end
            newHomework.sig = None
            self.end = newHomework
            self.end = newHomework

    def showList(self):
        aux = self.first
        while aux is not None:
            print("Carne " + aux.Carne + ' Nombre de la tareas ' + aux.Name + ' con descripcion ' + aux.Description + ' con fecha ' + aux.Date + ' a la hora ' + aux.Hora + ' y estado ' + aux.Status)
            aux = aux.sig

    def ShowGraph(self):
        aux = self.first
        data = ""
        pointer = ""
        cont = 1
        graph = "digraph List {\nrankdir=LR;\nnode [shape = circle, color=black , style=filled, fillcolor=gray93];\n"
        while aux is not None:
            data += "Node" + str(cont) + "[label=\"" + "Carne: " + aux.Carne + '\nNombre de la tarea: ' + aux.Name + ' \nDescripcion: ' + aux.Description + '\nFecha: ' + aux.Date + '\nHora: ' + aux.Hora + '\nEstado: ' + aux.Status + "\"];\n"
            if aux.sig is not None:
                pointer += "Node" + str(cont) + "->Node" + str(cont + 1) + ";\n"
                pointer += "Node" + str(cont + 1) + "->Node" + str(cont) + ";\n"
            cont += 1
            aux = aux.sig

        graph += data
        graph += pointer
        graph += "\n}"

        try:
            file = open("Tareas.dot", "w", encoding='UTF-8')

            file.write(graph)

            file.close()

            os.system("dot -Tpng Tareas.dot -o Tareas.png")
            os.startfile("Tareas.png")
        except:
            print("No se genero :)")