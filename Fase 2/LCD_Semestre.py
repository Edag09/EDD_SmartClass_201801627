from NodeSemestre import NodeSemester
import os



class ListCircularDoubleSemester:
    def __init__(self):
        self.first = None
        self.end = None

    def addListSemester(self, Semester):
        newSemester = NodeSemester(Semester)
        if (Semester == 1) or (Semester == 2):
            if self.first is None:
                self.first = newSemester
                self.first.sig = None
                self.first.ant = None
                self.end = self.first
            else:
                self.end.sig = newSemester
                newSemester.sig = None
                newSemester.ant = self.end
                self.end = newSemester
        else:
            print("Semestre no valido")

    def showList(self):
        aux = self.first
        while aux is not None:
            print("Estamos en el semestre " + str(aux.Semester))
            aux = aux.sig

    def showGraph(self):
        aux = self.first
        data = ""
        pointer = ""
        cont = 1
        graph = "digraph List {\nrankdir=LR;\nnode [shape = circle, color=black , style=filled, fillcolor=gray93];\n"
        while aux is not None:
            data += "Node" + str(cont) + "[label=\"" + "Semestre: " + str(aux.Semester) + "\"];\n"
            if aux.sig is not None:
                pointer += "Node" + str(cont) + "->Node" + str(cont + 1) + ";\n"
                pointer += "Node" + str(cont + 1) + "->Node" + str(cont) + ";\n"
            cont += 1
            aux = aux.sig

        graph += data
        graph += pointer
        graph += "\n}"

        try:
            file = open("Semester.dot", "w", encoding='UTF-8')

            file.write(graph)

            file.close()

            os.system("dot -Tpng Semester.dot -o Semester.png")
            os.startfile("Semester.png")
        except:
            print("No se genero :)")

    # validar semestre
    def val_Semester(self, semester):
        aux = self.first
        i = False
        while (aux is not None) and i:
            if aux.Semester != semester:
                aux = aux.sig
            else:
                i = True
        if aux is None:
            return False
        elif aux.Semester == semester:
            return False

    # insertar cursos
    def CurseB(self, semester, codigo, nombre, creditos, prerequisitos, obligatorio):
        aux = self.first
        i = False
        while aux is not None and i:
            if aux.Semester != semester:
                aux = aux.sig
            else:
                aux.cur.addListCurse(codigo, nombre, creditos, prerequisitos, obligatorio)
                i = True
