from Arista import Edge
import os


class GraphCurse:
    def __init__(self):
        self.first = None

    def AddG(self, codigo, curso, creditos, prerequisitos):
        graphCurse = Edge(codigo, curso, creditos, prerequisitos)
        if self.first is None:
            self.first = graphCurse
        else:
            if self.val(codigo) is False:
                graphCurse.Sig = self.first
                self.first = graphCurse

    def val(self, code):
        aux = self.first
        while aux is not None:
            if aux.Codigo == code:
                return True
            else:
                aux = aux.Sig
        return False

    def ShowGraphCurse(self):
        aux = self.first
        graph = 'digraph Curse {\ncharset=\"UTF-8\"\nrankdir=TB;\nNode [shape=rectangle, color=black, style=filled, fillcolor=gray93];\n'
        body = ""
        while aux is not None:
            body += 'Node' + aux.Codigo + '[label=\"' + aux.Codigo + '\\n ' + aux.Curso + '\" ]; \n'
            for pre in aux.Prerequisitos:
                if pre != '':
                    body += 'Node' + pre + ' -> Node' + aux.Codigo + '[label=\"' + str(aux.Creditos) + "\"]\n"
            aux = aux.Sig
        graph += body
        graph += '\n}'
        try:
            file = open('SmartClass\\src\\assets\\Grafo\\CurseStudent.dot', 'w', encoding='UTF-8')
            file.write(graph)
            file.close()
            os.system('dot -Tpng SmartClass\\src\\assets\\Grafo\\CurseStudent.dot -o SmartClass\\src\\assets\\Grafo\\CurseStudent.png')
            print('Si jalo :D')
        except:
            print('No se genero :)')
