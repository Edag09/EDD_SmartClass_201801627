from ArbolB.NodeCurse import DoubleNodeCurse
import os


class ListCurse:
    def __init__(self):
        self.first = None
        self.end = None

    def addListCurse(self, codigo, nombre, creditos, prerrequisitos, obligatorio):
        newCurse = DoubleNodeCurse(codigo, nombre, creditos, prerrequisitos, obligatorio)
        if self.first is None:
            self.first = newCurse
            self.first.Sig = None
            self.first.Ant = None
            self.end = self.first
        else:
            self.end.Sig = newCurse
            newCurse.Sig = None
            newCurse.Ant = self.end
            self.end = newCurse

    def showList(self):
        aux = self.first
        while aux is not None:
            print("Curso: " + aux.Nombre + '\nCodigo: ' + aux.Codigo + "\nCreditos: " + str(aux.Creditos) + "\nPrerrequisitos: " + aux.Prerequisitos + "\nObligatorio: " + str(
                aux.Obligatorio) + "\n")
            aux = aux.Sig

    def busCode(self, code):
        aux = self.first
        while aux is not None:
            if int(aux.Codigo) == int(code):
                curse = list()
                curse.append(aux.Codigo)
                curse.append(aux.Nombre)
                curse.append(aux.Creditos)
                curse.append(aux.Prerequisitos.split(","))
                curse.append(aux.Obligatorio)
                return curse
            else:
                aux = aux.Sig

    def ShowGraph(self):
        aux = self.first
        graph = 'digraph MallaCurse {\ncharset=\"UTF-8\"\nrankdir=TB;\nNode [shape=rectangle, color=black, style=filled, fillcolor=gray93];\n'
        body = ""
        while aux is not None:
            body += 'Node' + aux.Codigo + '[label=\"' + aux.Codigo + '\\n ' + aux.Nombre + '\" ]; \n'
            auxP = aux.Prerequisitos.split(",")
            for pre in auxP:
                if pre != '':
                    body += 'Node' + pre + ' -> Node' + aux.Codigo + "\n"
            aux = aux.Sig
        graph += body
        graph += '\n}'
        try:
            file = open('SmartClass\\src\\assets\\Grafo\\Malla.dot', 'w', encoding='UTF-8')
            file.write(graph)
            file.close()
            os.system('dot -Tpng SmartClass\\src\\assets\\Grafo\\Malla.dot -o SmartClass\\src\\assets\\Grafo\\Malla.png')
            print('Si jalo :D')
        except:
            print('No se genero :)')
