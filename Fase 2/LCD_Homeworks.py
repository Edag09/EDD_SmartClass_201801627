from NodeHomework import Nodehomework
import os


class ListCircularDoubleHomeworks:
    def __init__(self):
        self.first = None
        self.end = None

    def AddHomeworks(self, id, carnet, name, description, materia, date, hora, status):
        newHomework = Nodehomework(id, carnet, name, description, materia, date, hora, status)
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
            print("Id tarea: " + str(aux.id) + " Carne: " + aux.Carne + ' Nombre de la tareas: ' + aux.Name + ' con descripcion ' + aux.Description + ' con fecha ' + aux.Date + ' a la hora ' + aux.Hora + ' y estado ' + aux.Status)
            aux = aux.sig

    def ShowGraph(self):
        aux = self.first
        data = ""
        pointer = ""
        cont = 1
        graph = "digraph List {\nrankdir=LR;\nnode [shape = circle, color=black , style=filled, fillcolor=gray93];\n"
        while aux is not None:
            data += "Node" + str(
                cont) + "[label=\"" + "Carne: " + aux.Carne + '\nNombre de la tarea: ' + aux.Name + ' \nDescripcion: ' + aux.Description + '\nFecha: ' + aux.Date + '\nHora: ' + aux.Hora + '\nEstado: ' + aux.Status + "\"];\n"
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
            print(print("No se genero :)"))

    # ---------------------------- CRUD Tareas :D ----------------------------
    # (Update(PUT) Homework)
    def Update(self, taskJ):
        aux = self.first
        while aux is not None:
            if aux.id == taskJ['ID']:
                aux.Carne = taskJ['Carnet']
                aux.Name = taskJ['Nombre']
                aux.Description = taskJ['Descripcion']
                aux.Materia = taskJ['Materia']
                aux.Date = taskJ['Fecha']
                aux.Hora = taskJ['Hora']
                aux.Status = taskJ['Estado']
            else:
                aux = aux.sig

    # (GET homework)
    def Get_Homework(self, id):
        aux = self.first
        while aux is not None:
            if aux.id == id:
                homework = {'Carnet': aux.Carne,
                            'Nombre': aux.Name,
                            'Descripcion': aux.Description,
                            'Materia': aux.Materia,
                            'Fecha': aux.Date,
                            'Hora': aux.Hora,
                            'Estado': aux.Status
                            }
                return homework
            else:
                aux = aux.sig

    # (DELETE homework)
    def Delete_homework(self, id):
        aux = self.first
        while aux is not None:
            if aux is not None:
                if self.first.id == id:
                    self.first.sig.ant = None
                    aux = aux.sig
                    self.first.sig = None
                    self.first = aux
                    return 'Eliminado al inicio'
                elif aux.id == id:
                    aux.ant.sig = aux.sig
                    aux.sig.ant = aux.ant
                    aux.ant = None
                    aux.sig = None
                    return 'Eliminado en medio'
                elif self.end.id == id:
                    self.end.ant.sig = None
                    aux = self.end.ant
                    self.end.ant = None
                    self.end = aux
                    return 'Eliminado al final'
                else:
                    return 'Id no valido'
            aux = aux.sig

