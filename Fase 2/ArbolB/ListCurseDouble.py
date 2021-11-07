from ArbolB.NodeCurse import DoubleNodeCurse


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
            print("Curso: " + aux.Nombre + '\nCodigo: ' + aux.Codigo + "\nCreditos: " + str(aux.Creditos) + "\nPrerrequisitos: " + aux.Prerequisitos + "\nObligatorio: " + str(aux.Obligatorio) + "\n")
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
