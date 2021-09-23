from NodeMes import NodeMes
import os


class ListCircularDoubleMeses:
    def __init__(self):
        self.first = None
        self.end = None

    def AddListMeses(self, Meses):
        newMes = NodeMes(Meses)
        if Meses == 1 or Meses == 2 or Meses == 3 or Meses == 4 or Meses == 5 or Meses == 7 or Meses == 8 or Meses == 9 or Meses == 10 or Meses == 11:
            if self.first is None:
                self.first = newMes
                self.end = self.first
                self.first.sig = None
                self.first.ant = None
            else:
                self.end.sig = newMes
                newMes.ant = self.end
                newMes.sig = None
                self.end = newMes
                self.end = newMes
        else:
            print('Mes incorrecto')

    def showListMeses(self):
        aux = self.first
        while aux is not None:
            print('Este es el mes Nº ' + str(aux.Mes))
            aux = aux.sig

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